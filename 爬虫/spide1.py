#-*- codeing = utf-8 -*-
#@Time : 2021/8/1721:27
#@Author : mch
#@File : spide1.py
#@Software : PyCharm

from bs4 import BeautifulSoup                      #网页解析，获取数据
import re                       #正则表达式——文字匹配
import urllib.request           #制定URL，获取网页数据
import xlwt                     #进行excel操作
import sqlite3                  #进行SQlite数据库操作
import urllib.error


# noinspection PyInterpreter,PyInterpreter
def main():
    baseurl = "https://movie.douban.com/top250?start="

    datalist = GetData(baseurl)
    #savepath_1 = ".//豆瓣电影top250.xls"
    savepath_2 = "movie.db"

    #SaveData(datalist,savepath_1)
    SaveDataDB(datalist,savepath_2)
# askURL("https://movie.douban.com/top250?start=")

#影片详情
findLink = re.compile(r'<a href="(.*?)">')      #创建正则表达式内容，表示规则
#影片封面    width="100"/>
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
# findImgSrc = re.compile(r'<img alt=".*" class="" src="(.*?)" width="100"/>',re.S)
#影片片名
# findName = re.compile(r'<span class="title">(.*)</span>')
findName = re.compile(r'<span class="title">(.*?)</span>')
#影片评分
# findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#评价人数
# findJudge = re.compile(r'<span>(\d*)人评价</span>')
findJudge = re.compile(r'<span>(\d*?)人评价</span>')
#电影概况
# findInq = re.compile(r'<span class="inq">(.*)</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
#影片相关
# findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


#1.爬取网页
def GetData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i * 25)
        html = askURL(url)      #保存获取到的网页源码
        #2.解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_ = "item"):
            #print(item)            测试：查看item全部信息
            data = []               #保存一部电影的信息
            item = str(item)

            link_1 = re.findall(findLink,item)[0]     #re库用正则表达式来查找指定的字符串
            data.append(link_1)
            # print(link_1)
            # print(type(link_1))
            link_2 = re.findall(findImgSrc,item)[0]
            data.append(link_2)
            # print(link_2)
            # print(type(link_2))
            link_3 = re.findall(findName,item)
            if len(link_3) == 2:
                name_1 = link_3[0]
                data.append(name_1)
                name_2 = link_3[1].replace("/","")      #去掉无关符号
                data.append(name_2)
            else:
                data.append(link_3[0])
                data.append(' ')
            # print(link_3)
            link_4 = re.findall(findRating,item)[0]
            data.append(link_4)
            # print(link_4)
            link_5 = re.findall(findJudge,item)[0]
            data.append(link_5)
            # print(link_5)
            link_6 = re.findall(findInq,item)
            if len(link_6) != 0:
                link_6 = link_6[0].replace("。","")
                data.append(link_6)
            else:
                data.append(' ')
            # print(link_6)
            # link_7 = re.findall(findBd,item)[0]
            # data.append(link_7)
            # print(link_7)
            datalist.append(data)                   #把处理好的一部电影信息存入datalist
    # for i in datalist:
    #     print(i)

    return datalist

# 得到指定一个url的网页内容
def askURL(url):
    head = {                   #模拟浏览器头部信息，向服务器发送消息
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 92.0.4515.131Safari / 537.36Edg / 92.0.902.73"
    }                           #用户代理，告诉服务器我们是什么类型的机器/浏览器（本质上是告诉服务器，我们可以接受什么样的文件）
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reaeon"):
            print(e.reason)
    return html

#3.保存数据
def SaveData(datalist,savepath):

    workbook = xlwt.Workbook(encoding="utf-8",style_compression = 0)
    worksheet = workbook.add_sheet('Top250',cell_overwrite_ok = True)
    col = ("链接","封面","片名(中)","片名(外)","评分","人数","概况","其他")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print(i+1)
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

def SaveDataDB(datalist,savepath_2):
    init_db(savepath_2)
    conn = sqlite3.connect(savepath_2)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            # if
            data[index] = '"' + str(data[index]) + '"'
            # data[index] = '"' + data[index] + '"'
            # data[index] = str(data[index])
            # print(data[index])
        sql = '''
            insert into movie250 (
            info_link,pic_link,cname,ename,score,rated,su)
            values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(savepath_2):
    sql = '''
        create table if not exists movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        su text
        );
    '''
    con = sqlite3.connect(savepath_2)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

if __name__ == "__main__":
    try:
        main()
    finally:
        print("完成！")
