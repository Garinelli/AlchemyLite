import pytest 

from alchemylite import Table
from alchemylite.sync import SyncConfig, SyncCrudOperation
from alchemylite.exceptions import IncorrectDbmsName

@pytest.fixture
def model():
    order = Table(
        table_name='orders',
        fields=
        {
            "order_id": {"type": str, "max_len": 128},
            "price": {"type": float},
        }
    )

    order = order.model

    return order

@pytest.fixture
def correct_configuration():
    config = SyncConfig(
        db_host='localhost',
        db_port='5432',
        db_user='postgres',
        db_pass='qwertyQ',
        db_name='postgres',
        db_type='postgresql'
    )
    return config 

@pytest.fixture
def incorrect_configuration():
    config = SyncConfig(
        db_host='localhost',
        db_port='5432',
        db_user='postgres',
        db_pass='qwertyQ',
        db_name='postgres',
        db_type='incorrect_db_type'
    )
    return config 

def test_correct_configuration(correct_configuration, model):
    crud = SyncCrudOperation(
        correct_configuration,
        model,
        model.base
    )
    crud.create_all_tables()

def test_incorrect_configuration(incorrect_configuration, model):
    with pytest.raises(IncorrectDbmsName, match=f"An incorrect DBMS name was specified.\nDocumentation: link"):
        crud = SyncCrudOperation(
            incorrect_configuration,
            model,
            model.base
        )
        crud.create_all_tables()


