"""
Docstring for myapp.App
"""

import os
import sys

CURRENT_FILE = os.path.abspath(__file__)
SRC_PATH = os.path.dirname(os.path.dirname(CURRENT_FILE))

if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import streamlit as st

from myapp.common.container import Container
from myapp.common.database.sqlite_db import SqliteDatabase
from myapp.common.database.supabase_db import SupaBaseDatabase
from myapp.common.state_manager import StateManager


def main():
    """
    Docstring for main
    """

    if "Container" not in st.session_state:
        # db: SqliteDatabase= SqliteDatabase()
        db: SupaBaseDatabase = SupaBaseDatabase()
        container: Container = Container(db)
        st.session_state.Container = container

    auth_pages = [st.Page("_pages/home.py", title="Talksy")]

    pages = [
        st.Page("_pages/login.py", title="Login"),
        st.Page("_pages/new_account.py", title="New Account"),
    ]

    if StateManager.get_user() is not None and StateManager.get_authenticated():
        pg = st.navigation(auth_pages, position="top")
    else:
        pg = st.navigation(pages, position="top")

    pg.run()

if __name__ == "__main__":
    main()
