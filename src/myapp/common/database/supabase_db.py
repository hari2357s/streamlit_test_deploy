import contextlib
from collections.abc import Iterator

import supabase
from streamlit import secrets

from .database import IDatabase


class SupaBaseDatabase(IDatabase):
    """
    Docstring for Sqlite_Database
    """

    SUPABASE_URL = secrets["SUPABASE_URL"]
    SUPABASE_KEY = secrets["SUPABASE_KEY"]

    def __init__(self, db_path="chat_app.db"):
        self._db_path = db_path
        self._supabase = supabase.create_client(
            SupaBaseDatabase.SUPABASE_URL, SupaBaseDatabase.SUPABASE_KEY
        )

    def cursor(self):
        return self._supabase

    @contextlib.contextmanager
    def transaction(self) -> Iterator[supabase.Client]:
        try:
            yield self.cursor()
        except Exception:
            raise
