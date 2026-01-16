import os
import sqlite3
import contextlib
from collections.abc import Iterator

from .database import IDatabase

class Test_Database(IDatabase):
    def __init__(self, db_path=None):
        """
        Initializes a test database.

        :param db_path: Path to the SQLite database file.
                        If None, defaults to a writable location in Streamlit Cloud.
        """
        # Default path: writable temp folder in Streamlit Cloud
        if db_path is None:
            db_dir = os.path.join("/tmp", "data")  # /tmp is writable in Streamlit Cloud
            os.makedirs(db_dir, exist_ok=True)
            db_path = os.path.join(db_dir, "test.db")
        else:
            # Ensure the folder exists if a custom path is provided
            os.makedirs(os.path.dirname(db_path), exist_ok=True)

        self._db_path = db_path
        self._conn = sqlite3.connect(db_path, check_same_thread=False)

    def cursor(self):
        return self._conn.cursor()

    def commit(self):
        return self._conn.commit()

    def rollback(self):
        return self._conn.rollback()

    @contextlib.contextmanager
    def transaction(self) -> Iterator[sqlite3.Cursor]:
        """
        Context manager for SQLite transactions.

        Usage:
            with db.transaction() as cursor:
                cursor.execute(...)
        """
        cursor = self.cursor()
        try:
            yield cursor
            self.commit()
        except Exception:
            self.rollback()
            raise
        finally:
            cursor.close()
