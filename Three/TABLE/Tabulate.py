# -*- coding: utf-8 -*-

from tabulate import tabulate

users = [
    {'id': '1', 'name': 'alice', 'age': '16'},
    {'id': '2', 'name': 'bob', 'age': '15'},
    {'id': '3', 'name': 'kate', 'age': '19'},
]

table = tabulate(users, headers='keys', tablefmt='grid', stralign='center')

print(table)
