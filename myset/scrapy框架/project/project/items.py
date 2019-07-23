# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()
    name = scrapy.Field()
    state = scrapy.Field()
    s_type = scrapy.Field()
    tv = scrapy.Field()
    u_time = scrapy.Field()


