"""
Docstring for myapp.Modules.chat.chat_service
"""

from myapp.common.constants import HTTP

from .chat_repo import ChatResponse, IChatRepo


class ChatServices:
    """
    Docstring for ChatServices
    """

    def __init__(self, chat_repo: IChatRepo) -> None:
        self.__chat_repo = chat_repo

    def get_all(self, user_id: int) -> ChatResponse:
        """
        Docstring for getAllChats

        :param self: Description
        :param user_id: Description
        :type user_id: int
        :return: Description
        :rtype: ChatResponse
        """
        try:
            data = self.__chat_repo.get_all(user_id)
        except Exception as exc:
            return ChatResponse(HTTP.INTERNAL_SERVER_ERROR, str(exc.args), [])
        return ChatResponse(HTTP.OK, "successfully got all chat", tuple(data))

    def add(self, user_id: int, frnd_id: int) -> ChatResponse:
        """
        Docstring for addChat

        :param self: Description
        :param user_id: Description
        :type user_id: int
        :param frndID: Description
        :type frndID: int
        :return: Description
        :rtype: ChatResponse
        """
        self.__chat_repo.add(user_id, frnd_id)
        return ChatResponse(HTTP.OK, "successfully added", [])

    def get_not_in_chat(self, user_id: int):
        """
        Docstring for getNotInChat

        :param self: Description
        :param user_id: Description
        :type user_id: int
        """
        data = self.__chat_repo.get_not_in_chat(user_id)
        return ChatResponse(HTTP.OK, "successfully got not in chat", data)

    def update_block(
        self, user_id: int, chat_id: int, is_blocked: bool
    ) -> ChatResponse:
        """
        Docstring for updateBlock

        :param self: Description
        :param user_id: Description
        :type user_id: int
        :param chat_id: Description
        :type chat_id: int
        :param isBlocked: Description
        :type isBlocked: bool
        :return: Description
        :rtype: ChatResponse
        """
        blocked = 1 if is_blocked else 0
        self.__chat_repo.update(user_id, chat_id, blocked)
        return ChatResponse(HTTP.OK, "successfully updated block", [])
