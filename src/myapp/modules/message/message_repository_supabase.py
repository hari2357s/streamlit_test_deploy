"""
Docstring for myapp.Modules.message.message_repository
"""

from collections.abc import Iterator
from typing import cast

from supabase import Client

from myapp.common.constants import ChatType
from myapp.common.database import IDatabase

from .message_repo import IMessageRepo, Message


class MessageRepositorySupaBase(IMessageRepo):
    """
    Docstring for MessageRepository
    """

    def __init__(self, db: IDatabase) -> None:
        self.db = db

    def add_msg(
        self,
        msg: str,
        user_id: int,
        chat_id: int | None,
        grp_id: int | None,
        msg_type: ChatType,
    ):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("message").insert(
                {
                    "message": msg,
                    "userid": user_id,
                    "chatid": chat_id,
                    "groupid": grp_id,
                    "type": msg_type.value,
                }
            ).execute()

    def update_msg(self, updated_msg: str, msg_id: int):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("message").update({"message": updated_msg}).eq(
                "id", msg_id
            ).execute()

    def get_all_msg(
        self, uid: int, chat_id: int | None, group_id: int | None
    ) -> Iterator[Message]:
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            query = (
                supabase.table("message")
                .select("""id, message, chatid, groupid, sentat, deliveredat, seenat,
                                users!message_userid_fkey ( userid, username ) """)
                .order("sentat")
            )
            if chat_id is not None:
                query = query.eq("chatid", chat_id)
            else:
                query = query.eq("groupid", group_id)

            res = query.execute()
            msgs = res.data
            return (
                Message(
                    id=msg["id"],
                    msg=msg["message"],
                    userID=msg["users"]["userid"],
                    userName=msg["users"]["username"],
                    chat_id=msg["chatid"],
                    group_id=msg["groupid"],
                    sentAt=msg["sentat"],
                    deliveredAt=msg["deliveredat"],
                    seenAt=msg["seenat"],
                )
                for msg in msgs
            )

    def delete_msg(self, msg_id: int):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("message").delete().eq("id", msg_id).execute()
