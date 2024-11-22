import pytest
from sqlalchemy.inspection import inspect

from alchemylite import Model


@pytest.fixture
def model():
    user = Model(
        table_name='user',
        fields=
        {
            "name": {"type": str, "max_len": 255},
            "age": {"type": int},
            "email": {"type": str, "unique": True},
        }
    )

    user = user.model

    return user


@pytest.fixture
def metadatas(model):
    mapper = inspect(model)
    return mapper


def test_correct_model_attrs(metadatas):
    name = metadatas.columns.get('name')
    name_type = str(name.type)
    age = metadatas.columns.get('age')
    age_type = str(age.type)
    email = metadatas.columns.get('email')
    email_type = str(email.type)
    email_unique = email.unique

    assert name_type == "VARCHAR(255)"
    assert age_type == "INTEGER"
    assert email_type == 'VARCHAR'
    assert email_unique == True


def test_correct_table_name(model):
    table_name = model.__tablename__
    assert table_name == 'user'


def test_primary_key(metadatas):
    id_column = metadatas.columns.get("id")
    assert id_column.primary_key is True

def test_unsupported_type():
    with pytest.raises(ValueError, match=f"Unsupported field type: {list}"):
        model = Model(
            table_name="user",
            fields={"unsupported_field": {"type": list}}
        )
        model = model.model