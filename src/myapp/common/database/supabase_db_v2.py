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
        USER = os.getenv("user")
        PASSWORD = os.getenv("password")
        HOST = os.getenv("host")
        PORT = os.getenv("port")
        DBNAME = os.getenv("dbname")
        print(DBNAME)
        try:
            self._conn = psycopg2.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                dbname=DBNAME
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
