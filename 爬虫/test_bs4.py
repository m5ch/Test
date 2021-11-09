#-*- codeing = utf-8 -*-
#@Time : 2021/8/1915:47
#@Author : mch
#@File : test_bs4.py
#@Software : PyCharm


'''
BeautifulSoup4                  将复杂的HTML文件转换为复杂的树形结构每个节点都是python对象，可以归纳为4种：

1.Tag                           标签及其内容：拿到它所找到的第一个内容
2.NavigableString               标签里的内容（字符串）
3.BeautifulSoup                 表示整个文档
4.Comment                       是一个特殊的NavigableString,输出的内容不包含注释符号

'''


from bs4 import BeautifulSoup

#-----------------------------------------------

#文档的遍历






#文档的搜索

#1.find_all()               #字符串过滤：查找与字符串完全匹配的内容
#.find_all("")


#正则表达式搜索：使用search()来匹配内容
#import re
#.find_all(re.compile(""))



#根据函数内容搜索




#2. kwargs
#.find_all(** = "")
#.find_all(** = True)




#3. text参数



#4. limit参数
#.find_all("",limit = %d)       限制个数

#css 选择器

#.select.('title')             通过标签来查找

#.select(".mnav")              通过类名来查找

#.select('u1')                 通过id来查找

#.select("a[class = 'bri']")                 通过属性来查找

#.select('head > title')                 通过子标签来查找

#.select('.mnav ~ .bri')                 通过兄弟标签来查找