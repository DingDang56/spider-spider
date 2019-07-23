# -*- coding: utf-8 -*-
import scrapy,json
from lxml import etree
from ..items import ScrapdownloadermiddleItem


class TenPythonSpider(scrapy.Spider):
    name = 'ten_python'
    allowed_domains = ['tencent.com']
    print(3)
    start_urls = [
        "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1561539501193&keyword=python&pageIndex=1&pageSize=720&language=zh-cn&area=cn"
    ]

    def parse(self, response):
        print(5)
        html = response.body.decode("utf-8")
        # with open("tencent.json","w",encoding="utf-8")as fp:
        #     fp.write(html)
        bdict = json.loads(html)
        blist = bdict["Data"]["Posts"] # 内容列表

        for mdict in blist:
            recruitpostname = mdict.get("RecruitPostName")  # 职位名称
            locationname = mdict.get("LocationName")  # 工作地点
            bgname = mdict.get("BGName")  # 大类
            productname = mdict.get("ProductName")  # 产品名称
            categoryname = mdict.get("CategoryName")  # 职位类型
            responsibility = mdict.get("Responsibility")  # 工作职责
            lastupdatetime = mdict.get("LastUpdateTime")  # 发布时间
            # explainitem = mdict.get("RecruitPostName")  # 招聘要求
            PostId = mdict.get("PostId")  # ID
            PostURL = mdict.get("PostURL")  # 详情网址

            item = ScrapdownloadermiddleItem()
            item["recruitpostname"] = recruitpostname
            item["locationname"] = locationname
            item["bgname"] = bgname
            item["productname"] = productname
            item["categoryname"] = categoryname
            item["responsibility"] = responsibility
            item["lastupdatetime"] = lastupdatetime
            item["PostId"] = PostId
            item["PostURL"] = PostURL

            durl = "http://careers.tencent.com/jobdesc.html?postId=" + item["PostId"]

            yield scrapy.Request(durl,callback=self.de_parse,meta={"data":item,"PhantomJS":True},dont_filter=True)

    def de_parse(self,response):
        item = response.request.meta["data"]
        html = response.body.decode("utf-8")
        tree = etree.HTML(html)
        explainitem = "".join(tree.xpath("//div[@class='duty-text']/ul/li[@class='explain-item']//text()"))
        if explainitem:
            item["explainitem"] = explainitem
        else:
            item["explainitem"] = "暂无其他要求"
        print(item["recruitpostname"])

        yield item



