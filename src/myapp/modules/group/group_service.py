"""
Docstring for myapp.Modules.group.group_service
"""

from .group_repo import GroupResponse, IGroupRepo


class GroupServices:
    """
    Docstring for GroupServices
    """

    def __init__(self, grp_repo: IGroupRepo) -> None:
        self.__grp_repo = grp_repo

    def create_group(self, user_id: int, group_name: str, member_ids: list[int]):
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
        group_id = self.__grp_repo.create(user_id, group_name)
        try:
            for memeber_id in member_ids:
                self.__grp_repo.add_members(memeber_id, group_id, "MEMBER")
        except Exception:
            raise
        return GroupResponse(200, "Successfully group created", [])

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
        return GroupResponse(200, "Successfully got all groups", data)

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
            return GroupResponse(500, str(exc), [])
        return GroupResponse(200, "Successfully deleted group", [])
