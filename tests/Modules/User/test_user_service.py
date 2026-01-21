'''
Docstring for myapp.Test.Modules.User.test_user_service
'''

import pytest
from myapp.modules.user.user_repo import UserResponse
from myapp.modules.user.user_service import UserServices
from myapp.modules.user.user_repository_supabase import UserRepositorySupaBase
from myapp.common.database.sqlite_db import SqliteDatabase


# def test_login_empty_fields(user_service):
#     resp = user_service.login("", "")
#     assert resp.status == 400
#     assert resp.msg == "Fill all the mandatory fields!"
#     assert resp.content == []


# def test_login_short_username_or_password(user_service):
#     resp = user_service.login("abc", "12345678")
#     assert resp.status == 404
#     assert resp.msg == "User not found!"

#     resp = user_service.login("validuser", "123")
#     assert resp.status == 404
#     assert resp.msg == "User not found!"


# def test_login_user_not_found(user_service,):
#     resp : UserResponse = user_service.login("validuser", "validpass")

#     assert resp.status == 404
#     assert resp.msg == "User not found"
#     assert resp.content == []


def test_login_success_with_mock(mocker):
    mocker.Mock(spec= UserRepositorySupaBase) 
    # user_service.create_account("validuser", "validpass", "validpass").content

    # resp = user_service.login("validuser", "validpass")

    # assert resp.status == 200
    # assert resp.msg == "Successfully logged in"

# def test_create_account_short_username(user_service):
#     resp = user_service.create_account("abc", "password123", "password123")
#     assert resp.status == 400
#     assert resp.msg == "Username should be minimum of 4 characters long!"


# def test_create_account_short_password(user_service):
#     resp = user_service.create_account("validuser", "short", "short")
#     assert resp.status == 400
#     assert resp.msg == "Password should be minimum of 8 characters long!"


# def test_create_account_password_mismatch(user_service):
#     resp = user_service.create_account("validuser", "password123", "password321")
#     assert resp.status == 400
#     assert resp.msg == "Passwords doesn't match!"


# def test_create_account_success(user_service):
#     resp = user_service.create_account("validuser", "password123", "password123")

#     assert resp.status == 200
#     assert resp.msg == "Account created successfully"
#     assert resp.content == []
