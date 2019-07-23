# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TecentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    countryname = scrapy.Field()
    locationname = scrapy.Field()
    bgname = scrapy.Field()
    categoryname = scrapy.Field()
    responsibility = scrapy.Field()
