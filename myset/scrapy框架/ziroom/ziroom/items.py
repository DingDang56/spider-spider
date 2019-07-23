# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZiroomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class City(scrapy.Item):
    city_name = scrapy.Field()
    city_url = scrapy.Field()

class Concrete(scrapy.Item):
    c_name = scrapy.Field()
    c_url = scrapy.Field()

class DownTown(scrapy.Item):
    # title = scrapy.Field()  # 标题 ---------列表页
    # price = scrapy.Field()  # 价格 ---------列表页
    # tags = scrapy.Field()  # 标签 ---------列表页
    # area = scrapy.Field()  # 面积 ---------详情页
    # direction = scrapy.Field()  # 朝向 ---------详情页
    # room = scrapy.Field() # 房间 --------- 详情页
    # floor = scrapy.Field() # 楼层 --------- 详情页
    # traffic = scrapy.Field() # 交通 --------- 详情页
    # settings = scrapy.Field() #房间配置 ---------详情页
    # rent = scrapy.Field() # 是否首次出租 --------- 列表页
    # atmo = scrapy.Field() # 空气质量 --------- 列表页
    # vacant = scrapy.Field() # 空置天数 --------- 列表页
    # count = scrapy.Field() # 房间总数 --------- 列表页

    city = scrapy.Field()
    gra_name = scrapy.Field()
    fa_name = scrapy.Field()
    tags = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    room = scrapy.Field()
    juli = scrapy.Field()
    rent = scrapy.Field()
    atmo = scrapy.Field()
    count = scrapy.Field()