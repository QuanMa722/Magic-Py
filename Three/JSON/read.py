# -*- coding: utf-8 -*-

import json

with open('news.json', 'r', encoding='utf-8') as f:
    news_list: list[str] = json.load(f)

print(news_list[0])
