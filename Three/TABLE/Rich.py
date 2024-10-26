# -*- coding: utf-8 -*-

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

users = [
    {'id': '1', 'name': 'alice', 'age': '16'},
    {'id': '2', 'name': 'bob', 'age': '15'},
    {'id': '3', 'name': 'kate', 'age': '19'},
]

table = Table(title=None, box=box.ROUNDED)

table.add_column('id', justify='center')
table.add_column('name', justify='center')
table.add_column('age', justify='center')

for user in users:
    table.add_row(user['id'], user['name'], user['age'])


console.print(table)
