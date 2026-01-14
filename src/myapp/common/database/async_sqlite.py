import contextlib
from collections.abc import AsyncIterator

import aiosqlite
from database.async_Database import IAsyncDatabase

db = aiosqlite


class Asqlite_Database(IAsyncDatabase):
    def __init__(self, db_path="myapp/test_aiosqlite.db"):
        self.db_path = db_path
        self.conn: aiosqlite.Connection | None = None

    async def connect(self):
        self.conn = await db.connect(self.db_path)

    async def cursor(self) -> aiosqlite.Cursor:
        if self.conn is None:
            raise aiosqlite.DatabaseError("can't access database connection")
        return await self.conn.cursor()

    async def commit(self):
        if self.conn is None:
            raise aiosqlite.DatabaseError("can't access database connection")
        await self.conn.commit()

    async def rollback(self):
        if self.conn is None:
            raise aiosqlite.DatabaseError("can't access database connection")
        await self.conn.rollback()

    @contextlib.asynccontextmanager
    async def transaction(self) -> AsyncIterator[aiosqlite.Cursor]:
        cursor = await self.cursor()
        try:
            yield cursor
            await self.commit()

        except Exception:
            await self.rollback()
            raise

        finally:
            await cursor.close()
