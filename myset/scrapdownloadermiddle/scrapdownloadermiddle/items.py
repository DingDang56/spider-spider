# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapdownloadermiddleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    '''
    {"Id": 0, "PostId": "1123176879843446784",
     "RecruitPostId": 48075,
     "RecruitPostName": "CSIG16-python高级研发工程师",
     "CountryName": "中国",
     "LocationName": "北京",
     "BGName": "CSIG",
     "ProductName": "",
     "CategoryName": "技术",
     "Responsibility": "1.负责地理数据采集平台核心系统/模块的设计和研发；\n"
                       "2.负责关键技术调研和设计实现；\n3.负责相关系统或模块文档的撰写。",
     "LastUpdateTime": "2019年06月24日",
     "PostURL": "http://careers.tencent.com/jobdesc.html?postId=1123176879843446784",
     "SourceID": 1,
     "IsCollect": false,
     "IsValid": false
     }
    '''


    recruitpostname = scrapy.Field() #职位名称
    locationname = scrapy.Field() #工作地点
    bgname = scrapy.Field() # 大类
    productname = scrapy.Field() #产品名称
    categoryname = scrapy.Field() #职位类型
    responsibility = scrapy.Field() #工作职责
    lastupdatetime = scrapy.Field() # 发布时间
    explainitem = scrapy.Field() # 招聘要求
    PostId = scrapy.Field() # ID
    PostURL = scrapy.Field() #详情网址


