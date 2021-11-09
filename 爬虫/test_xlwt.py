#-*- codeing = utf-8 -*-
#@Time : 2021/8/22  22:16
#@Author : mch
#@File : test_xlwt.py
#@Software : PyCharm


import xlwt

workbook = xlwt.Workbook(encoding = "utf-8")
worksheet = workbook.add_sheet('sss')
for i in range(1,10):
    for j in range(1,i+1):
        worksheet.write(i-1,j-1,"%d * %d = %d"%(j,i,i * j))

#worksheet.write(0,0,"hello")
workbook.save('xlwt_1.xls')