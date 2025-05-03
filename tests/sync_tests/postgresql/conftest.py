import pytest
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from alchemylite.sync import SyncCrudOperation, SyncPostgresConfig


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


@pytest.fixture(scope='module')
def session():
    config = SyncPostgresConfig(
        db_host="localhost",
        db_port="5432",
        db_user="postgres",
        db_pass="qwertyQ",
        db_name="postgres",
    )

    return config


@pytest.fixture
def sync_crud(session):
    crud = SyncCrudOperation(session, User, Base)
    return crud
