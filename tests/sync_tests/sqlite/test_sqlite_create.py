import pytest 
from alchemylite.sync import SyncCrud


@pytest.mark.order(1)
def test_create(sync_crud: SyncCrud) -> None:
    sync_crud.delete_table()
    sync_crud.create_table()

    sync_crud.create(name='AlchemyLite', age=18, info='Python library')

    result = (sync_crud.read_all())[0]

    assert result['id'] == 1
    assert result['age'] == 18
    assert result['info'] == 'Python library'


@pytest.mark.order(2)
def test_create_with_incorrect_params(sync_crud: SyncCrud):
    with pytest.raises(ValueError, match='Parameter stars is not a valid column name'):
        sync_crud.create(name='AlchemyLite', age=18, stars=1337)
