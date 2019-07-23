from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from scrapy.http import HtmlResponse
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")




class ScrapdownloadermiddleDownloaderMiddleware(object):
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument(('--proxy-server=https://' + "112.85.168.206:9999"))
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def process_request(self, request, spider):
        if request.meta.get("PhantomJS"):
            self.driver.get(request.url)
            html = self.driver.page_source
            # print(html)

            return HtmlResponse(url=request.url,body=html,encoding="utf-8",request=request)
