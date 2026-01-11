"""
Configuration for async session
"""
import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from alchemylite import BaseConfig, BaseSQLiteConfig
from alchemylite.exceptions import SQLiteDbDoesNotExists


class AsyncPostgresConfig(BaseConfig):
    """
    Class for configuring PostgreSQL async sessions
    """

    def __init__(
        self,
        db_host: str,
        db_port: str,
        db_user: str,
        db_pass: str,
        db_name: str
    ) -> None:
        self._db_host = db_host
        self._db_port = db_port
        self._db_user = db_user
        self._db_pass = db_pass
        self._db_name = db_name

    @property
    def DATABASE_URL(self) -> str:
        return f'postgresql+asyncpg://{self._db_user}:{self._db_pass}@{self._db_host}:{self._db_port}/{self._db_name}'  # noqa: E501

    @property
    def session(self) -> async_sessionmaker:
        async_engine = create_async_engine(
            url=self.DATABASE_URL,
        )
        async_session = async_sessionmaker(
            async_engine,
            expire_on_commit=False,
        )
        return async_session


class AsyncSqliteConfig(BaseSQLiteConfig):
    """
    Class for configuring SQLite async sessions
    """

    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    @property
    def DATABASE_URL(self) -> str:
        return f'sqlite+aiosqlite:///{self._db_path}'

    @property
    def session(self) -> async_sessionmaker:
        if not os.path.exists(self._db_path):
            raise SQLiteDbDoesNotExists
        async_engine = create_async_engine(
            url=self.DATABASE_URL,
        )
        async_session = async_sessionmaker(
            async_engine,
            expire_on_commit=False,
        )
        return async_session
