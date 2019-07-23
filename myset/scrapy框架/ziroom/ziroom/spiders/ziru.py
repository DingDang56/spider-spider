# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import City


class ZiruSpider(scrapy.Spider):
    name = 'ziru'
    allowed_domains = ['ziroom.com']
    start_urls = ['http://www.ziroom.com/z/nl/z3.html']

    def parse(self, response):
        html = response.body.decode("utf-8")
        # print(1)
        # with open('自如租房.html',"w",encoding="utf-8")as fp:
        #     fp.write(html)
        dd = etree.HTML(html)
        dl = dd.xpath('//dl[@class="changeCityList"]/dd/a')
        # print(len(dl))
        for city in dl:
            # print(2)
            print(city)
            city_name = city.xpath("./text()")[0]
            city_url = city.xpath("./@href")[0]

            item = City()
            item["city_name"] = city_name
            item["city_url"] = city_url
            # with open("location.txt","a",encoding="utf-8")as fp:
                # content = city_name + "\t" + city_url +"\n"
                # fp.write(content)
            yield item