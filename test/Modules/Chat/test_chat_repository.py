import sqlite3
import pytest
from ....src.myapp.common.database.sqlite_db import SqliteDatabase
from ....src.myapp.modules.chat.chat_repository import ChatRepository

@pytest.fixture
def chat_repository():
    db = SqliteDatabase(":memory:")
    return ChatRepository(db)

def test_add(chat_repository : ChatRepository):
    chat_repository.add(1,2)
    ...