"""
Docstring for myapp.Common.constants
"""

from enum import Enum, IntEnum

MIN_USERNAME_LENGTH = 6
MIN_PASSWORD_LENGTH = 8


class HTTP(IntEnum):
    OK = 200
    FILE_NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    BAD_REQUEST = 400


class GroupRole(Enum):
    MEMEBR = "MEMBER"
    ADMIN = "ADMIN"


class ChatType(Enum):
    DM = "DM"
    GROUP = "GROUP"
