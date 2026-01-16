"""
Docstring for myapp.Modules.group.group_repository
"""

from collections.abc import Iterator

from myapp.common.database import IDatabase

from .group_repo import Group, IGroupRepo


class GroupRepository(IGroupRepo):
    """
    Docstring for GroupRepository
    """

    def __init__(self, db: IDatabase) -> None:
        self.db = db
        self.create_table()

    def create_table(self):
        with self.db.transaction() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS GROUPS(
                                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  NAME TEXT NOT NULL,
                                  CREATEDAT TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

            cur.execute("""CREATE TABLE IF NOT EXISTS USER_GROUP(
                                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  USERID INTEGER NOT NULL,
                                  GROUPID INTEGER NOT NULL,
                                  ROLE TEXT NOT NULL,
                                  FOREIGN KEY(USERID) REFERENCES USER(USERID) ON DELETE CASCADE,
                                  FOREIGN KEY(GROUPID) REFERENCES GROUPS(ID) ON DELETE CASCADE)""")

    def add_members(self, member_id: int, group_id: int, role: str):
        with self.db.transaction() as cur:
            cur.execute(
                """INSERT INTO USER_GROUP (USERID, GROUPID, ROLE) VALUES(?,?,?)""",
                (member_id, group_id, role),
            )

    def create(self, user_id: int, group_name: str) -> int:
        with self.db.transaction() as cur:
            cur.execute(
                """INSERT INTO GROUPS (
                                    NAME) VALUES(?)""",
                (group_name,),
            )
            group_id = cur.lastrowid
            if group_id is None:
                raise Exception("Error group id is None")
            self.add_members(user_id, group_id, "ADMIN")
            return group_id

    def get_all(self, user_id: int) -> Iterator[Group]:
        with self.db.transaction() as cur:
            cur.execute(
                """SELECT G.ID, G.NAME, G.CREATEDAT, UG.ROLE FROM 
                                            GROUPS G JOIN 
                                            USER_GROUP UG ON G.ID = UG.GROUPID WHERE 
                                            UG.USERID = ?""",
                (user_id,),
            )
            grps = cur.fetchall()
            return (Group(*grp) for grp in grps)

    def update(self, new_name: str, group_id: int):
        with self.db.transaction() as cur:
            cur.execute(
                """UPDATE GROUPS SET NAME = ? WHERE ID = ?""", (new_name, group_id)
            )

    def delete(self, group_id: int):
        with self.db.transaction() as cur:
            cur.execute("""DELETE FROM GROUPS WHERE ID = ?""", (group_id,))
