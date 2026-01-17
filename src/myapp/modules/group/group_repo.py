"""
Docstring for myapp.Modules.group.group_repo
"""

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from datetime import datetime
from typing import NamedTuple

from myapp.common.repository import IRepository
from myapp.common.response import Response


class Group(NamedTuple):
    """
    Docstring for Group
    """

    id: int
    name: str
    createdAt: datetime
    role: str


class GroupResponse(Response):
    """
    Docstring for GroupResponse
    """

    content: Iterable[Group]


class IGroupRepo(IRepository):
    """Docstring for IGroupRepo"""

    @abstractmethod
    def create(self, user_id: int, group_name: str) -> int:
        """
        Docstring for create

        :param self: Description
        :param userID: Description
        :type userID: int
        :param groupName: Description
        :type groupName: str
        :return: Description
        :rtype: int
        """

    @abstractmethod
    def get_all(self, user_id: int) -> Iterator[Group]:
        """
        Docstring for get_all

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Group, ...]
        """

    @abstractmethod
    def update(self, new_name: str, group_id: int):
        """
        Docstring for update

        :param self: Description
        :param newName: Description
        :type newName: str
        :param groupID: Description
        :type groupID: int
        """

    @abstractmethod
    def delete(self, group_id: int):
        """
        Docstring for delete

        :param self: Description
        :param groupID: Description
        :type groupID: int
        """

    @abstractmethod
    def add_member(self, member_id: int, group_id: int, role: str):
        """
        Docstring for add_members

        :param self: Description
        :param memberID: Description
        :type memberID: int
        :param groupID: Description
        :type groupID: int
        :param role: Description
        :type role: str
        """
