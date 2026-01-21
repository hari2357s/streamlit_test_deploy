"""
Docstring for myapp.Common.state_manager
"""

from typing import NamedTuple

import streamlit as st

from myapp.modules.user import User

from .constants import ChatType
from .container import Container


class CurrentChat(NamedTuple):
    """
    Docstring for CurrentChat
    """

    chatID: int
    chatName: str
    type: ChatType


class StateManager:
    """
    Docstring for StateManager
    """

    @staticmethod
    def set_authenticated(is_auth: bool):
        """
        Docstring for setAuthenticated

        :param is_auth: Description
        :type is_auth: bool
        """
        st.session_state["authenticated"] = is_auth

    @staticmethod
    def get_authenticated() -> bool:
        """
        Docstring for getAuthenticated

        :return: Description
        :rtype: bool
        """
        return st.session_state.get("authenticated", False)

    @staticmethod
    def set_user(user: User):
        """
        Docstring for setUser

        :param user: Description
        :type user: User
        """
        st.session_state["user"] = user

    @staticmethod
    def get_user() -> User | None:
        """
        Docstring for getUser

        :return: Description
        :rtype: User | None
        """
        return st.session_state.get("user", None)

    @staticmethod
    def set_current_chat(curr_chat: CurrentChat | None):
        """
        Docstring for setCurrentChat

        :param currChat: Description
        :type currChat: CurrentChat | None
        """
        st.session_state["currentChat"] = curr_chat

    @staticmethod
    def get_current_chat() -> CurrentChat | None:
        """
        Docstring for getCurrentChat

        :return: Description
        :rtype: CurrentChat | None
        """
        return st.session_state.get("currentChat", None)

    @staticmethod
    def get_container() -> Container:
        """
        Docstring for getContainer

        :return: Description
        :rtype: Container
        """
        return st.session_state.Container
