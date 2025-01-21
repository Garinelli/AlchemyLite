Working with Tables and Fields
==============================

This section will show you how to create tables using AlchemyLite.

To create use the following approach

.. code-block:: python
    
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

When creating an instance of a class, two parameters are passed to the constructor:

1. table_name - Name of your table
2. fields - Fields of your custom table. This parameter must be a dictionary, where all the table fields are described

There is no need to create a row (id) with a primary key, this is done automatically by the library

For a class to become a sqlalchemy model, you need to access the .model property.

.. code-block:: python

    user = user.model

The class accepts two params, the first is table name, the second is fields of table Types can be as follows:

1. int
2. str
3. bool
4. float
5. "date"
6. "datetime"
7. "time"
8. "text"

If you specify a str type, you must specify a maximum length for it, using "max_len"

If there is no need to use max_len then use type "text"

You can also specify additional parameters for the row

1. nullable - True or False. Default - True
2. default - Your value. Default - None
3. unique - True or False. Default - False
4. index - True or False. Default - False

You can also add a foreign key row. Example:

.. code-block:: python
    
    from alchemylite import Table

    order = Table(
        table_name='orders',
        fields={
            "user": {"type": int, "foreignkey": "users.id"},
            "item": {"type": str}
        }
    )

    order = order.model

We have now learned how to create tables using only Python syntax.

You can also use these models in SyncCrudOperation and AsyncCrudOperation classes.