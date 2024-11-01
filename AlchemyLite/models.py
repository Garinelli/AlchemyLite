from typing import Any, Dict, Type
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class ModelFactory:
    TYPES = {
        int: Integer,
        str: String,
    }

    def __init__(self, name: str, fields: Dict[str, Type[Any]]):
        self.name = name
        self.fields = fields

    def create_model(self):

        attrs = {
            '__tablename__': self.name,
            'id': mapped_column(Integer, primary_key=True),
        }


        for field_name, field_type in self.fields.items():
            column_type = self.TYPES.get(field_type)
            if column_type:
                attrs[field_name] = mapped_column(column_type)
            else:
                raise ValueError(f"Тип {field_type} не поддерживается")


        model = type(self.name, (Base,), attrs)
        return model

