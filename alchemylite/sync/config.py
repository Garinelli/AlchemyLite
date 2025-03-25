"""
Configuration for sync session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemylite import BaseConfig
from alchemylite.exceptions import IncorrectDbmsName

class SyncConfig(BaseConfig):
    """
    Class for configuring async sessions
    """

    DB_URLS = {
        'postgresql': 'postgresql+psycopg://{}:{}@{}:{}/{}',
        'mysql': 'mysql+pymysql://{}:{}@{}:{}/{}'
    }

    @property
    def DATABASE_URL(self) -> str:
        db_type = (self.DB_URLS).get((self.db_type).lower())
        if db_type is None:
            raise IncorrectDbmsName
        return db_type.format(self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)

    @property
    def session(self) -> sessionmaker:
        sync_engine = create_engine(
            url=self.DATABASE_URL,
            echo=False
        )
        session_factory = sessionmaker(sync_engine)
        return session_factory
