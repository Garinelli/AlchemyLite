from typing import Any, Dict, Type

from sqlalchemy import Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class ModelFactory:
    TYPES = {
        int: Integer,
        str: String,
        bool: Boolean,
        float: Float,
    }

    def __init__(self, name: str, fields: Dict[str, Type[Any]]):
        self.name = name
        self.fields = fields

    @property
    def model(self):

        attrs = {
            '__tablename__': self.name,
            'id': mapped_column(Integer, primary_key=True),
        }

        for field_name, field_params in self.fields.items():
            column_type = field_params.get("type")
            column_type = self.TYPES.get(column_type)
            nullable = field_params.get('null', True)
            default = field_params.get('default', None)
            unique = field_params.get('unique', False)
            index = field_params.get('index', False)
            if column_type:
                attrs[field_name] = mapped_column(column_type,
                                                  nullable=nullable,
                                                  default=default,
                                                  unique=unique,
                                                  index=index)
            else:
                raise ValueError(f"Type {field_params} no supported")

        model = type(self.name, (Base,), attrs)
        return model
