# -*- coding: utf-8 -*-
import scrapy
import pymongo
from ..items import Concrete
from lxml import etree

class ConcreteSpider(scrapy.Spider):
    name = 'concrete'
    allowed_domains = ['ziroom']
    client = pymongo.MongoClient('localhost')

    # 连接名叫'newtestdb'数据库
    db = client['ziroom_cities']
    start_urls = []

    info = db["ziroom_cities_data"].find() # 查询出来的数据必须遍历才能出来
    for inf in info:
        city_url = "http:"+inf.get("city_url")
        city_name = inf.get("city_name")
        # print(city_name)
        start_urls.append(city_url)

    def parse(self, response):
        item = Concrete()

        # 这里我们需要获取每个城市的具体小区的信息
        # print("ddddd") #调试
        html = response.body.decode("utf-8")
        # print(html) # 调试
        tree = etree.HTML(html)
        alist = tree.xpath("//ul[@class='clearfix filterList'][1]/li")[1:] # 城市分区
        for sqli in alist:
            fenqu = sqli.xpath('.//span/a/text()')[0]
            # print(fenqu)  # 分区名
            blist = sqli.xpath('.//div/span/a')[1:]
            for juti in blist:
                j_url = "http:"+juti.xpath('./@href')[0]
                j_name = fenqu+juti.xpath('./text()')[0]
                item["c_name"] = j_name
                item["c_url"] = j_url
                print(j_url,j_name)
                yield  item
        # print(len(alist))


