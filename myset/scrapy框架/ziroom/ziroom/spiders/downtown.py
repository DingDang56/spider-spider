# -*- coding: utf-8 -*-
import scrapy
from ..items import DownTown
import pymongo
from lxml import etree
import requests

class DowntownSpider(scrapy.Spider):
    client = pymongo.MongoClient('localhost')
    name = 'downtown'
    allowed_domains = ['ziroom']
    db = client['ziroom_cities']
    info = db["ziroom_concrete"].find()
    start_urls = []
    for inf in info:
        gg_name = inf.get("c_name")
        gg_url = inf.get("c_url")
        # print(gg_url)
        start_urls.append(gg_url)


    def parse(self, response):
        html = response.body.decode("utf-8")
        r_url = response.url
        tree = etree.HTML(html)
        pages = int(tree.xpath("//span[@class='pagenum']/text()")[0][1:])

        city = tree.xpath('//span[@id="curCityName"]/text()')[0] # 大城市
        gra_name = tree.xpath('//div[@id="none_id"]/span/a/text()')[0] # 某大区
        fa_name = tree.xpath('//div[@id="none_id"]/span/a/text()')[1] # 某小区

        # print(city)
        # print(gra_name)
        # print(fa_name)

        for page in range(1,pages+1):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            }
            l_url = r_url+f"?p={page}"
            l_response = requests.get(url=l_url,headers=headers).content.decode("utf-8")
            tree = etree.HTML(l_response)
            hourselist= tree.xpath('//ul[@id="houseList"]/li')
            for li in hourselist:
                title = "".join(li.xpath('.//h3/a[@class="t1"]/text()'))  # 标题 ---------列表页
                href = "http:"+li.xpath('.//a/@href')[3]  #详情页链接
                print(title)
                print(href)

                # price = scrapy.Field()  # 价格 ---------列表页
                tags = ",".join(li.xpath('.//p/span[@class="subway"]/text()'))  # 标签 ---------列表页
                print(tags)
                area = ",".join(li.xpath('.//div[@class="detail"]/p[1]/span[1]/text()'))  # 面积 ---------详情页
                floor = ",".join(li.xpath('.//div[@class="detail"]/p[1]/span[2]/text()'))  # 面积 ---------详情页
                room = ",".join(li.xpath('.//div[@class="detail"]/p[1]/span[3]/text()'))  # 面积 ---------详情页
                juli = ",".join(li.xpath('.//div[@class="detail"]/p[2]/span[1]/text()'))  # 面积 ---------详情页
                # print(area,floor,room,juli)
                # direction = scrapy.Field()  # 朝向 ---------详情页
                # room = scrapy.Field()  # 房间 --------- 详情页
                # floor = scrapy.Field()  # 楼层 --------- 详情页
                # traffic = scrapy.Field()  # 交通 --------- 详情页
                # settings = scrapy.Field()  # 房间配置 ---------详情页
                rent = ",".join(li.xpath('.//span[@class="green"]/text()')).replace("\t","").replace(" ","").replace("\n","") # 是否首次出租 --------- 列表页
                atmo = ",".join(li.xpath('.//span[@class="org"]/text()')).replace("\t","").replace(" ","").replace("\n","")  # 空气质量 --------- 列表页
                # vacant = scrapy.Field()  # 空置天数 --------- 列表页
                count = ",".join(li.xpath('.//p[@class="leave"]/text()')).replace("\t","").replace(" ","").replace("\n","")  # 房间总数 --------- 列表页
                item=DownTown()
                item["city"]=city
                item["gra_name"]=gra_name
                item["fa_name"]=fa_name
                item["tags"]=tags
                item["area"]=area
                item["floor"]=floor
                item["room"]=room
                item["juli"]=juli
                item["rent"]=rent
                item["atmo"]=atmo
                item["count"]=count
                yield  item
            #     print(rent,atmo,count)
            # print(len(hourselist))


