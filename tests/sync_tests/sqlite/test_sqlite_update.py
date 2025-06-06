import pytest

from alchemylite.sync import SyncCrud

@pytest.mark.order(6)
def test_update_by_id(sync_crud: SyncCrud):
    sync_crud.update_by_id(id=1, name='alchemylite', info='ALCHEMYLITE')
    result = sync_crud.read_by_id(id=1)
    result = result[0]
    assert result['id'] == 1
    assert result['name'] == 'alchemylite'
    assert result['info'] == 'ALCHEMYLITE'


@pytest.mark.order(7)
def test_update_by_id_with_exception(sync_crud: SyncCrud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        sync_crud.update_by_id(id='id', name='alchemylite', info='AlchemyLite')


@pytest.mark.order(8)
def test_update_by_id_with_id_missing(sync_crud: SyncCrud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        sync_crud.update_by_id(name='alchemylite', info='AlchemyLite')


@pytest.mark.order(9)
def test_update_by_id_with_incorrect_params(sync_crud: SyncCrud):
    with pytest.raises(ValueError, match='Parameter year is not a valid column name'):
        sync_crud.update_by_id(name='test', age=18, year='year')
