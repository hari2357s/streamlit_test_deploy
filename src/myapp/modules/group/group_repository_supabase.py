"""
Docstring for myapp.Modules.group.group_repository
"""

from collections.abc import Iterator
from supabase import Client
from typing import cast
from myapp.common.database import IDatabase

from .group_repo import Group, IGroupRepo


class GroupRepositorySupaBase(IGroupRepo):
    """
    Docstring for GroupRepository
    """

    def __init__(self, db: IDatabase) -> None:
        self.db = db

    def add_member(self, member_id: int, group_id: int, role: str):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("user_group").insert({"userid":member_id, "groupid":group_id, "role":role}).execute()

    def create(self, user_id: int, group_name: str) -> int:
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            res = supabase.from_("groups").insert({"name" : group_name}).execute()
            group_id = res.data[0]["id"]
            self.add_member(user_id, group_id, "ADMIN")
            return group_id

    def get_all(self, user_id: int) -> Iterator[Group]:
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            response = ( supabase.table("user_group").select("""
                                    role, groups!user_group_groupid_fkey 
                                    ( id, name, createdat ) """
                                )
                                .eq("userid", user_id)
                                .execute()
                        )
            grps = response.data
            return (Group(id=grp["groups"]["id"], 
                          name=grp["groups"]["name"],
                          createdAt=grp["groups"]["createdat"],
                          role=grp["role"]) for grp in grps)

    def update(self, new_name: str, group_id: int):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("groups").update({"name" : new_name}).eq("id", group_id).execute()

    def delete(self, group_id: int):
        with self.db.transaction() as supabase:
            supabase = cast(Client, supabase)
            supabase.from_("groups").delete().eq("id", group_id).execute()
