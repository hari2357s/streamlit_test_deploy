
import contextlib
import supabase
from collections.abc import Iterator

from .database import IDatabase
from streamlit import secrets

class SupaBaseDatabase(IDatabase):
    """
    Docstring for Sqlite_Database
    """    
    # SUPABASE_URL="https://uzklqxaqtfigzorkirqx.supabase.co"
    # SUPABASE_KEY="sb_publishable_EI74d76J5E6rp93Blz3PFw_4QsgZQJR"
    
    SUPABASE_URL = secrets["SUPABASE_URL"]
    SUPABASE_KEY = secrets["SUPABASE_KEY"]

    def __init__(self, db_path="chat_app.db"):
        self._db_path = db_path
        self._supabase = supabase.create_client(SupaBaseDatabase.SUPABASE_URL, SupaBaseDatabase.SUPABASE_KEY)

    def cursor(self):
        return self._supabase

    @contextlib.contextmanager
    def transaction(self) -> Iterator[supabase.Client]:
        try:
            yield self.cursor()
        except Exception:
            raise


