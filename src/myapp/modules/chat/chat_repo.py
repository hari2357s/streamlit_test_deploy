"""
Docstring for myapp.Modules.chat.chat_repo
"""

from abc import abstractmethod
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from typing import Any, NamedTuple

from myapp.common.repository import IRepository
from myapp.common.response import Response


class Chat(NamedTuple):
    """
    Docstring for Chat
    """

    id: int
    userID: int
    userName: str
    chatID: int
    blocked: int


@dataclass
class ChatResponse(Response):
    """
    Docstring for ChatResponse
    """

    content: Sequence[Chat]


class IChatRepo(IRepository):
    """
    Docstring for IChatRepo
    """

    @abstractmethod
    def add(self, user_id: int, frnd_uid: int):
        """
        Docstring for add

        :param self: Description
        :param userID: Description
        :type userID: int
        :param frndUID: Description
        :type frndUID: int
        """

    @abstractmethod
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

    @abstractmethod
    def get_all(self, user_id: int) -> Iterator[Chat]:
        """
        Docstring for get_all

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Chat, ...]
        """

    @abstractmethod
    def delete(self, chat_id: int):
        """
        Docstring for delete

        :param self: Description
        :param chatID: Description
        :type chatID: int
        """

    @abstractmethod
    def get_not_in_chat(self, user_id: int) -> tuple[Any]:
        """
        Docstring for get_not_in_chat

        :param self: Description
        :param userID: Description
        :type userID: int
        :return: Description
        :rtype: Tuple[Any]
        """
