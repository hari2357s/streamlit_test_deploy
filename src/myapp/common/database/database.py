"""
Docstring for myapp.Common.Database.database
"""

from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from sqlite3 import Cursor


class IDatabase(ABC):
    """
    Docstring for IDatabase
    """

    @abstractmethod
    def cursor(self) -> Cursor:
        """
        Docstring for cursor

        :param self: Description
        :return: Description
        :rtype: Cursor
        """

    @abstractmethod
    def commit(self):
        """
        Docstring for commit

        :param self: Description
        """

    @abstractmethod
    def rollback(self):
        """
        Docstring for rollback

        :param self: Description
        """

    @abstractmethod
    def transaction(self) -> AbstractContextManager:
        """
        Docstring for transaction

        :param self: Description
        :return: Description
        :rtype: AbstractContextManager[Any, bool | None]
        """
