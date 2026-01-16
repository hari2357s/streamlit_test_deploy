import contextlib
import sqlite3
from collections.abc import Iterator

from .database import IDatabase


class Test_Database(IDatabase):
    def __init__(self, db_path="test.db"):
        self._db_path = db_path
        self._conn = sqlite3.connect(db_path)

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
