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


def test_create(sync_crud):
    sync_crud.delete_all_tables()
    sync_crud.create_all_tables()
    sync_crud.create(name='test', email='<EMAIL>')

    result = (sync_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'


def test_create_with_incorrect_params(sync_crud):
    with pytest.raises(ValueError, match='Parameter password is not a valid column name'):
        sync_crud.create(name='test', email='<EMAIL>', password='<PASSWORD>')