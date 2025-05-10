import pytest

from alchemylite import Table
from alchemylite.sync import SyncCrudOperation, SyncPostgresConfig

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
        db_pass="qwertyQ",
        db_name="postgres",
    )

    return config


@pytest.fixture
def sync_crud(session) -> SyncCrudOperation:
    crud = SyncCrudOperation(session, user, user.base)
    return crud
