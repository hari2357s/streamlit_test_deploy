"""
Docstring for myapp.Modules.message.message_service

It has all the services related to message
"""

from myapp.common.constants import HTTP, ChatType

from .message_repo import IMessageRepo, MessageResponse


class MessageServices:
    """
    Docstring for MessageServices
    """

    def __init__(self, msg_repo: IMessageRepo) -> None:
        self.__msg_repo = msg_repo

    def add_message(
        self, msg: str, user_id: int, chat_id: int, chat_type: ChatType
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
        if chat_type == ChatType.DM:
            self.__msg_repo.add_msg(msg, user_id, chat_id, None, chat_type)
            return MessageResponse(HTTP.OK, "Successfully added DM message", [])
        elif chat_type == ChatType.GROUP:
            self.__msg_repo.add_msg(msg, user_id, None, chat_id, chat_type)
            return MessageResponse(HTTP.OK, "Successfully added Group message", [])

        return MessageResponse(HTTP.INTERNAL_SERVER_ERROR, "invalid option", [])

    def get_all_message(
        self, uid: int, chat_id: int | None, chat_type: ChatType
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
        if chat_type == ChatType.DM:
            result = self.__msg_repo.get_all_msg(uid, chat_id, None)
        elif chat_type == ChatType.GROUP:
            result = self.__msg_repo.get_all_msg(uid, None, chat_id)

        if result:
            return MessageResponse(HTTP.OK, "Successfully got all msgs", result)

        return MessageResponse(HTTP.INTERNAL_SERVER_ERROR, "Invalid option", [])

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
            return MessageResponse(HTTP.INTERNAL_SERVER_ERROR, str(exc.args), [])
        return MessageResponse(HTTP.OK, "Message deleted successfully", [])

    def update_msg(self, updated_msg: str, msg_id: int):
        """
        Docstring for update_msg

        :param self: Description
        :param updated_msg: Description
        :type updated_msg: str
        :param msg_id: Description
        :type msg_id: int
        """
        try:
            self.__msg_repo.update_msg(updated_msg, msg_id)
        except Exception as exc:
            return MessageResponse(HTTP.INTERNAL_SERVER_ERROR, str(exc.args), [])
        return MessageResponse(HTTP.OK, "Message updated successfully", [])
