import pytest


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create(async_crud):
    await async_crud.delete_table()
    await async_crud.create_table()
    await async_crud.create(name='test', email='<EMAIL>')

    result = await (async_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_create_with_incorrect_params(async_crud):
    with pytest.raises(ValueError, match='Parameter password is not a valid column name'):
        await async_crud.create(name='test', email='<EMAIL>', password='<PASSWORD>')
