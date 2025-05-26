import pytest
from alchemylite.sync import SyncCrud


@pytest.mark.order(10)
def test_delete_by_id(sync_crud: SyncCrud) -> None:
    sync_crud.delete_by_id(id=1)
    result = sync_crud.read_by_id(id=1)
    assert len(result) == 0


@pytest.mark.order(11)
def test_delete_by_id_with_exception(sync_crud: SyncCrud):
    with pytest.raises(ValueError, match='Parameter "id" must be an integer'):
        sync_crud.update_by_id(id='id', age=18, info='Info about AlchemyLite')


@pytest.mark.order(12)
def test_delete_by_id_with_id_missing(sync_crud: SyncCrud):
    with pytest.raises(ValueError, match='Parameter "id" is missing'):
        sync_crud.delete_by_id(age=18, info='The best library...')
