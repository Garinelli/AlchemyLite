from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemylite import BaseConfig


class SyncConfig(BaseConfig):
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+psycopg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def session(self) -> sessionmaker:
        sync_engine = create_engine(
            url=self.DATABASE_URL,
            echo=False
        )
        session_factory = sessionmaker(sync_engine)
        return session_factory
