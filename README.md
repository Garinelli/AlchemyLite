# AlchemyLite
## A library that simplifies CRUD operations with PostgreSQL database.

# What is new in 0.1.0 release?
[Full docs](https://alchemylite.readthedocs.io/)
1. With this release, you can create a table in a database without using sqlalchemy syntax.  
How to do this?
```python
from alchemylite import Table

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
```  
There is no need to create a row (id) with a primary key, this is done automatically by the library   
For a class to become a sqlalchemy model, you need to access the .model property.  
```python
user = user.model
```
The class accepts two params, the first is table name, the second is fields of table
Types can be as follows:
* int
* str,
* bool
* float
* "date"
* "datetime"
* "time"
* "text"  

If you specify a str type, you must specify a maximum length for it, using "max_len"  
If there is no need to use max_len then use type "text"  
You can also specify additional parameters for the row  
* nullable - True or False. Default value - True
* default - Your value. Default - None
* unique - True or False. Default - False
* index - True or False. Default - False

2. There is no need to transfer config.session, just config  
Example  
```python
from alchemylite.sync import SyncCrudOperation, SyncConfig
from alchemylite import Table

User = Table(
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

User = User.model

config = SyncConfig(
    db_host="localhost",
    db_port="5432",
    db_user="postgres",
    db_pass="qwertyQ",
    db_name="AlchemyLite"
)

crud = SyncCrudOperation(config, User)
```
Previously it was necessary to transfer it like this:  
```python
crud = SyncCrudOperation(config.session, User)
```

3. It is not necessary to pass Base to a class with CRUD operations  
Only need to pass if you want to use the create_all_tables() and delete_all_tables() methods
To create and delete a table
Example
```python
crud = SyncCrudOperation(config, User)
```
4. You can also add a foreign key row  
Example
```python
from alchemylite import Table

order = Table(
    table_name='orders',
    fields={
        "user": {"type": int, "foreignkey": "users.id"},
        "item": {"type": str}
    }
)
order = order.model
```
# How to use it?
First, install the library with the command ```pip install AlchemyLite```  
First you need to create a configuration in which you need to register the database parameters  
For synchronous operation
```python
from alchemylite.sync impoty SyncConfig

config = SyncConfig(
    db_host="your_host",
    db_port="your_port",
    db_user="your_user",
    db_pass="your_password",
    db_name="your_db_name"
)
```
Then, we create a class to which we pass our configuration, model class and base class of model
```python
from alchemylite.sync import SyncCrudOperation

crud = SyncCrudOperation(
    config.session, YourModel, Base
)
```
For async operation
```python
from alchemylite.async_ import AsyncConfig, AsyncCrudOperation

config = AsyncConfig(
    db_host="your_host",
    db_port="your_port",
    db_user="your_user",
    db_pass="your_password",
    db_name="your_db_name"
)

crud = AsyncCrudOperation(
    config.session, YourModel, Base
)
```
# How to perform CRUD operations?
The library supports the following methods
* create - Creates new data in the table.
* read_all - Reads all data from a table.
* limited_read - Reads a certain amount of data. Default values: limit = 50, offset = 0
* read_by_id - Reads all data from a table by id
* update_by_id - Update data by id
* delete_by_id - Delete data by id
* create_all_tables - Creates all tables in database
* delete_all_tables - Delete all tables in database

# Examples of use

```python
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
    config.session, User, Base
)

crud.create_all_tables()
crud.create(name="User", email="email@mail.ru")
crud.read_all()
crud.limited_read(limit=5, offset=0)
crud.read_by_id(id=1)
crud.update_by_id(id=1, name="new value", email="new_emal")
crud.delete_by_id(id=1)
crud.delete_all_tables()
```
## The library will be supported, this is the first version for now. New features will be added in the future.
### If you have suggestions for improvements or any comments, I'm ready to listen to you
