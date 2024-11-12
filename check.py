import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from alchemylite.async_ import AsyncCrudOperation, AsyncConfig

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]

config = AsyncConfig(
    db_host="localhost",
    db_port="5432",
    db_user="postgres",
    db_pass="qwertyQ",
    db_name="AlchemyLite"
)

crud = AsyncCrudOperation(
    config.session, model=User, base=Base
)

async def main():
    await crud.delete_all_tables()
    # await crud.create_all_tables()

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
