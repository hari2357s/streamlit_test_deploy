"""Docstring for container"""

from myapp.common.database import IDatabase
from myapp.modules.chat import ChatRepository, ChatServices
from myapp.modules.chat.chat_repository_supabase import ChatRepositorySupaBase
from myapp.modules.group import GroupRepository, GroupServices
from myapp.modules.group.group_repository_supabase import GroupRepositorySupaBase
from myapp.modules.message import MessageRepository, MessageServices
from myapp.modules.message.message_repository_supabase import MessageRepositorySupaBase
from myapp.modules.user import UserRepository, UserServices
from myapp.modules.user.user_repository_supabase import UserRepositorySupaBase


class Container:
    """
    Docstring for Container
    """

    def __init__(self, db: IDatabase) -> None:
        # chat_repo = ChatRepository(db)
        # grp_repo = GroupRepository(db)
        # msg_repo = MessageRepository(db)
        # user_repo = UserRepository(db)
        
        chat_repo = ChatRepositorySupaBase(db)
        grp_repo = GroupRepositorySupaBase(db)
        msg_repo = MessageRepositorySupaBase(db)
        user_repo = UserRepositorySupaBase(db)

        self.user_service = UserServices(user_repo)
        self.group_service = GroupServices(grp_repo)
        self.chat_service = ChatServices(chat_repo)
        self.msg_service = MessageServices(msg_repo)

    def __str__(self) -> str:
        return "pass"
