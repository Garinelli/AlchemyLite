import pytest

from alchemylite import Table
from alchemylite.sync import SyncCrud, SyncMySqlConfig

user = Table(
    table_name='users',
    fields={
        "name": {"type": "text"},
        "email": {"type": "text"}
    }
).model


@pytest.fixture(scope='module')
def session() -> SyncMySqlConfig:
    config = SyncMySqlConfig(
        db_host='localhost',
        db_port='3306',
        db_user='root',
        db_pass='password',
        db_name='test'
    )

    return config


@pytest.fixture
def sync_crud(session) -> SyncCrud:
    crud = SyncCrud(session, user, user.base)
    return crud
