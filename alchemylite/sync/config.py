"""
Configuration for sync session
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemylite import BaseConfig, BaseSQLiteConfig
from alchemylite.exceptions import SQLiteDbDoesNotExists


class SyncPostgresConfig(BaseConfig):
    """
    Class for configuring PostgreSQL sync sessions
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
        return f'postgresql+psycopg://{self._db_user}:{self._db_pass}@{self._db_host}:{self._db_port}/{self._db_name}'  # noqa: E501

    @property
    def session(self) -> sessionmaker:
        sync_engine = create_engine(
            url=self.DATABASE_URL,
            echo=False
        )
        session_factory = sessionmaker(sync_engine)
        return session_factory


class SyncSqliteConfig(BaseSQLiteConfig):
    """
    Class for configuring SQLite sync sessions
    """
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    @property
    def DATABASE_URL(self) -> str:
        return f'sqlite:///{self._db_path}'

    @property
    def session(self) -> sessionmaker:
        if not os.path.exists(self._db_path):
            raise SQLiteDbDoesNotExists
        sync_engine = create_engine(
            url=self.DATABASE_URL,
            echo=False
        )
        session_factory = sessionmaker(sync_engine)
        return session_factory
