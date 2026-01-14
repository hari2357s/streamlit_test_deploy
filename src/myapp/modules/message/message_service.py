"""
Docstring for myapp.Modules.message.message_service

It has all the services related to message
"""

from .message_repo import IMessageRepo, MessageResponse


class MessageServices:
    """
    Docstring for MessageServices
    """

    def __init__(self, msg_repo: IMessageRepo) -> None:
        self.__msg_repo = msg_repo

    def add_message(
        self, msg: str, user_id: int, chat_id: int, chat_type: str
    ) -> MessageResponse:
        """
        Docstring for add_message

        :param self: Description
        :param msg: Description
        :type msg: str
        :param user_id: Description
        :type user_id: int
        :param chat_id: Description
        :type chat_id: int
        :param chat_type: Description
        :type chat_type: str
        :return: Description
        :rtype: MessageResponse
        """
        if chat_type == "DM":
            self.__msg_repo.add_msg(msg, user_id, chat_id, None, chat_type)
        elif chat_type == "GROUP":
            self.__msg_repo.add_msg(msg, user_id, None, chat_id, chat_type)

        return MessageResponse(500, "invalid option", [])

    def get_all_message(
        self, uid: int, chat_id: int | None, chat_type: str
    ) -> MessageResponse:
        """
        Docstring for get_all_message

        :param self: Description
        :param uid: Description
        :type uid: int
        :param chat_id: Description
        :type chat_id: int | None
        :param chat_type: Description
        :type chat_type: str
        :return: Description
        :rtype: MessageResponse
        """
        result = None
        if chat_type == "DM":
            result = self.__msg_repo.get_all_msg(uid, chat_id, None)
        elif chat_type == "GROUP":
            result = self.__msg_repo.get_all_msg(uid, None, chat_id)

        if result:
            return MessageResponse(200, "Successfully got all msgs", result)

        return MessageResponse(500, "invalid option", [])

    def delete_msg(self, msg_id: int) -> MessageResponse:
        """
        Docstring for delete_msg

        :param self: Description
        :param msg_id: Description
        :type msg_id: int
        :return: Description
        :rtype: MessageResponse
        """
        try:
            self.__msg_repo.delete_msg(msg_id)
        except Exception as exc:
            return MessageResponse(500, str(exc.args), [])
        return MessageResponse(200, "Message deleted successfully", [])
