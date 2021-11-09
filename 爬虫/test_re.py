#-*- codeing = utf-8 -*-
#@Time : 2021/8/2121:41
#@Author : mch
#@File : test_re.py
#@Software : PyCharm


#正则表达式：字符串模式（判断字符串是否含有一定的标准）

import re

#创建模式对象

pat = re.compile("AA")

m = pat.search("AFA")                   #search方法：进行比对查找

m = pat.search("LKGAA")

#m = pat.search("AALIGFJAAA")

print(m)

#没有模式对象

i = re.search("asd","lkjasd")           #前面为规则，后面为被校验的对象

print(i)


print(re.findall("[^A-Z]+","KVDIvnjJOFPD"))


#sub:替换

print(re.sub("a","A","ananvjd"))            #找到a用A替换，在第三个字符串中查找


#建议在正则表达式中，被比较的字符串前面加"r",(不用担心转义字符的问题)