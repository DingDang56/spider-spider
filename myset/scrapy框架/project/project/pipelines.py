# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ProjectPipeline(object):
    def process_item(self, item, spider):
        fp = open("meiju.json","a",encoding="gb2312")
        json.dump(dict(item),fp,ensure_ascii=False)
        print(fp)

        return item


























        # with open("meiju.json","a+",encoding="gb2312")as e:
        #     e.write(fp)

        # fp.close()