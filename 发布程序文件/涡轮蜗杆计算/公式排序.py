# -*- coding = utf-8 -*-
# @time:2023/10/16 19:35
# Author:lizhuang
# @File:公式排序.py
# @Software:PyCharm
class test():
    def __init__(self):
        print('Python')
if __name__ == '__main__': 
  test=test()
  import xlwings as xw
  import numpy as np
  import pandas as pd
  import re
  app = xw.App(visible=False, add_book=False)
  # wb = app.books.open('E:\温度对下死点精度影响\9-20\9-20日上午8点到下午五点分析图片存放.xlsx')
  wb = app.books.open(r'E:\mitcalc2\gear4\公式储存(1).xlsx')
  sheet = wb.sheets['公式命名分割处理后']
  原数据=sheet.range('A1').options(pd.DataFrame, index=False, numbers=int,expand='table').value
  数据列表池=原数据['分割公式']
  关键字='_a'
  def 赛选包含关键字(原数据=原数据,关键字1=关键字):
      包含关键字公式=原数据[原数据.合并公式.str.match(关键字1, na=False)]
      if len(包含关键字公式)>0:
          包含关键字公式=包含关键字公式.reset_index()
          for i in range(len(包含关键字公式)):
              判断值=re.split(r'[,()/^*+-=<>]' ,str(包含关键字公式.loc[i,'合并公式']))
              print(判断值)
              是否删除='是'
              for ii in range(len(判断值)):
                  if 判断值[ii]==关键字1:
                      是否删除='否'
              print(是否删除)
              if 是否删除=='是':
                  包含关键字公式.drop(index=i,inplace=True)
      return 包含关键字公式
  包含关键字数据=赛选包含关键字(原数据=原数据,关键字1=关键字)
  #开头是关键字= 包含关键字公式[包含关键字公式.再次合并公式.str.startswith(关键字, na=False)]
  app.quit()
  app.kill()
