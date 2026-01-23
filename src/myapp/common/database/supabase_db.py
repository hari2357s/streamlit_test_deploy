import contextlib
from collections.abc import Iterator

import supabase
import os
from postgrest import exceptions
from .database import IDatabase
from dotenv import load_dotenv

load_dotenv()
class SupaBaseDatabase(IDatabase):
    """
    Docstring for Sqlite_Database
    """
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    def __init__(self, db_path="chat_app.db"):
        self._db_path = db_path
        if SupaBaseDatabase.SUPABASE_KEY is None or SupaBaseDatabase.SUPABASE_URL is None:
            raise ValueError
        self._supabase = supabase.create_client(
            SupaBaseDatabase.SUPABASE_URL, SupaBaseDatabase.SUPABASE_KEY
        )

    def cursor(self):
        return self._supabase

    @contextlib.contextmanager
    def transaction(self) -> Iterator[supabase.Client]:
        try:
            yield self.cursor()
        except exceptions.APIError:
            raise
