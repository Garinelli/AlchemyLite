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


def test_update_by_id(sync_crud):
    sync_crud.update_by_id(id=1, name='new_test', email='<EMAIL>')
    result = sync_crud.read_by_id(id=1)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'new_test'
    assert result['email'] == '<EMAIL>'


def test_delete_by_id(sync_crud):
    sync_crud.delete_by_id(id=1)
    result = sync_crud.read_by_id(id=1)
    assert len(result) == 0

def test_update_by_id_with_exception(sync_crud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        sync_crud.update_by_id(id='id', name='new_test', email='<EMAIL>')


def test_delete_by_id_with_exception(sync_crud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        sync_crud.update_by_id(id='id', name='new_test', email='<EMAIL>')

def test_update_by_id_with_id_missing(sync_crud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        sync_crud.update_by_id(name='new_test', email='<EMAIL>')

def test_delete_by_id_with_id_missing(sync_crud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        sync_crud.delete_by_id(name='new_test', email='<EMAIL>')

def test_create_with_incorrect_params(sync_crud):
    with pytest.raises(ValueError, match='Parameter password is not a valid column name'):
        sync_crud.create(name='test', email='<EMAIL>', password='<PASSWORD>')

def test_update_by_id_with_incorrect_params(sync_crud):
    with pytest.raises(ValueError, match='Parameter year is not a valid column name'):
        sync_crud.update_by_id(name='test', email='<EMAIL>', year='year')