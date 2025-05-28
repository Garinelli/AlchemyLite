import pytest

from sqlalchemy import Integer, String
from sqlalchemy.inspection import inspect

from alchemylite import Table

@pytest.fixture
def model():
    user = Table(
        table_name='user',
        fields=
        {
            "name": {"type": str, "max_len": 255},
            "age": {"type": int},
            "email": {"type": str, "unique": True, "index": True},
            "is_admin": {"type": bool, "default": False},
            "balance": {"type": float},
            "joined_date": {"type": "datetime"},
            "about_me": {"type": "text", "null": True},
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
        model = Table(
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


def test_correct_create_boolean(metadatas):
    boolean_column = metadatas.columns.get("is_admin")
    boolean_column = boolean_column.type
    assert str(boolean_column) == "BOOLEAN"


def test_correct_create_float(metadatas):
    float_column = metadatas.columns.get("balance")
    float_column = float_column.type
    assert str(float_column) == "FLOAT"


def test_correct_create_datetime(metadatas):
    datetime_column = metadatas.columns.get("joined_date")
    datetime_column = datetime_column.type
    assert str(datetime_column) == "DATETIME"


def test_correct_create_text(metadatas):
    text_column = metadatas.columns.get("about_me")
    text_column = text_column.type
    assert str(text_column) == "TEXT"


def test_correct_create_null(metadatas):
    null_column = metadatas.columns['about_me'].nullable
    assert null_column is True


def test_correct_create_default_value(metadatas):
    column_with_default_value = metadatas.columns['is_admin'].default
    assert column_with_default_value.arg is False


def test_correct_create_unique(metadatas):
    unique_column = metadatas.columns['email'].unique
    assert unique_column is True


def test_correct_create_index(metadatas):
    index_column = metadatas.columns['email'].index
    assert index_column is True
