from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from AlchemyLite import SyncConfig, SyncCrudOperation

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


config = SyncConfig(
    db_host="localhost",
    db_port="5432",
    db_user="postgres",
    db_pass="qwertyQ",
    db_name="AlchemyLite"
)
sync_crud = SyncCrudOperation(config.get_session(), User)

sync_crud.create({"name": "test", "email": "<EMAIL>"})
sync_crud.delete_by_id({'id': 1})