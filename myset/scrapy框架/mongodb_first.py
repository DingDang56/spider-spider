import pymongo

#客户端对象
client = pymongo.MongoClient('localhost')

#连接名叫'newtestdb'数据库
db = client['newtestdb']

#获取名为newtable的表，并插入一条信息
db["newtable"].insert({'name':"雷诗婕",'age':"18","sex":"男","married":False})

#查询条件为name = 雷诗婕的数据
info = db["newtable"].find_one({"name":"雷诗婕"})
print(type(info),info)