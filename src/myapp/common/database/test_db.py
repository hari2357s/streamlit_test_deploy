import os
import sqlite3
import contextlib
from collections.abc import Iterator
from .database import IDatabase

class Test_Database(IDatabase):
    def __init__(self, db_path = None):
        """
        Initializes a test database.

        If db_path is None or not writable, defaults to Streamlit Cloud's /tmp folder.
        """
        # Use a default writable folder in Streamlit Cloud
        if db_path is None:
            db_dir = os.path.join("/tmp", "data")  # always writable
            os.makedirs(db_dir, exist_ok=True)
            db_path = os.path.join(db_dir, "test.db")
        else:
            # Ensure folder exists if custom path is provided
            folder = os.path.dirname(db_path)
            if folder:
                os.makedirs(folder, exist_ok=True)

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
        cursor = self.cursor()
        try:
            yield cursor
            self.commit()
        except Exception:
            self.rollback()
            raise
        finally:
            cursor.close()
