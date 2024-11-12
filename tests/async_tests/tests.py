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
    return config.session


@pytest.fixture
def async_crud(session):
    crud = AsyncCrudOperation(session, User, Base)
    return crud

@pytest.mark.asyncio
async def test_create(async_crud):
    await async_crud.delete_all_tables()
    await async_crud.create_all_tables()
    await async_crud.create(name='test', email='<EMAIL>')

    result = (await async_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'

@pytest.mark.asyncio
async def test_read_all(async_crud):
    result = (await async_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'

@pytest.mark.asyncio
async def test_read_by_id(async_crud):
    result = await async_crud.read_by_id(id=1)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'

@pytest.mark.asyncio
async def test_limited_read(async_crud):
    result = await async_crud.limited_read(limit=5, offset=0)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'

@pytest.mark.asyncio
async def test_update_by_id(async_crud):
    await async_crud.update_by_id(id=1, name='new_test', email='<EMAIL>')
    result = await async_crud.read_by_id(id=1)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'new_test'
    assert result['email'] == '<EMAIL>'

@pytest.mark.asyncio
async def test_delete_by_id(async_crud):
    await async_crud.delete_by_id(id=1)
    result = await async_crud.read_by_id(id=1)
    assert len(result) == 0
@pytest.mark.asyncio
async def test_update_by_id_with_exception(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        await async_crud.update_by_id(id='id', name='new_test', email='<EMAIL>')

@pytest.mark.asyncio
async def test_delete_by_id_with_exception(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        await async_crud.update_by_id(id='id', name='new_test', email='<EMAIL>')
@pytest.mark.asyncio
async def test_update_by_id_with_id_missing(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        await async_crud.update_by_id(name='new_test', email='<EMAIL>')
@pytest.mark.asyncio
async def test_delete_by_id_with_id_missing(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        await async_crud.delete_by_id(name='new_test', email='<EMAIL>')
@pytest.mark.asyncio
async def test_create_with_incorrect_params(async_crud):
    with pytest.raises(ValueError, match='Parameter password is not a valid column name'):
        await async_crud.create(name='test', email='<EMAIL>', password='<PASSWORD>')
@pytest.mark.asyncio
async def test_update_by_id_with_incorrect_params(async_crud):
    with pytest.raises(ValueError, match='Parameter year is not a valid column name'):
        await async_crud.update_by_id(name='test', email='<EMAIL>', year='year')