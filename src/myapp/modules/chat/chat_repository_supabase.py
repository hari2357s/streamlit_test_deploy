"""
Docstring for myapp.Modules.chat.chat_repository
"""

from collections.abc import Iterator
from typing import Any, cast
from supabase import Client

from myapp.common.database import IDatabase
from .chat_repo import Chat, IChatRepo


class ChatRepositorySupaBase(IChatRepo):
    """
    Docstring for ChatRepository
    """

    def __init__(self, db: IDatabase) -> None:
        self.db = db

    def add(self, user_id: int, frnd_uid: int):
        """
        Docstring for add

        :param self: Description
        :param userID: Description
        :type userID: int
        :param frndUID: Description
        :type frndUID: int
        """
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            res = supabase.from_("chat").insert({"name" : "NULL"}).execute()
            chat_id = res.data[0].get("id") # type: ignore
            supabase.from_("user_chat").insert({'userid': user_id, 'chatid': chat_id}).execute()
            supabase.from_("user_chat").insert({'userid': frnd_uid, 'chatid': chat_id}).execute()

    def get_all(self, user_id: int) -> Iterator[Chat]:
        """
        Docstring for get_all

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Chat, ...]
        """
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            res = supabase.from_("get_all_contacts").select('user_chatid,frnd_userid, frnd_username, chatid, blocked').eq("userid", user_id).execute()
            chats = res.data
            return(Chat(*chat.values()) for chat in chats)

    def get_not_in_chat(self, user_id: int) -> tuple[Any]:
        """
        Docstring for get_not_in_chat

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Any]
        """
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            chat_ids_resp = (
                supabase
                .table("user_chat")
                .select("chatid")
                .eq("userid", user_id)
                .execute()
            )

            chat_ids = [row["chatid"] for row in chat_ids_resp.data]
            
            shared_users_resp = (
                supabase
                .table("user_chat")
                .select("userid")
                .in_("chatid", chat_ids)
                .execute()
            )

            blocked_user_ids = {row["userid"] for row in shared_users_resp.data}
            blocked_user_ids.add(user_id)  # exclude self
            
            users_resp = (
                supabase
                .table("users")
                .select("userid, username")
                .not_.in_("userid", list(blocked_user_ids))
                .execute()
            )

            return tuple(
                (u["userid"], u["username"])
                for u in users_resp.data
            )

    def update(self, user_id: int, chat_id: int, blocked: int):
        """
        Docstring for update

        :param self: Description
        :param userID: Description
        :type userID: int
        :param chatID: Description
        :type chatID: int
        :param blocked: Description
        :type blocked: int
        """
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("user_chat").update({'blocked':blocked}).eq("userid", user_id).eq({"chatid" : chat_id}).execute()

    def delete(self, chat_id: int):
        """
        Docstring for delete

        :param self: Description
        :param chatID: Description
        :type chatID: int
        """
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("chat").delete().eq("id", chat_id)