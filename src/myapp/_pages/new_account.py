"""
Docstring for myapp.Pages.new_account
"""

import streamlit as st

from myapp.common.constants import (
    HTTP_INTERNAL_SERVER_ERROR,
    HTTP_OK,
)
from myapp.common.state_manager import StateManager as sm
from myapp.common.ui_components import my_text, success, toast_warning


class NewAccountPage:
    """
    DocString for NewAccountPage
    """

    @st.dialog("Kindly Login with Userid and Password")
    def redirect(self):
        """
        Docstring for redirect

        :param self: Description
        """
        if st.button("Okayy"):
            st.switch_page("_pages/login.py")

    def __init__(self):
        """
        Docstring for __init__

        :param self: Description
        """
        my_text("Welcome to Talksy", size="h1", alignment="center")

        with st.container(horizontal_alignment="center", border=True):
            st.markdown("#### Create New Account")
            with st.form(key="form", border=False):
                uname = st.text_input("User Name*", placeholder="User Name").strip()
                upass = st.text_input(
                    "Password*", type="password", placeholder="Password"
                ).strip()
                ucpass = st.text_input(
                    "Confirm Password*", type="password", placeholder="Password"
                ).strip()
                submit_btn = st.form_submit_button(
                    "Create New Account", type="primary", use_container_width=True
                )

                if submit_btn:
                    res = sm.get_container().user_service.create_account(
                        uname, upass, ucpass
                    )
                    if res.status == HTTP_OK:
                        success("Account created successfully")
                        st.balloons()
                        self.redirect()
                    elif res.status != HTTP_INTERNAL_SERVER_ERROR:
                        toast_warning(res.msg)
                    else:
                        toast_warning("Something went wrong!")

            st.page_link("_pages/login.py", label="Already have an Account")


def main():
    """
    Docstring for main
    """
    NewAccountPage()


if __name__ == "__main__":
    main()
