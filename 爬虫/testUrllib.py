#-*- codeing = utf-8 -*-
#@Time : 2021/8/1810:22
#@Author : mch
#@File : testUrllib.py
#@Software : PyCharm

import urllib.request
#
#
# #获取一个get请求
# response = urllib.request.urlopen("http://www.bsidu.com")
# print(response.read().decode('utf-8'))                  #对获取到的网页进行utf-8的解码


# #获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"莫成辉"}),encoding = "utf-8")
# response_1 = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response_1.read().decode("utf-8"))





# #伪装成浏览器
# headers = {
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
# }
# url = "https://www.douban.com"
# req = urllib.request.Request(url = url,data = data,headers = headers,method = "POST")
# print()



headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}
url = "https://www.douban.com"
req = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))