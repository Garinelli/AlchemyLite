"""
Configuration for async session
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from alchemylite import BaseConfig
from alchemylite.exceptions import IncorrectDbmsName

class AsyncConfig(BaseConfig):
    """
    Class for configuring async sessions
    """

    DB_URLS = {
        'postgresql': 'postgresql+asyncpg://{}:{}@{}:{}/{}',
        'mysql': 'mysql+aiomysql://{}:{}@{}:{}/{}'
    }

    @property
    def DATABASE_URL(self) -> str:
        db_type = (self.DB_URLS).get((self.db_type).lower())
        if db_type is None:
            raise IncorrectDbmsName
        return db_type.format(self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)

    @property
    def session(self):
        async_engine = create_async_engine(
            url=self.DATABASE_URL,
        )
        async_session = async_sessionmaker(
            async_engine,
            expire_on_commit=False,
        )
        return async_session
