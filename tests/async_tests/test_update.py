import pytest


@pytest.mark.asyncio
async def test_update_by_id(async_crud):
    await async_crud.update_by_id(id=1, name='new_test', email='<EMAIL>')
    result = await async_crud.read_by_id(id=1)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'new_test'
    assert result['email'] == '<EMAIL>'


@pytest.mark.asyncio
async def test_update_by_id_with_exception(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        await async_crud.update_by_id(id='id', name='new_test', email='<EMAIL>')


@pytest.mark.asyncio
async def test_update_by_id_with_id_missing(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        await async_crud.update_by_id(name='new_test', email='<EMAIL>')


@pytest.mark.asyncio
async def test_update_by_id_with_incorrect_params(async_crud):
    with pytest.raises(ValueError, match='Parameter year is not a valid column name'):
        await async_crud.update_by_id(name='test', email='<EMAIL>', year='year')
