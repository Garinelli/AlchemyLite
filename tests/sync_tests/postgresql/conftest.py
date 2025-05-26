import pytest

from alchemylite import Table
from alchemylite.sync import SyncCrud, SyncPostgresConfig

user = Table(
    table_name="users",
    fields={
        "name": {"type": "text"},
        "email": {"type": "text"}
    }
).model

@pytest.fixture(scope='module')
def session() -> SyncPostgresConfig:
    config = SyncPostgresConfig(
        db_host="localhost",
        db_port="5432",
        db_user="postgres",
        db_pass="postgres",
        db_name="postgres",
    )

    return config


@pytest.fixture
def sync_crud(session) -> SyncCrud:
    crud = SyncCrud(session, user, user.base)
    return crud
