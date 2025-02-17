sync CRUD operations
====================

The library supports both synchronous and asynchronous database queries. This section will show you how to work with the synchronous option.

First, you need to create a config to make queries.

.. code-block:: python

 from alchemylite.sync import SyncConfig

 config = SyncConfig(
     db_host="your_host",
     db_port="your_port",
     db_user="your_user",
     db_pass="your_password",
     db_name="your_db_name"
 )

When creating the config, five parameters are passed: host, port, user, password, name of DB

Next, you need to create an instance of the class that will represent the methods for CRUD operations.

.. code-block:: python

 from alchemylite.sync import SyncCrudOperation

 crud = SyncCrudOperation(
     config,
     YourModel,
     base
 )

The class constructor accepts three parameters:

1. The instance of the Sync Config class that you created
2. Your DB model
3. Base class of your model. It is not required.It is necessary if you want to use the create_all_tables or delete_all_tables methods.

This completes the setup! Now we can use CRUD operations

List of supported methods of the SyncCrudOperation class:

1. create_all_tables - Creates a table in the database that you specified
2. create(param_1, param_2, param_n) - Creates an entry in the database. A real example will be shown below
3. read_all - Calculates all the data from the table
4. limited_read(limit=value, offset=value) - Reads a certain amount of data. Default values: limit = 50, offset = 0
5. read_by_id(id=value) - Reads all data from a table by id
6. update_by_id(id=value, update_param=value) - Update data by id
7. delete_by_id(id=value) - Delete data by id
8. delete_all_tables - Deletes a table in the database that you specified

Examples of use

.. code-block:: python

 from alchemylite.sync import SyncCrudOperation, SyncConfig
 from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


 config = SyncConfig(
     db_host="localhost",
     db_port="5432",
     db_user="postgres",
     db_pass="postgres",
     db_name="alchemylite"
 )


 class Base(DeclarativeBase):
     pass
    
    
 class User(Base):
     __tablename__ = "users"
     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str]
     email: Mapped[str]


 crud = SyncCrudOperation(
     config, User, Base
 )

 crud.create_all_tables()
 crud.create(name="User", email="email@mail.ru")
 crud.read_all()  # [{'name': 'User', 'email': 'email@mail.ru'}]
 crud.limited_read(limit=5, offset=0)  # [{'name': 'User', 'email': 'email@mail.ru'}]
 crud.read_by_id(id=1)  # [{'name': 'User', 'email': 'email@mail.ru'}]
 crud.update_by_id(id=1, name="new value",)
 crud.delete_by_id(id=1)
 crud.delete_all_tables()
