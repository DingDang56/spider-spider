# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TecentItem


class TecentBossSpider(scrapy.Spider):
    name = 'tecent_boss'
    allowed_domains = ['tecent.com']
    start_urls = []
    for i in range(1,72):
        # if i == 1:
        url = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1561432610967&keyword=python&pageIndex={i}&pageSize=10&language=zh-cn&area=cn"
        start_urls.append(url)

    def parse(self, response):
        html = response.body.decode("utf-8")
        b_dict = json.loads(html)
        data = b_dict["Data"]["Posts"]
        for i in data:
            item = TecentItem()
            item["title"] = i.get("RecruitPostName")
            item["countryname"] = i.get("CountryName")
            item["locationname"] = i.get("LocationName")
            item["bgname"] = i.get("BGName")
            item["categoryname"] = i.get("CategoryName")
            item["responsibility"] = i.get("Responsibility")
            # print(title,countryname,locationname,bgname,categoryname,responsibility,sep="\n")
            yield item


        # with open("腾讯招聘.html","w",encoding="utf-8")as fp:
        #     fp.write(html)

'''
yield 生成器

import time
def A():
    while True:
        print("___A____")
        yield
        time.sleep(0.5)
def B(g):
    while True:
        print("___B_____")
        g.__next__()
        time.sleep(0.5)

if __name__ == '__main__':
    g = A()
    B(g)

'''

