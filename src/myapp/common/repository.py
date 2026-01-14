"""
Docstring for repository.py
"""

from abc import ABC, abstractmethod


class IRepository(ABC):
    """
    Docstring for IRepository
    """

    @abstractmethod
    def create_table(self):
        """
        Docstring for create_table

        :param self: Description
        """
