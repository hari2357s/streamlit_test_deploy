import sqlite3
import pytest
from myapp.common.database.sqlite_db import SqliteDatabase
from myapp.modules.user.user_repository import UserRepository

@pytest.fixture
def user_repository():
    db = SqliteDatabase(":memory:")
    return UserRepository(db)


def test_add_user(user_repository):
    user_repository.add("test_user1", "test_user")

    with pytest.raises(ValueError, match="Username already exists"):
        user_repository.add("test_user1", "test_user")

def test_get_user_success(user_repository):
    user_repository.add("user1", "pass1")
    user = user_repository.get_userbyname("user1", "pass1")

    assert user is not None
    assert user.userName == "user1"
    assert isinstance(user.userID, int)

def test_get_user_wrong_password(user_repository):
    user_repository.add("user1", "pass1")
    user = user_repository.get_userbyname("user1", "wrongpass")
    assert user is None

def test_get_user_nonexistent(user_repository):
    user = user_repository.get_userbyname("no_user", "anypass")
    assert user is None

def test_update_username(user_repository):
    user_repository.add("user1", "pass1")
    user = user_repository.get_userbyname("user1", "pass1")

    user_repository.update(user.userID, "new_user1")
    updated_user = user_repository.get_userbyname("new_user1", "pass1")

    assert updated_user is not None
    assert updated_user.userName == "new_user1"

def test_update_username_conflict(user_repository):
    user_repository.add("user1", "pass1")
    user_repository.add("user2", "pass2")
    user1 = user_repository.get_userbyname("user1", "pass1")

    with pytest.raises(sqlite3.IntegrityError):
        user_repository.update(user1.userID, "user2")

def test_delete_user(user_repository):
    user_repository.add("user1", "pass1")
    user = user_repository.get_userbyname("user1", "pass1")

    user_repository.delete(user.userID)
    deleted_user = user_repository.get_userbyname("user1", "pass1")
    assert deleted_user is None


def test_user_defaults(user_repository):
    user_repository.add("user1", "pass1")
    user = user_repository.get_userbyname("user1", "pass1")

    assert hasattr(user, "userID")
    assert hasattr(user, "userName")
    assert hasattr(user, "lastseen")
    # assert user.status == 0
