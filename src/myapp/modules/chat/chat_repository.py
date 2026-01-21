"""
Docstring for myapp.Modules.chat.chat_repository
"""

from collections.abc import Iterator
from typing import Any

from myapp.common.database import IDatabase

from .chat_repo import Chat, IChatRepo


class ChatRepository(IChatRepo):
    """
    Docstring for ChatRepository
    """

    def __init__(self, db: IDatabase) -> None:
        self.db = db
        # self.create_table()

    def create_table(self):
        """
        Docstring for create_table

        :param self: Description
        """
        with self.db.transaction() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS CHAT (
                                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  NAME TEXT )""")

            cur.execute("""CREATE TABLE IF NOT EXISTS USER_CHAT(
                                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  USERID INTEGER NOT NULL,
                                  CHATID INTEGER NOT NULL,
                                  BLOCKED INTEGER DEFAULT 0,
                                  FOREIGN KEY(USERID) REFERENCES USERS(USERID) ON DELETE CASCADE,
                                  FOREIGN KEY(CHATID) REFERENCES CHAT(ID) ON DELETE CASCADE)""")

    def add(self, user_id: int, frnd_uid: int):
        """
        Docstring for add

        :param self: Description
        :param userID: Description
        :type userID: int
        :param frndUID: Description
        :type frndUID: int
        """
        with self.db.transaction() as cur:
            cur.execute("""INSERT INTO CHAT (NAME) VALUES(NULL)""")
            chat_id = cur.lastrowid
            cur.execute(
                """INSERT INTO USER_CHAT (USERID, CHATID) VALUES(%s,%s)""",
                (user_id, chat_id),
            )
            cur.execute(
                """INSERT INTO USER_CHAT (USERID, CHATID) VALUES(%s,%s)""",
                (frnd_uid, chat_id),
            )

    def get_all(self, user_id: int) -> Iterator[Chat]:
        """
        Docstring for get_all

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Chat, ...]
        """
        with self.db.transaction() as cur:
            cur.execute(
                """SELECT UC2.ID, U.USERID, U.USERNAME, UC2.CHATID, UC2.BLOCKED FROM USERS U
                            JOIN USER_CHAT UC1 ON U.USERID = UC1.USERID
                            JOIN USER_CHAT UC2 ON UC1.CHATID = UC2.CHATID
                            WHERE UC2.USERID = %s AND U.USERID != %s""",
                (user_id, user_id),
            )
            chats = cur.fetchall()
            return (Chat(*chat) for chat in chats)

    def get_not_in_chat(self, user_id: int) -> tuple[Any]:
        """
        Docstring for get_not_in_chat

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Any]
        """
        with self.db.transaction() as cur:
            cur.execute(
                """SELECT USERID, USERNAME FROM USERS
                            WHERE USERID <> %s
                            AND USERID NOT IN (
                                SELECT UC1.USERID
                                FROM USER_CHAT UC1
                                JOIN USER_CHAT UC2 ON UC1.CHATID = UC2.CHATID
                                WHERE UC2.USERID = %s
                            )""",
                (user_id, user_id),
            )
            users = cur.fetchall()
            return tuple(users)

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
        with self.db.transaction() as cur:
            cur.execute(
                """UPDATE USER_CHAT SET BLOCKED = %s WHERE USERID = %s AND CHATID = %s""",
                (blocked, user_id, chat_id),
            )

    def delete(self, chat_id: int):
        """
        Docstring for delete

        :param self: Description
        :param chatID: Description
        :type chatID: int
        """
        with self.db.transaction() as cur:
            cur.execute("""DELETE FROM CHAT WHERE ID = %s""", (chat_id,))
