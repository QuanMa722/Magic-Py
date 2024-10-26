# -*- coding: utf-8 -*-

from pymongo import MongoClient
import os

# 连接数据库

# 方法1
# 连接到 MongoDB 服务器
client = MongoClient('mongodb://localhost:27017/')

# 方法2
# 从环境变量获取连接字符串
# mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
# client = MongoClient(mongo_uri)

# 方法3
# 配置文件
# {
#   "mongo_uri": "mongodb://localhost:27017/"
# }
# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)
#     mongo_uri = config['mongo_uri']
#
# client = MongoClient(mongo_uri)

# 方法4
# 创建连接池
# client = MongoClient('mongodb://localhost:27017/', maxPoolSize=10)

# 创建数据库 'MyDatabase'
# 惰性创建，只有数据插入后才会创建
db = client['MyDatabase']

# 创建集合 'MyCollection'
collection = db['MyCollection']

# 插入一条数据，自动创建数据库和集合
document = {
    "_id": "custom_id_001",
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
result = collection.insert_one(document)

# 打印插入的文档 ID
print("插入的文档 ID:", result.inserted_id)

print(db.list_collection_names())

# 创建要插入的多条数据
# documents = [
#     {"name": "Alice", "age": 30, "city": "New York"},
#     {"name": "Bob", "age": 25, "city": "Los Angeles"},
#     {"name": "Charlie", "age": 35, "city": "Chicago"},
#     {"name": "Diana", "age": 28, "city": "Houston"}
# ]

# # 使用 insert_many() 插入多条数据
# result = collection.insert_many(documents)

# # 打印插入的文档 ID
# print("插入的文档 ID:", result.inserted_ids)

# $eq：等于
# $ne：不等于
# $gt：大于
# $gte：大于等于
# $lt：小于
# $lte：小于等于
# $and：与
# $or：或
# $not：非

# 删除数据库
# client.drop_database('MyDatabase')

# 删除集合
# db[collection_name].drop()

