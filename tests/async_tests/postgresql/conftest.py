import pytest

from alchemylite import Table
from alchemylite.async_ import AsyncCrudOperation, AsyncPostgresConfig

user = Table(
    table_name="users",
    fields={
        "name": {"type": "text"},
        "email": {"type": "text"}
    }
).model

@pytest.fixture(scope='module')
def session() -> AsyncPostgresConfig:
    config = AsyncPostgresConfig(
        db_host="localhost",
        db_port="5432",
        db_user="postgres",
        db_pass="qwertyQ",
        db_name="AlchemyLite",
    )
    return config


@pytest.fixture
def async_crud(session) -> AsyncCrudOperation:
    crud = AsyncCrudOperation(session, user, user.base)
    return crud