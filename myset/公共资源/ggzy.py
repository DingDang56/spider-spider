import re,requests,json,time,pymysql
from lxml import etree
from selenium import  webdriver
from selenium.webdriver.firefox.options import Options

conn = pymysql.connect(host="192.168.120.129",user="root",passwd = "",db="demo")
cur = conn.cursor(pymysql.cursors.Cursor)

def get_data(data):
    try:
        data = data.split("：")[-1]
    except:
        data = ""
    return data


firefox_options = Options()
# firefox_options.add_argument('--headless')
# firefox_options.add_argument('--disable-gpu')
driver = webdriver.Firefox(firefox_options=firefox_options) #要导入火狐驱动exe

url = "http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp"
headers = {
    "Host": "deal.ggzy.gov.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept-Encoding": "gzip, deflate",#既然gzip不影响结果，那就写上吧
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp",
    "Cookie": "JSESSIONID=2a88f58d4d0af113972a2ea52a6c; JSESSIONID=2a88f58d4d0af113972a2ea52a6c; insert_cookie=97324480"
}

import datetime
end = datetime.date.today()
start = datetime.date.today()-datetime.timedelta(days=9)
pages = 851 #专门爬个页面来找页数是不合算的，不如直接自己写
for page in range(1,pages+1):
    data = {
        "TIMEBEGIN_SHOW":f"{start}", #起始时间，今天-10+1
        "TIMEEND_SHOW":f"{end}", #结束时间，今天,建议通过程序获取
        "TIMEBEGIN":f"{start}", #起始时间
        "TIMEEND":f"{end}", # 结束时间
        "SOURCE_TYPE":"1",
        "DEAL_TIME":"02",
        "DEAL_CLASSIFY":"00", #
        "DEAL_STAGE":"0001", #1公告，2成交公示，0不限
        "DEAL_PROVINCE":"0",
        "DEAL_CITY":"0",
        "DEAL_PLATFORM":"0",
        "BID_PLATFORM":"0",
        "DEAL_TRADE":"0",
        "isShowAll":"1", # 1代表是
        "PAGENUMBER":f"{page}", #当前页码，#翻页策略：（1.手动填所有页，2自动循环，直到返回数据为空）
        "FINDTXT":"",#搜索关键字
    }

    response=requests.post(url=url,headers=headers,data=data).content.decode("utf-8")
    # with open("test_page3.json","w+",encoding="utf-8")as fp:#已经获取页面
    #     fp.write(response)

    """
    列表json页可以获取的字段有：
            注意空字段！
    title:大标题
    province:省份
    resource:来源平台
    btype:业务类型
    itype:信息类型
    deurl:详情页网址
    """

    # source = open("test_page3.json","r+",encoding="utf-8")
    # source = json.loads(source.read())

    # print(response)
    data = json.loads(response).get("data")
    print(data)
    for i in data:
        title =  i.get('title',"None")#没有取到，写None
        province = i.get('districtShow',"None")
        resource = i.get("platformName","None")
        btype = i.get("stageShow","None")
        itype = i.get("classifyShow","None")
        deurl = i.get("url","None")
    #     print(title,province,resource,btype,itype,deurl)


        # response=requests.get(url=deurl,headers=headers).content.decode("utf-8")
        # with open("detail.html","w+",encoding="utf-8")as fp:#已经获取页面
        #     fp.write(response) # 放弃，使用selenium

        driver.get(deurl)
        # print(deurl)
        width = driver.execute_script( # 截全屏，写在get.url下面
                "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
        height = driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        driver.set_window_size(width, height)

        # driver.save_screenshot("详情页.png")
        # with open("fox.shtml","w+",encoding="utf-8")as fp:#已经获取页面
        #     fp.write(driver.page_source)

        response = driver.page_source
        tree = etree.HTML(response)
        ul = tree.xpath("//ul[@class='ul_toggle']/li/@id")
        if len(ul)>1:
            ul[1],ul[2]=ul[2],ul[1] #把交易公告放到第二优先级来
        # print(ul) # 找到所有关键按钮
        dic = {"address": "", "linkman": "", "proxy": "", "telphone": "", "email": "", "endtime": ""}
        for li in ul:
            driver.find_element_by_id(li).click()
            response = driver.page_source
            tree = etree.HTML(response)
            id = 'div'+li[1:] # id 需要拼接
            # print(id)
            gonggao = tree.xpath(f"//div[@id='{id}']/ul[@class='fully_list']/li/a/@onclick")#div_0102
            # print(gonggao)
            if len(gonggao)==0: # 没有文件，去取第二个
                continue
            elif len(gonggao)>1:
                gonggao=gonggao[:1]
            else:
                gonggao=gonggao # 公告文件链接列表栏
            gong = gonggao[0].split("','")[-1][:-2]
            href="http://www.ggzy.gov.cn"+gong #获取文件链接
            print(href)
            response = requests.get(url=href,headers=headers)
            body = response.content.decode("utf-8") #body字段
            print(type(body))
            # with open("file.html","w+",encoding="utf-8")as fp:#已经获取页面
            #     fp.write(response.content.decode("utf-8"))

            pattern = re.compile(">(.*?)<")
            c = pattern.findall(body)
            alist1 = []
            for al in c:
                if len(al.strip().replace("&nbsp;","")):
                    alist1.append(al.strip().replace("&nbsp;",""))
            c = alist1
            print(c)

            for i in range(len(c)-1): # 允许被覆盖
                if "截" in c[i] and "止" in c[i] and "时" in c[i] and "间" in c[i] and "，" not in c[i] and "," not in c[i] and "超" not in c[i]:
                    if "：" not in c[i]:
                        dic["endtime"] = c[i+1]
                    else:
                        dic["endtime"] = get_data(c[i])
                if "代" in c[i] and "址" in c[i] and "，" not in c[i] and "," not in c[i] and "邮" not in c[i] and "原" not in c[i]:
                    dic["address"] = get_data(c[i])
                    # if "：" not in c[i+1]:
                    #     dic["address"] = dic["address"]+","+c[i+1]
                    if "：" not in c[i] and "：" in c[i+1]:
                        dic["address"] = c[i+1].split("：")[-1]
                if "联系人" in c[i] and "，" not in c[i] and "," not in c[i] or "代理机构联系方式" in c[i]:
                    dic["linkman"] = get_data(c[i])
                    if "：" not in c[i+1]:
                        if dic["linkman"] == "":
                            dic["linkman"] = c[i+1]
                        else :
                            dic["linkman"] = dic["linkman"] + "," + c[i + 1]
                    if "：" not in c[i] and "：" in c[i+1]:
                        dic["linkman"] = c[i+1].split("：")[-1]
                    if re.findall("\d+",c[i+1]):
                        dic["telphone"]=c[i+1]
                if "代" and "理" and "机" and "构" in c[i] and "，" not in c[i] and "," not in c[i]:
                    dic["proxy"] = get_data(c[i])
                if "电" and "话" in c[i] and "监" not in c[i] and "，" not in c[i] and "," not in c[i] and "（" not in c[i]:
                    dic["telphone"] = get_data(c[i])
                    if dic["telphone"] == "":
                        dic["telphone"] = c[i+1]
                if "邮" in c[i] and "，" not in c[i] and "," not in c[i]:
                    dic["email"] = get_data(c[i])
                    if dic["email"] == "":
                        dic["email"] = c[i+1]

            print("地址",dic["address"])  # 允许被覆盖
            print("联系人",dic["linkman"])
            print("代理机构",dic["proxy"])
            print("电话",dic["telphone"])
            print("邮箱",dic["email"])
            print("结束时间",dic["endtime"])
        try:
            print(title,resource,dic['endtime'],dic['address'],dic['linkman'],dic['telphone'],dic['email'],"999999999999",href)
            cur.execute("insert into ggzy('title','resource','endtime','address','linkman','telphone','eamil','body','bodyurl') values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(title,resource,dic['endtime'],dic['address'],dic['linkman'],dic['telphone'],dic['email'],"999999999999",href))
            conn.commit()
        except Exception as e:
            print('插入失败', e)
            conn.rollback()
        break






