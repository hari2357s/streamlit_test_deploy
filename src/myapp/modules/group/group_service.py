"""
Docstring for myapp.Modules.group.group_service
"""

from myapp.common.constants import HTTP

from .group_repo import GroupResponse, IGroupRepo


class GroupServices:
    """
    Docstring for GroupServices
    """

    def __init__(self, grp_repo: IGroupRepo) -> None:
        self.__grp_repo = grp_repo

    def add_members(
        self, user_id: int, group_id: int, member_ids: tuple[int, ...], role: str
    ):
        """
        Docstring for add_members

        :param self: Description
        :param user_id: Description
        :type user_id: int
        :param group_id: Description
        :type group_id: int
        :param member_ids: Description
        :type member_ids: tuple[int]
        """
        try:
            # need to validate whether the user_id is ADMIN or not
            for member_id in member_ids:
                self.__grp_repo.add_member(member_id, group_id, role)
        except Exception as exc:
            return GroupResponse(HTTP.INTERNAL_SERVER_ERROR, str(exc.args), [])
        return GroupResponse(HTTP.OK, "Successfully group created", [])

    def create_group(self, user_id: int, group_name: str, member_ids: tuple[int, ...]):
        """
        Docstring for createGroup

        :param self: Description
        :param userID: Description
        :type userID: int
        :param groupName: Description
        :type groupName: str
        :param memberIDs: Description
        :type memberIDs: list[int]
        """
        try:
            group_id = self.__grp_repo.create(user_id, group_name)
            self.add_members(user_id, group_id, member_ids, "MEMBER")
            # for member_id in member_ids:
            #     self.__grp_repo.add_member(member_id, group_id, "MEMBER")
        except Exception as exc:
            return GroupResponse(HTTP.INTERNAL_SERVER_ERROR, str(exc.args), [])
        return GroupResponse(HTTP.OK, "Successfully group created", [])

    def get_all_groups(self, user_id: int) -> GroupResponse:
        """
        Docstring for getAllGroups

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: GroupResponse
        """
        data = self.__grp_repo.get_all(user_id)
        return GroupResponse(HTTP.OK, "Successfully got all groups", data)

    def delete_group(self, group_id: int):
        """
        Docstring for delete_group

        :param self: Description
        :param grp_id: Description
        :type grp_id: int
        """
        try:
            self.__grp_repo.delete(group_id)
        except ValueError as exc:
            return GroupResponse(HTTP.INTERNAL_SERVER_ERROR, str(exc.args), [])
        return GroupResponse(HTTP.OK, "Successfully deleted group", [])
