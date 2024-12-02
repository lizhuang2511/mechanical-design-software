# -*- coding = utf-8 -*-
# @time:2023/10/13 19:25
# Author:lizhuang
# @File:表格处理测试.py
# @Software:PyCharm
import xlwings as xw
import numpy as np
import pandas as pd
app = xw.App(visible=False, add_book=False)
# wb = app.books.open('E:\温度对下死点精度影响\9-20\9-20日上午8点到下午五点分析图片存放.xlsx')
wb = app.books.open(r'D:\MITCalcSW_64\mitcalc2\chains\chains_01 - 查看代码.xls')
sheet = wb.sheets[0]
wb2 = app.books.open(r'D:\MITCalcSW_64\mitcalc2\chains\公式储存.xlsx')
sheet2 = wb2.sheets[0]
行数=np.linspace(1,212,212)
列=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
   'P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD']
'''列=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
   'P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI'
    ,'AJ','AK','AL','AM','AN','AO',
   'AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL']'''
名称=[]
值=[]
公式=[]
写入位置=1
表=pd.DataFrame()
c = sheet.range('t303').formula
print(c)

print(str(c))
for i in range(len(列)):
    for j in range(len(行数)):
        位置=列[i]+str(int(行数[j]))
        print(列[i]+str(int(行数[j])))
        a = sheet.range(位置).name
        b = sheet.range(位置).value
        c = sheet.range(位置).formula

        try:
            位置写入位置 = 'A' + str(int(写入位置))
            名称写入位置 = 'B' + str(int(写入位置))
            值写入位置 = 'C' + str(int(写入位置))
            公式写入位置 = 'D' + str(int(写入位置))
            写入位置 = 写入位置 + 1
            sheet2.range(位置写入位置).value=位置
            sheet2.range(名称写入位置).value = str(a)
            sheet2.range(值写入位置).value = str(b)
            sheet2.range(公式写入位置).formula = ' '+c
        except Exception as e:
            print(f"处理URL时发生错误: {e}")
            print(位置)
            continue

'''表['名称']=名称
表['值']=值
表['公式']=公式
print(名称)'''
wb2.save()
wb2.close()
app.quit()
app.kill()


