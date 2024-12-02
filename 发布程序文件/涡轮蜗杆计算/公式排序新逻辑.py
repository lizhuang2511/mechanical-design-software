# -*- coding = utf-8 -*-
# @time:2023/10/17 7:57
# Author:lizhuang
# @File:公式排序新逻辑.py
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
  def is_number(string):
      pattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$')
      return bool(pattern.match(string))
  app = xw.App(visible=False, add_book=False)
  # wb = app.books.open('E:\温度对下死点精度影响\9-20\9-20日上午8点到下午五点分析图片存放.xlsx')
  wb = app.books.open(r'E:\mitcalc2\gear4\公式储存.xlsx')
  sheet = wb.sheets['和并表']
  #sheet = wb.sheets['数值合并测试']
  原数据 = sheet.range('A1').options(pd.DataFrame, index=False, numbers=int, expand='table').value
  压入表=原数据.loc[原数据['合并公式']=='变量值',:].reset_index()
  公式表 = 原数据.loc[原数据['合并公式'] != '变量值', :].reset_index()
  def 压入一次(公式表=公式表,压入表=压入表, 压入数量=0,无法压入数量=0):
      不可执行=[]
      for i in range(len(公式表)):
        压入值=公式表.iloc[i,:]
        公式=str(公式表.loc[i, '合并公式'])
        判断值 =re.split(r'[-,*&=/+ )(><^]', 公式,maxsplit=0)
        分割公式=str(公式表.loc[i, '分割公式'])
        print('分割公式',分割公式)
        print(判断值)
        for ii in range(len(判断值)):
          公式是否可行='是'
          索引值=判断值[ii]
          #print(索引值)
          if is_number(索引值):
            #print('数值')
            continue
          elif 索引值=='':
            #print('空')
            continue
          elif ':' in 索引值:
            #print('空')
            continue
          elif '_ToothType' in 索引值:
            if 索引值==分割公式:
                break
            else:
                #continue
                break#相互印证无法处理
          elif 'INDEX' in 索引值:
            #print('空')
            break
          elif 'XM' in 索引值:
            #print('空')
            break
          else:
            寻找变量=压入表.loc[压入表['分割公式'] == str(索引值), :]
            #print(寻找变量)
            判断压入表是否存在=len(寻找变量)
            if 判断压入表是否存在>0:
              公式是否可行 = '是'
            else:
              print('不可压入公式',公式)
              print('不可行原因',索引值)
              不可执行.append(索引值)
              公式是否可行 = '否'
              break
        if 公式是否可行 == '是':
           print('压入')
           压入值 = 压入值.to_frame()
           压入值 = pd.DataFrame(压入值.values.T, index=压入值.columns, columns=压入值.index)
           压入表=pd.concat([压入表,压入值],axis=0,ignore_index=False)
           压入数量=压入数量+1
           #print(str(公式))
        else:
           print('公式不可行')
           无法压入数量=无法压入数量+1
           #print(str(公式))
      公式表处理=pd.merge(公式表,压入表,how='left',on=['分割公式'])
      公式表处理=公式表处理.fillna('WU')
      公式表处理=公式表处理.loc[公式表处理['合并公式_y']=='WU', :]
      公式表处理.rename(columns={'index_x':'index','合并公式_x':'合并公式','再次合并公式_x':'再次合并公式'},inplace=True)
      公式表=公式表处理.reindex(['分割公式','合并公式','再次合并公式'],axis='columns')
      公式表=公式表.reset_index()
      print('压入', 压入数量)
      print('无法压入数量', 无法压入数量)
      print(不可执行)
      return  公式表,压入表
  压入循环=50
  结果 = 压入一次(公式表=公式表, 压入表=压入表)
  for i in range(压入循环):
      结果 = 压入一次(公式表=结果[0], 压入表=结果[1])
  压入表=结果[1]
  公式表=结果[0]
  压入表.to_excel(r'E:\mitcalc2\gear4\写入python压入表.xlsx')
  公式表.to_excel(r'E:\mitcalc2\gear4\写入python公式表.xlsx')
  app.quit()
  app.kill()