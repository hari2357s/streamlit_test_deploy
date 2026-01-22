"""
Docstring for myapp.Common.Database.sqlite_db
"""

import contextlib
import os
import psycopg2
from dotenv import load_dotenv
from collections.abc import Iterator

from .database import IDatabase

load_dotenv()

class SupaBaseDatabase_V2(IDatabase):
    """
    Docstring for Sqlite_Database
    """

    def __init__(self):
        # USER = os.getenv("DB_USER")
        # PASSWORD = os.getenv("DB_PASSWORD")
        # HOST = os.getenv("DB_HOST")
        # PORT = os.getenv("DB_PORT")
        DB_URL = os.getenv("DB_URL")
        try:
            self._conn = psycopg2.connect(
                DB_URL,
            )
        except Exception as exc:
            raise ConnectionError("Database connection failed") from exc

    def cursor(self):
        try:
            return self._conn.cursor()
        except Exception as exc:
            raise ConnectionError("Database Cursor failed") from exc
        
    def commit(self):
        return self._conn.commit()

    def rollback(self):
        return self._conn.rollback()

    @contextlib.contextmanager
    def transaction(self):
        cursor = self.cursor()
        try:
            yield cursor
            self.commit()

        except Exception:
            self.rollback()
            raise

        finally:
            cursor.close()
