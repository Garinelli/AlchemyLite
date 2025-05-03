from alchemylite.sync import SyncCrudOperation


def test_read_all(sync_crud: SyncCrudOperation) -> None:
    result = (sync_crud.read_all())[0]
    assert result['name'] == 'AlchemyLite'
    assert result['age'] == 18
    assert result['info'] == 'Python library'


def test_read_by_id(sync_crud: SyncCrudOperation) -> None:
    result = sync_crud.read_by_id(id=1)
    result = result[0]
    assert result['name'] == 'AlchemyLite'
    assert result['age'] == 18
    assert result['info'] == 'Python library'


def test_limited_read(sync_crud: SyncCrudOperation) -> None:
    result = sync_crud.limited_read(limit=5, offset=0)
    result = result[0]
    assert result['name'] == 'AlchemyLite'
    assert result['age'] == 18
    assert result['info'] == 'Python library'
