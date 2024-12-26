from alchemylite import Table

order = Table(
    table_name='orders',
    fields={
        "user": {"type": int, "foreignkey": "users.id"},
        "item": {"type": str}
    }
)
order = order.model


