"""
Docstring for myapp.Modules.user.user_repository
"""

from typing import cast

from supabase import Client

from myapp.common.database import IDatabase

from .user_repo import IUserRepo, User


class UserRepositorySupaBase(IUserRepo):
    """
    Docstring for UserRepository
    """

    def __init__(self, db: IDatabase):
        self.db = db

    def add(self, uname: str, upass: str):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            data = {"username": uname, "password": self.sha512(upass)}
            supabase.from_("users").insert(data).execute()

    def get(self, uname: str, upass: str) -> User | None:
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            res = (
                supabase.from_("users")
                .select("userid", "username", "lastseen")
                .eq("username", uname)
                .eq("password", self.sha512(upass))
                .execute()
            )
            # if res.data:
            return User(*tuple(res.data[0].values())) if res.data else None
            # else:
            #     return None

    def update(self, uid: int, new_name: str):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("users").update({"username": new_name}).eq(
                "userid", uid
            ).execute()

    def delete(self, uid: int):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("users").delete().eq("userid", uid).execute()
