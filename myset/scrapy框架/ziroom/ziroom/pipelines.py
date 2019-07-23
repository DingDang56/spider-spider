# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ZiroomPipeline(object):
    def __init__(self):
        self.cient = pymongo.MongoClient("localhost")
        self.db1 = self.cient["ziroom_cities"]
        self.table1 = self.db1["ziroom_cities_data"]
        self.table2 = self.db1["ziroom_concrete"]
        self.table3 = self.db1["ziroom_detial"]

    # def process_item(self, item, spider): # 第一次获取所有城市
    #     self.table1.insert(dict(item))
    #     return item

    # def process_item(self,item,spider): #第二次获取具体城市
    #     self.table2.insert(dict(item))
    #     return item

    def process_item(self,item,spider):
        self.table3.insert(dict(item))

        return item
