from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class SyncConfig:
    def __init__(self, db_host: str, db_port: str, db_user: str, db_pass: str,
                 db_name: str) -> None:
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+psycopg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    def get_sync_session(self) -> sessionmaker:
        sync_engine = create_engine(
            url=self.DATABASE_URL,
            echo=False
        )
        session = sessionmaker(sync_engine)
        return session


class AsyncConfig:
    def __init__(self, db_host: str, db_port: str, db_user: str, db_pass: str,
                 db_name: str) -> None:
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    def get_async_session(self) -> async_sessionmaker:
        async_engine = create_async_engine(
            url=self.DATABASE_URL,
        )
        async_session = async_sessionmaker(async_engine)
        return async_session