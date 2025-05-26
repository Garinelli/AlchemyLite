import pytest
from alchemylite.sync import SyncCrud


@pytest.mark.order(3)
def test_read_all(sync_crud: SyncCrud) -> None:
    result = (sync_crud.read_all())[0]
    assert result['name'] == 'AlchemyLite'
    assert result['age'] == 18
    assert result['info'] == 'Python library'


@pytest.mark.order(4)
def test_read_by_id(sync_crud: SyncCrud) -> None:
    result = sync_crud.read_by_id(id=1)
    result = result[0]
    assert result['name'] == 'AlchemyLite'
    assert result['age'] == 18
    assert result['info'] == 'Python library'


@pytest.mark.order(5)
def test_limited_read(sync_crud: SyncCrud) -> None:
    result = sync_crud.limited_read(limit=5, offset=0)
    result = result[0]
    assert result['name'] == 'AlchemyLite'
    assert result['age'] == 18
    assert result['info'] == 'Python library'
