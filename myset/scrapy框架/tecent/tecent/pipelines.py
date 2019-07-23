# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
class TecentPipeline(object):
    def __init__(self):
        #连接数据库
        self.client = pymongo.MongoClient("localhost")
        #创建数据库
        self.db = self.client["tencent"]
        #创建集合
        self.table = self.db["tencent_data"]



    def process_item(self, item, spider):

        # fp = open("腾讯招聘.json","a+",encoding="utf-8")
        # json.dump(dict(item),fp,ensure_ascii=False)

        self.table.insert(dict(item))

        return item  # 相当于next,产生协程