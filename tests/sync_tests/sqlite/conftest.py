from pathlib import Path

import pytest

from alchemylite import Table
from alchemylite.sync import SyncCrud, SyncSqliteConfig

DB_PATH = (Path(__file__).parent) / 'database.db'


model = Table(
    table_name='users',
    fields={
        "name": {"type": str, "max_len": 128},
        "age": {"type": int},
        "info": {"type": "text", "null": True}
    }
).model


@pytest.fixture(scope="module")
def session() -> SyncSqliteConfig:
    config = SyncSqliteConfig(db_path=DB_PATH)
    return config


@pytest.fixture(scope="module")
def sync_crud(session) -> SyncCrud:
    crud = SyncCrud(session, model, model.base)
    return crud
