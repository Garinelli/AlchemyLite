import pytest
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from alchemylite.sync import SyncCrudOperation, SyncConfig


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


@pytest.fixture(scope='module')
def session():
    config = SyncConfig(
        db_host="localhost",
        db_port="5432",
        db_user="postgres",
        db_pass="qwertyQ",
        db_name="AlchemyLite"
    )
    return config.session


@pytest.fixture
def sync_crud(session):
    crud = SyncCrudOperation(session, User, Base)
    return crud

def test_read_all(sync_crud):
    result = (sync_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'


def test_read_by_id(sync_crud):
    result = sync_crud.read_by_id(id=1)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'


def test_limited_read(sync_crud):
    result = sync_crud.limited_read(limit=5, offset=0)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'