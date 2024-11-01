from typing import Any
from sqlalchemy import select, update, delete
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.asyncio import async_sessionmaker

class AsyncCrudOperation:
    def __init__(self, async_session_factory: async_sessionmaker, model, base):
        self.async_session_factory = async_session_factory
        self.model = model
        self.base = base

    def validate_params(self, params: dict[str, Any]) -> bool:
        model_columns = {column.name: column.type for column in inspect(self.model).columns}
        for key, value in params.items():
            if key not in model_columns:
                raise ValueError(f'Parameter {key} is not a valid column name')
        return True

    async def create(self, params: dict[str, Any]) -> None:
        async with self.async_session_factory() as session:
            model = self.model(**params)
            session.add(model)
            await session.commit()
