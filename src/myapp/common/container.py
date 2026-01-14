"""Docstring for container"""

from src.myapp.common.database import IDatabase

from src.myapp.modules.chat import ChatRepository, ChatServices
from src.myapp.modules.group import GroupRepository, GroupServices
from src.myapp.modules.message import MessageRepository, MessageServices
from src.myapp.modules.user import UserRepository, UserServices


class Container:
    """
    Docstring for Container
    """

    def __init__(self, db: IDatabase) -> None:
        chat_repo = ChatRepository(db)
        grp_repo = GroupRepository(db)
        msg_repo = MessageRepository(db)
        user_repo = UserRepository(db)

        self.user_service = UserServices(user_repo)
        self.group_service = GroupServices(grp_repo)
        self.chat_service = ChatServices(chat_repo)
        self.msg_service = MessageServices(msg_repo)

    def __str__(self) -> str:
        return "pass"
