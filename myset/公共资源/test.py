# import re
# a = open("file.html","r+",encoding="utf-8")
# b =a.read()
# print(b)
# pattern = re.compile(">(.*?)<")#在联系方式一栏
# c = pattern.findall(b)
# print(c)
# jiezhi = ""
#
# def get_data(data):
#     try:
#         data = data.split("：")[-1]
#     except:
#         data = ""
#     return data
# for i in c:
#     if "地" and "址" in i:
#         address = get_data(i)
#     if "联" and "系" and "人"  in i:
#         linkman = get_data(i)
#     if "代" and "理" and "机" and "构" in i:
#         proxy = get_data(i)
#     if "电" and "话" in i and "监" not in i:
#         telphone = get_data(i)
#     if "邮" in i:
#         email = get_data(i)
#
#
# print(address) #允许被覆盖
# print(linkman)
# print(proxy)
# print(telphone)
# print(email)


# import datetime
# print(datetime.date.today())
# print(datetime.date.today()-datetime.timedelta(days=9))

# import re
# print(re.findall("\d+",'0311-87660023'))
print('d' in '99')