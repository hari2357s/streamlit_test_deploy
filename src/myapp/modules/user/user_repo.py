"""
Docstring for myapp.Modules.user.user_repo
"""

from abc import abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime
from hashlib import sha512
from typing import NamedTuple

from src.myapp.common.repository import IRepository
from src.myapp.common.response import Response


class User(NamedTuple):
    """
    Docstring for User
    """

    userID: int
    userName: str
    lastseen: datetime


@dataclass
class UserResponse(Response):
    """
    Docstring for UserResponse
    """

    content: Sequence[User]


class IUserRepo(IRepository):
    """
    Docstring for IUserRepo
    """

    def sha512(self, text: str) -> str:
        """
        Docstring for sha512

        :param self: Description
        :param text: Description
        :type text: str
        :return: Description
        :rtype: str
        """
        sha512_hasher = sha512()
        sha512_hasher.update(text.encode("utf-8"))
        return sha512_hasher.hexdigest()

    @abstractmethod
    def add(self, uname: str, upass: str):
        """
        Docstring for add

        :param self: Description
        :param uname: Description
        :type uname: str
        :param upass: Description
        :type upass: str
        """

    @abstractmethod
    def get(self, uname: str, upass: str) -> User | None:
        """
        Docstring for get_userbyname

        :param self: Description
        :param uname: Description
        :type uname: str
        :param upass: Description
        :type upass: str
        :return: Description
        :rtype: User | None
        """

    @abstractmethod
    def update(self, uid: int, new_name: str):
        """
        Docstring for update

        :param self: Description
        :param uid: Description
        :type uid: int
        :param newName: Description
        :type newName: str
        """

    @abstractmethod
    def delete(self, uid: int):
        """
        Docstring for delete

        :param self: Description
        :param uid: Description
        :type uid: int
        """
