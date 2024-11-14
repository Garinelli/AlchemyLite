from alchemylite.sync import SyncCrudOperation, SyncConfig
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

config = SyncConfig(
    db_host="localhost",
    db_port="5432",
    db_user="postgres",
    db_pass="qwertyQ",
    db_name="AlchemyLite"
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


crud = SyncCrudOperation(
    config.session, User
)

crud.create_all_tables()
crud.create(name="User", email="email@mail.ru")
crud.read_all()
crud.limited_read(limit=5, offset=0)
crud.read_by_id(id=1)
crud.update_by_id(id=1, name="new value", email="new_emal")
crud.delete_by_id(id=1)
crud.delete_all_tables()