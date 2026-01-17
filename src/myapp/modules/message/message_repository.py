"""
Docstring for myapp.Modules.message.message_repository
"""

from collections.abc import Iterator

from myapp.common.database import IDatabase

from .message_repo import IMessageRepo, Message


class MessageRepository(IMessageRepo):
    """
    Docstring for MessageRepository
    """

    def __init__(self, db: IDatabase) -> None:
        self.db = db
        self.create_table()

    def create_table(self):
        with self.db.transaction() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS MESSAGE(
                                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  MESSAGE TEXT NOT NULL,
                                  USERID INTEGER NOT NULL,
                                  CHATID INTEGER ,
                                  GROUPID INTEGER,
                                  TYPE TEXT NOT NULL,
                                  SENTAT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                  DELIVEREDAT TIMESTAMP ,
                                  SEENAT TIMESTAMP ,
                                  FOREIGN KEY(USERID) REFERENCES USER(USERID) ON DELETE CASCADE,
                                  FOREIGN KEY(CHATID) REFERENCES CHAT(ID) ON DELETE CASCADE,
                                  FOREIGN KEY(GROUPID) REFERENCES GROUPS(ID) ON DELETE CASCADE
                                )""")

    def add_msg(
        self,
        msg: str,
        user_id: int,
        chat_id: int | None,
        grp_id: int | None,
        msg_type: str,
    ):
        with self.db.transaction() as cur:
            cur.execute(
                """INSERT INTO MESSAGE (MESSAGE, USERID, CHATID, GROUPID, TYPE) VALUES(?,?,?,?,?)""",
                (msg, user_id, chat_id, grp_id, msg_type),
            )
            
    def update_msg(
        self,
        updated_msg: str,
        msg_id: int
    ):
        with self.db.transaction() as cur:
            cur.execute(
                '''UPDATE MESSAGE SET MESSAGE = ? WHERE ID = ?''',
                (updated_msg, msg_id,)
            )

    def get_all_msg(
        self, uid: int, chat_id: int | None, group_id: int | None
    ) -> Iterator[Message]:
        with self.db.transaction() as cur:
            if chat_id is not None:
                cur.execute(
                    """SELECT ID, MESSAGE, U.USERID, USERNAME, CHATID, GROUPID, SENTAT, DELIVEREDAT, SEENAT 
                                FROM MESSAGE M JOIN USER U ON M.USERID = U.USERID 
                                WHERE CHATID = ? ORDER BY SENTAT """,
                    (chat_id,),
                )
            else:
                cur.execute(
                    """SELECT ID, MESSAGE, U.USERID, U.USERNAME, CHATID, GROUPID, SENTAT, DELIVEREDAT, SEENAT 
                                FROM MESSAGE M JOIN USER U ON M.USERID = U.USERID
                                WHERE GROUPID = ?  ORDER BY SENTAT """,
                    (group_id,),
                )
            msgs = cur.fetchall()
            return (Message(*msg) for msg in msgs)

    def delete_msg(self, msg_id: int):
        with self.db.transaction() as cur:
            cur.execute("""DELETE FROM MESSAGE WHERE ID = ?""", (msg_id,))
