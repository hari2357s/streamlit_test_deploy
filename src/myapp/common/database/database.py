"""
Docstring for myapp.Common.Database.database
"""

from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Any


class IDatabase(ABC):
    """
    Docstring for IDatabase
    """

    @abstractmethod
    def cursor(self) -> Any:
        """
        Docstring for cursor

        :param self: Description
        :return: Description
        :rtype: Cursor
        """

    @abstractmethod
    def transaction(self) -> AbstractContextManager:
        """
        Docstring for transaction

        :param self: Description
        :return: Description
        :rtype: AbstractContextManager[Any, bool | None]
        """
