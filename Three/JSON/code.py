# -*- coding: utf-8 -*-

import json

data = [
    {"name": "Alice", "age": 30, "isStudent": False},
    {"name": "Bob", "age": 25, "isStudent": True},
    {"name": "Charlie", "age": 22, "isStudent": True},
]

for infor in data:
    if infor['name'] == 'Bob':
        data.remove(infor)


json_string = json.dumps(data, indent=4, ensure_ascii=False)  # ensure_ascii=False 用于正确处理非 ASCII 字符

print(json_string)

with open('data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_string)
