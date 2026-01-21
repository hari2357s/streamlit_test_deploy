"""
Docstring for myapp.Modules.user.user_repository
"""

import sqlite3

from myapp.common.database import IDatabase

from .user_repo import IUserRepo, User


class UserRepository(IUserRepo):
    """
    Docstring for UserRepository
    """

    def __init__(self, db: IDatabase):
        self.db = db
        # self.create_table()

    def create_table(self):
        with self.db.transaction() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS USERS(
                                  USERID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  USERNAME TEXT NOT NULL UNIQUE,
                                  PASSWORD TEXT NOT NULL,
                                  STATUS INTEGER DEFAULT 0,
                                  LASTSEEN TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                  )""")

    def add(self, uname: str, upass: str):
        with self.db.transaction() as cur:
            cur.execute(
                """INSERT INTO USERS(USERNAME, PASSWORD) 
                                    VALUES(%s,%s)""",
                (uname, self.sha512(upass)),
            )

    def get(self, uname: str, upass: str) -> User | None:
        with self.db.transaction() as cur:
            cur.execute(
                """SELECT USERID , USERNAME , LASTSEEN FROM 
                    USERS WHERE USERNAME = %s AND PASSWORD = %s""",
                (uname, self.sha512(upass)),
            )
            row = cur.fetchone()
            if row is None:
                return None

        return User(*row)

    def update(self, uid: int, new_name: str):
        with self.db.transaction() as cur:
            cur.execute(
                """UPDATE USERS SET USERNAME = %s WHERE USERID = %s""", (new_name, uid)
            )

    def delete(self, uid: int):
        with self.db.transaction() as cur:
            cur.execute("""DELETE FROM USERS WHERE USERID = %s""", (uid,))
