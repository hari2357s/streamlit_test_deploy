from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from aiosqlite import Cursor


class IAsyncDatabase(ABC):
    @abstractmethod
    async def cursor(self) -> Cursor: ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    def transaction(self) -> AbstractAsyncContextManager[Cursor]: ...
