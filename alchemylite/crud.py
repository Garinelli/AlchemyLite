from abc import ABC, abstractmethod
from typing import Any, Union

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker


class AbstractOperations(ABC):
    def __init__(self, session_factory: Union[sessionmaker, async_sessionmaker], model):
        self.session_factory = session_factory
        self.model = model

    @abstractmethod
    def validate_params(self, params: dict[str, Any]) -> bool:
        pass


class SyncCrudOperation:
    def __init__(self, session_factory: sessionmaker, model):
        self.session_factory = session_factory
        self.model = model

    def validate_params(self, params: dict[str, Any]) -> bool:
        model_columns = {column.name: column.type for column in inspect(self.model).columns}
        for key, value in params.items():
            if key not in model_columns:
                raise ValueError(f'Parameter {key} is not a valid column name')
        return True

    def create(self, params: dict[str, Any]) -> None:
        self.validate_params(params)
        with self.session_factory() as session:
            model = self.model(**params)
            session.add(model)
            session.commit()

    def read(self) -> tuple:
        with self.session_factory() as session:
            query = select(self.model)
            result = (session.execute(query)).all()
            return result
            # model_columns = {column.name: column.type for column in inspect(self.model).columns}
            # result_dict = {}

    def update_by_id(self, condition: dict[str, int], params: dict[str, int]) -> None:
        self.validate_params(params)
        if 'id' not in condition:
            raise ValueError(f'Parameter "id" is missing')
        id = condition['id']
        if type(id) is not int:
            raise ValueError(f'Parameter "id" must be an integer')

        with self.session_factory() as session:
            stmt = update(self.model).where(self.model.id == id).values(params)
            session.execute(stmt)
            session.commit()

    def delete_by_id(self, condition: dict[str, int]) -> None:
        if 'id' not in condition:
            raise ValueError(f'Parameter "id" is missing')
        id = condition['id']
        if type(id) is not int:
            raise ValueError(f'Parameter "id" must be an integer')

        with self.session_factory() as session:
            stmt = delete(self.model).where(self.model.id == id)
            session.execute(stmt)
            session.commit()

