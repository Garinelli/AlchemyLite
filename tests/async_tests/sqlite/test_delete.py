import pytest

@pytest.mark.asyncio
@pytest.mark.order(10)
async def test_delete_by_id(async_crud):
    await async_crud.delete_by_id(id=1)
    result = await async_crud.read_by_id(id=1)
    assert len(result) == 0


@pytest.mark.asyncio
@pytest.mark.order(11)
async def test_delete_by_id_with_exception(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        await async_crud.update_by_id(id='id', age=21, info='new info')


@pytest.mark.asyncio
@pytest.mark.order(12)
async def test_delete_by_id_with_id_missing(async_crud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        await async_crud.delete_by_id(name='new_test', age=18)
