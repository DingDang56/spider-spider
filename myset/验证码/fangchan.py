import requests,re,json,time,random,math,os
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def redata(data):
    try:
        name = data[0]
    except:
        name = "None"
    return name
# os.makedirs("安居客")
#字段：图片，标题，室(数字)，厅(数字)，面积，楼层，总楼层，经纪人，小区名，城区，商圈，地址，租房方式，朝向，地铁线，价格。
url = "https://bj.zu.anjuke.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
# driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# driver.get(url)
# time.sleep(3)
# driver.save_screenshot("fangchan.bmp")
for q in range(9,51):
    url = f"https://bj.zu.anjuke.com/fangyuan/p{q}/"
    response = requests.get(url = url,headers = headers).content.decode("utf-8") #列表页
    # with open ("房产.html","w",encoding="utf-8")as fp:
    #     fp.write(response)
    tree = etree.HTML(response)
    div = tree.xpath('//div[@class="zu-itemmod"]/@link')[::-1]
    count =0
    for durl in div:
        count += 1
        response2 = requests.get(url = durl,headers = headers).content.decode("utf-8") #详情页
        '''
        if durl == div[0]:
            with open("detail.html","w",encoding="utf-8")as fp:
                fp.write(response2)
        else:
            break
        '''
        dtree = etree.HTML(response2)
        # info = dtree.xpath('//')
        title = dtree.xpath('//h3[@class="house-title"]/text()')
        title = redata(title) #标题
        price = "".join(dtree.xpath('//span[@class="light info-tag"]//text()')) #价格

        room = "".join(dtree.xpath('//span[@class="info-tag"]//text()')).strip() #室厅
        area = "".join(dtree.xpath('//span[@class="info-tag no-line"]//text()')) #面积
        way = dtree.xpath('//li[@class="title-label-item rent"]/text()') #租房方式
        way = redata(way)

        type = dtree.xpath('.//span[@class="type"]/text()')  # 房子类型
        type = redata(type)

        ori = dtree.xpath('//li[@class="title-label-item buy"]/text()') #朝向
        ori = redata(ori)

        subway = dtree.xpath('//li[@class="title-label-item subway"]/text()') #地铁线
        subway = redata(subway)

        img = dtree.xpath('//div[@id="room_pic_wrap"]/div[@class="img_wrap"][1]/img/@src') #图片
        img = redata(img)

        shoper = dtree.xpath('//h2[@class="broker-name"]/text()') #销售
        shoper = redata(shoper)

        bed = dtree.xpath('.//ul[@class="house-info-zufang cf"]/li[@class="house-info-item l-width"]/span[@class="info"]/text()') #具体户型
        bed = redata(bed)

        floor = dtree.xpath('.//ul[@class="house-info-zufang cf"]/li[@class="house-info-item l-width"]/span[@class="info"]/text()')[1] #楼层
        street ="".join( dtree.xpath('.//ul[@class="house-info-zufang cf"]/li[@class="house-info-item l-width"]/a/text()')).replace('\n',"").replace(" ","") #小区

        decorate = dtree.xpath('//li[@class="house-info-item"][3]/span[@class="info"]/text()') #装修
        decorate = redata(decorate)

        hourse_type = dtree.xpath('//li[@class="house-info-item"][4]/span[@class="info"]/text()') #房子类型
        hourse_type = redata(hourse_type)

        require = dtree.xpath('//li[@class="house-info-item"][5]/span[@class="info"]/text()') #要求
        require = redata(require)

        content=f"标题：{title}\n价格：{price}\n面积：{area}\n具体户型：{bed}\n租赁方式：{way}\n朝向：{ori}\n地铁线：{subway}\n图片:{img}\n销售：{shoper}\n楼层：{floor}\n小区：{street}\n装修：{decorate}\n房子类型：{hourse_type}\n要求：{require}\n\n"
        with open(f"安居客\{q}.json","a+",encoding="utf-8")as e:
            e.write(content)
        print(count)
        print(content)

# print(div)
# print(len(div))
# print(response)




