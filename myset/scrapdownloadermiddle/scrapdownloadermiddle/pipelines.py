# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class ScrapdownloadermiddlePipeline(object):
    def __init__(self):
        print(999)
        self.client = pymongo.MongoClient("localhost",27017)
        self.db = self.client["mytencent"]
        self.table = self.db["mytxzp"]

    def process_item(self, item, spider):
        self.table.insert(dict(item))
        print(89989)
        return item
