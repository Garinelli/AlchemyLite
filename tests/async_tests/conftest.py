import pytest
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from alchemylite.async_ import AsyncCrudOperation, AsyncConfig


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


@pytest.fixture(scope='module')
def session():
    config = AsyncConfig(
        db_host="localhost",
        db_port="5432",
        db_user="postgres",
        db_pass="qwertyQ",
        db_name="AlchemyLite"
    )
    return config


@pytest.fixture
def async_crud(session):
    crud = AsyncCrudOperation(session, User, Base)
    return crud