from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker
from .config import SyncConfig, AsyncConfig


class SyncCrudOperation:
    def __init__(self, session: sessionmaker, model):
        self.session = session
        self.model = model

