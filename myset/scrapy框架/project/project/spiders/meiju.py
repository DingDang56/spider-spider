# -*- coding: utf-8 -*-
import scrapy
from ..items import ProjectItem
from lxml import etree



class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ["https://www.meijutt.com/new100.html"]

    def parse(self, response):
        html = response.body.decode("gb2312")
        tree = etree.HTML(html)
        ul = tree.xpath('//ul[@class="top-list  fn-clear"]/li')
        # with open("meiju_new100.html","w",encoding="gb2312")as fp:
        #     fp.write(html)
        for li in ul:
            item = ProjectItem()
            item["index"] = li.xpath('.//div/i/text()')[0]
            item["name"] = li.xpath('.//h5/a/@title')[0]
            item["state"] = li.xpath('.//span/font/text()')[0]
            item["s_type"] = li.xpath('.//span[@class="mjjq"]/text()')[0]
            item["tv"] = li.xpath('.//span[@class="mjtv"]/text()')[0]
            item["u_time"] = li.xpath('.//div[@class="lasted-time new100time fn-right"]//text()')[0]

            yield item


