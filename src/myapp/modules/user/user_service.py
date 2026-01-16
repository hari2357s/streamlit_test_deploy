"""
Docstring for myapp.Modules.user.user_service
"""

from myapp.common.constants import (
    HTTP_BAD_REQUEST,
    HTTP_FILE_NOT_FOUND,
    HTTP_INTERNAL_SERVER_ERROR,
    HTTP_OK,
    MIN_PASSWORD_LENGTH,
    MIN_USERNAME_LENGTH,
)
from myapp.modules.user import IUserRepo, UserResponse


class UserServices:
    """
    Docstring for UserServices
    """

    def __init__(self, user_repo: IUserRepo) -> None:
        self.__user_repo = user_repo

    def login(self, uname: str, upass: str) -> UserResponse:
        """
        Docstring for login

        :param self: Description
        :param uname: Description
        :type uname: str
        :param upass: Description
        :type upass: str
        :return: Description
        :rtype: UserResponse
        """
        if uname == "" or upass == "":
            return UserResponse(
                HTTP_INTERNAL_SERVER_ERROR, "Fill all the mandatory fields!", []
            )

        if len(uname) < MIN_USERNAME_LENGTH or len(upass) < MIN_PASSWORD_LENGTH:
            return UserResponse(HTTP_FILE_NOT_FOUND, "User not found!", [])

        user = self.__user_repo.get(uname, upass)

        if user is None:
            return UserResponse(HTTP_FILE_NOT_FOUND, "User not found", [])
        return UserResponse(HTTP_OK, "Successfully logged in", [user])

    def create_account(self, uname: str, ucpass: str, upass: str) -> UserResponse:
        """
        Docstring for create_account

        :param self: Description
        :param uname: Description
        :type uname: str
        :param ucpass: Description
        :type ucpass: str
        :param upass: Description
        :type upass: str
        :return: Description
        :rtype: UserResponse
        """
        if len(uname) < MIN_USERNAME_LENGTH:
            return UserResponse(
                HTTP_BAD_REQUEST, "Username should be minimum of 4 characters long!", []
            )
        if len(upass) < MIN_PASSWORD_LENGTH or len(ucpass) < MIN_PASSWORD_LENGTH:
            return UserResponse(
                HTTP_BAD_REQUEST, "Password should be minimum of 8 characters long!", []
            )
        if upass != ucpass:
            return UserResponse(HTTP_BAD_REQUEST, "Passwords doesn't match!", [])

        try:
            self.__user_repo.add(uname, upass)
        except ValueError as exc:
            return UserResponse(HTTP_BAD_REQUEST, str(exc.args[0]), [])
        return UserResponse(HTTP_OK, "Account created successfully", [])

    def delete_account(self, user_id: int) -> UserResponse:
        """
        Docstring for delete_account

        :param self: Description
        :param user_id: Description
        :type uuser_id: int
        """
        self.__user_repo.delete(user_id)
        return UserResponse(HTTP_OK, "Account deleted Succesfully", [])
