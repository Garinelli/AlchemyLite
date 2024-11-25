import pytest
from sqlalchemy import Integer, String
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


def test_correct_create_int(metadatas):
    integer_column = metadatas.columns.get("age")
    assert isinstance(integer_column.type, Integer)

def test_correct_create_str(metadatas):
    string_column = metadatas.columns.get("email")
    assert isinstance(string_column.type, String)

def test_correct_create_string_max_len(metadatas):
    string_with_max_len = metadatas.columns.get("name")
    string_with_max_len = string_with_max_len.type
    assert str(string_with_max_len) == "VARCHAR(255)"