import os
import sqlite3
import contextlib
from collections.abc import Iterator
from .database import IDatabase

class Test_Database(IDatabase):
    def __init__(self, db_path = None):
        """
        Initializes the test database.

        - Uses /tmp/data/test.db in Streamlit Cloud (writable)
        - Falls back to ./data/test.db locally
        """
        # Detect if running in Streamlit Cloud
        running_on_cloud = os.environ.get("STREAMLIT_SERVER_PORT") is not None

        if db_path is None:
            if running_on_cloud:
                db_dir = os.path.join("/tmp", "data")
            else:
                db_dir = os.path.join(os.getcwd(), "data")
            os.makedirs(db_dir, exist_ok=True)
            db_path = os.path.join(db_dir, "test.db")
        else:
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
