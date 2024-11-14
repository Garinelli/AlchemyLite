import pytest

def test_create(sync_crud):
    sync_crud.delete_all_tables()
    sync_crud.create_all_tables()
    sync_crud.create(name='test', email='<EMAIL>')

    result = (sync_crud.read_all())[0]
    assert result['id'] == 1
    assert result['name'] == 'test'
    assert result['email'] == '<EMAIL>'


def test_create_with_incorrect_params(sync_crud):
    with pytest.raises(ValueError, match='Parameter password is not a valid column name'):
        sync_crud.create(name='test', email='<EMAIL>', password='<PASSWORD>')