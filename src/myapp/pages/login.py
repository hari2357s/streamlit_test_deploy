"""
Docstring for myapp.Pages.login
"""

import time

import streamlit as st

from src.myapp.common.constants import (
    HTTP_INTERNAL_SERVER_ERROR,
    HTTP_OK,
)
from src.myapp.common.state_manager import StateManager as sm
from src.myapp.common.ui_components import my_text, toast_success, toast_warning


class Login:
    """
    Docstring for Login
    """

    def login(self, uname, upass):
        """
        Docstring for login

        :param self: Description
        :param uname: Description
        :param upass: Description
        """
        res = sm.get_container().user_service.login(uname, upass)
        if res.status == HTTP_OK:
            sm.set_authenticated(True)
            sm.set_user(res.content[0])
        else:
            if res.status != HTTP_INTERNAL_SERVER_ERROR:
                toast_warning(res.msg)
            else:
                toast_warning("Something is not right!")
            return False
        return True

    def __init__(self):
        """
        Docstring for __init__

        :param self: Description
        """
        my_text("Welcome to Talksy", size="h1", alignment="center")

        with st.container(horizontal_alignment="center", border=True):
            st.markdown("#### Login Page")
            with st.form("login", border=False):
                uname = st.text_input("User Name*", placeholder="User Name").strip()
                upass = st.text_input(
                    "Password*", placeholder="Password", type="password"
                ).strip()
                login_btn = st.form_submit_button(
                    "Login", use_container_width=True, type="primary"
                )
                if login_btn and self.login(uname, upass):
                    toast_success("Verified!")
                    with st.status("Connecting to your account", width="stretch"):
                        time.sleep(1)
                    st.rerun()
            st.page_link("src/myapp/pages/new_account.py", label="Create New Account")


def main():
    """
    Docstring for main
    """
    Login()


if __name__ == "__main__":
    main()
