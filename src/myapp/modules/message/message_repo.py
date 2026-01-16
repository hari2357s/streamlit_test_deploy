"""
Docstring for message_repo
"""

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime
from typing import NamedTuple

from myapp.common.repository import IRepository
from myapp.common.response import Response


class Message(NamedTuple):
    """
    Docstring for Message
    """

    id: int
    msg: str
    userID: int
    userName: str
    chat_id: int | None
    group_id: int | None
    sentAt: datetime
    deliveredAt: datetime | None
    seenAt: datetime | None


@dataclass
class MessageResponse(Response):
    """
    Docstring for MessageResponse
    """

    content: Iterable[Message]


class IMessageRepo(IRepository):
    """
    Docstring for IMessageRepo
    """

    @abstractmethod
    def add_msg(
        self,
        msg: str,
        user_id: int,
        chat_id: int | None,
        grp_id: int | None,
        msg_type: str,
    ):
        """
        Docstring for add_msg

        :param self: Description
        :param msg: Description
        :type msg: str
        :param user_id: Description
        :type user_id: int
        :param chat_id: Description
        :type chat_id: int | None
        :param grp_id: Description
        :type grp_id: int | None
        :param msg_type: Description
        :type msg_type: str
        """

    @abstractmethod
    def get_all_msg(
        self, uid: int, chat_id: int | None, group_id: int | None
    ) -> Iterator[Message]:
        """
        Docstring for getAllMsg

        :param self: Description
        :param uid: Description
        :type uid: int
        :param chat_id: Description
        :type chat_id: int | None
        :param group_id: Description
        :type group_id: int | None
        :return: Description
        :rtype: Tuple[Message, ...]
        """

    @abstractmethod
    def delete_msg(self, msg_id: int):
        """
        Docstring for deleteMsg

        :param self: Description
        :param msg_id: Description
        :type msg_id: int
        """
