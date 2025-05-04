import pytest


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
