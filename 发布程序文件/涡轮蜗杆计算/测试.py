# -*- coding = utf-8 -*-
# @time:2023/10/15 20:47
# Author:lizhuang
# @File:测试.py
# @Software:PyCharm
class test():
    def __init__(self):
        print('Python')
if __name__ == '__main__': 
  test=test()
  import re
  str='_a/IF(S_Units,1,2 5.4)'
  a=re.split(r'[-,*&=/+ )(><^]', str,maxsplit=0)
  print(a)
  def is_number(string):
      pattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$')
      return bool(pattern.match(string))
  索引值='-1'
  if is_number(索引值):
      print('数值')
  c='b1:b2'
  if ':' in c:
      print(1)
  if re.findall(c,':'):
    print('是否含有帽号')

  import xlwings as xw
  import numpy as np
  import pandas as pd

  app = xw.App(visible=False, add_book=False)
  # wb = app.books.open('E:\温度对下死点精度影响\9-20\9-20日上午8点到下午五点分析图片存放.xlsx')
  wb = app.books.open('E:\mitcalc2\gear4\Gear4_01蜗杆查看代码.xls')
  sheet = wb.sheets[0]
  wb2 = app.books.open('E:\mitcalc2\gear4\公式储存.xlsx')
  sheet2 = wb2.sheets[0]
  行数 = np.linspace(1, 428, 428)
  '''列=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
     'P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI'
      ,'AJ','AK','AL','AM','AN','AO',
     'AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ']'''
  列 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
       'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI'
      , 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO',
       'AP']
  名称 = []
  值 = []
  公式 = []
  写入位置 = 1
  表 = pd.DataFrame()
  from math import *

  '''c = sheet.range('AD251').formula
  print(c)
  sheet2.range('D1').formula = ' '+c
  wb2.save()
  wb2.close()'''
  app.quit()
  app.kill()