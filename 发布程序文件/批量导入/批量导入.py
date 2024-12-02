# -*- coding: utf-8 -*-
import re
import win32com.client
from os import  listdir,path,rename
#获取文件列表
def 批量更改(filepath):
#filepath=r'C:\Users\Administrator\Desktop\批量导入测试'
#filepath2=r'C:\Users\Administrator\Desktop\批量导出测试'
    filelist=listdir(filepath)
    #print(filelist)
    for i in range(len(filelist)):
        string=filelist[i]
        pathi=filepath+'/'+string
        spstr=string.split()
        mcode=spstr[0]
        try:
          mname=spstr[1]
          tsname = spstr[0] + '#' + mname
          tspathi = filepath + '/' + tsname
          print(tsname)
          # Save the documet
          rename(pathi, tspathi)
        except Exception as err:
          print('第'+str(i+1)+'个文件异常或已处理')
          continue
    print('处理完成请检查处理结果')
    return

#按照位数
import os,shutil,re,glob
'''path =r'文件目录'
file_filter=r"过滤词，如*.jpg之类"
strToReplace="要替换的字符串 "
replace="替换成的字符串"
filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
os.chdir(path)
for temp in glob.glob(file_filter):
    (filename,extension) = os.path.splitext(temp）
    newName=re.sub(strToReplace,replace,filename)+extension
    os.rename(temp,newName)#重命名
print("-----完成-----")'''
import win32com.client

#acad = win32com.client.dynamic.Dispatch("AutoCAD.Application")
#acad.Visible=True
'''    acad.Documents.Open(pathi)
    doc = acad.ActiveDocument
    doc.SaveAs(tspathi)
    ### Adjust dwg ###
    doc.Save()'''
#acad.colse()
#os.chdir(filepath2)
if __name__ == "__main__":
    filepath = r'C:\Users\Administrator\Desktop\批量导入测试'
    批量更改(filepath)