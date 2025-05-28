import pytest 


@pytest.mark.order(1)
def test_create(sync_crud):
    # sync_crud.delete_table()
    sync_crud.create_table()
    sync_crud.create(name='test', email='<EMAIL>')

    result = (sync_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'

