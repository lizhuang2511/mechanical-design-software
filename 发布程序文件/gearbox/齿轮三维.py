# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:54:07 2024

@author: Administrator
"""
'''[SpurGear_betanotzero_Wheel_mm]
1=MC_db2;D1@Sketch1#齿根圆
2=MC_b2;D1@Base-Extrude#齿厚
3=MC_d2;D1@Sketch2#分度圆
4=MC_da2;D2@Sketch2#齿顶圆
5=MC_sa2;D3@Sketch2#齿顶长
6=MC_s2;D4@Sketch2齿根长
7=MC_sb2;D5@Sketch2分度圆长
8=MC_z2;D1@CirPattern1齿数
9=MC_aw;D1@Plane1#中心距
10=MC_Pitch2;D4@Helix1#螺旋角螺距
MC_Pitch2=1000000000;99999'''
import win32com.client
import os
from pathlib import Path
import os

# 获取当前文件的绝对路径
current_path = os.path.abspath(__file__)

# 获取当前文件的上一级目录
parent_path = os.path.dirname(current_path)

# 获取上一级目录的上一级目录
grandparent_path = os.path.dirname(parent_path)

print("当前文件的绝对路径:", current_path)
print("上一级目录:", parent_path)
print("上上一级目录:", grandparent_path)

path=os.getcwd()

path1=grandparent_path+'\数据文件\spurgear_betanotzero_wheel_mm.SLDPRT'
path2=grandparent_path+'\数据文件\gearrack_betaeqzero_pinion_mm.sldprt'

import win32com.client
import pythoncom
import sys
sys.path.append("../数据文件")
from swconst import constants
def opendoc(path=path1,D1Sketch1=0.0678,
            D1BaseExtrude=0.034,
            D1Sketch2=0.07609,
            D2Sketch2=0.09078,
            D3Sketch2=0.00189,
            D4Sketch2=0.0056,
            D5Sketch2=0.00559,
            D1CirPattern1=13,
            D1Plane1=0.06898,
            D4Helix1=0.65676,
            banben=2022):
    # SolidWorks年份版本
    sldver = banben
    # 建立com连接,如只有一个版本,可以只写"SldWorks.Application"
    swApp = win32com.client.Dispatch(f'SldWorks.Application.{sldver - 1992}')
    # 提升API交互效率
    swApp.CommandInProgress = True
    # 显示SolidWorks界面
    swApp.Visible = True
    # 打开文件
    Errors = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, -1)
    Warnings = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, -1)
    Part=swApp.OpenDoc6(path, 1, 1, "", Errors, Warnings)
    Part.GetMassProperties2(-1)
    AssemblyDoc = swApp.ActiveDoc
    #a = AssemblyDoc.GetMassProperties2()
    #print(a)
    # Define both dimensions
    dim1 = AssemblyDoc.Parameter("D1@Sketch1")
    dim2 = AssemblyDoc.Parameter("D1@Base-Extrude")
    dim3 = AssemblyDoc.Parameter("D1@Sketch2")
    dim4 = AssemblyDoc.Parameter("D2@Sketch2")
    dim5 = AssemblyDoc.Parameter("D3@Sketch2")
    dim6 = AssemblyDoc.Parameter("D4@Sketch2")
    dim7 = AssemblyDoc.Parameter("D5@Sketch2")
    dim8= AssemblyDoc.Parameter("D1@CirPattern1")
    dim9= AssemblyDoc.Parameter("D1@Plane1")
    dim10 = AssemblyDoc.Parameter("D4@Helix1")
    print(dim1.SystemValue)
    #dim2 = AssemblyDoc.Parameter("data@Sketch1@Part2.Part")
    # Setting new value for dimensions
    dim1.SystemValue = D1Sketch1
    dim2.SystemValue = D1BaseExtrude
    dim3.SystemValue = D1Sketch2
    dim4.SystemValue = D2Sketch2
    dim5.SystemValue = D3Sketch2
    dim6.SystemValue = D4Sketch2
    dim7.SystemValue = D5Sketch2
    dim8.SystemValue= D1CirPattern1
    dim9.SystemValue= D1Plane1
    dim10.SystemValue = D4Helix1
    # 获取模型文档对象  
    # 执行重建操作  
    #AssemblyDoc.EditRebuild3()
    #bool=AssemblyDoc.EditRebuild3()      
    # 可选：保存零件文件（如果需要的话）  
    #a=AssemblyDoc.Save3(1, int(1), int(1))  
    boolstatus = AssemblyDoc.Save3(constants.swSaveAsOptions_Silent, Errors, Warnings)
    if boolstatus:
        print('文件保存成功')
    else:
        print(f'文件保存失败,出现如下错误：{Errors}')
        print(f'文件保存失败,出现如下警告：{Warnings}')
    return
''''[gearrack_betaeqzero_Pinion_mm]
1=MC_db1;D1@Sketch1
2=MC_b1;D1@Base-Extrude
3=MC_d1;D1@Sketch2
4=MC_da1;D2@Sketch2
5=MC_sa1;D3@Sketch2
6=MC_s1;D4@Sketch2
7=MC_sb1;D5@Sketch2
8=MC_z1;D1@CirPattern1
9=MC_aw;D1@Plane1'''
def opendoczhichi(path=path2,D1Sketch1=0.0678,
            D1BaseExtrude=0.034,
            D1Sketch2=0.07609,
            D2Sketch2=0.09078,
            D3Sketch2=0.00189,
            D4Sketch2=0.0056,
            D5Sketch2=0.00559,
            D1CirPattern1=13,
            D1Plane1=0.06898,
            banben=2022):
    # SolidWorks年份版本
    sldver = banben
    # 建立com连接,如只有一个版本,可以只写"SldWorks.Application"
    swApp = win32com.client.Dispatch(f'SldWorks.Application.{sldver - 1992}')
    # 提升API交互效率
    swApp.CommandInProgress = True
    # 显示SolidWorks界面
    swApp.Visible = True
    # 打开文件
    Errors = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, -1)
    Warnings = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, -1)
    Part=swApp.OpenDoc6(path, 1, 1, "", Errors, Warnings)
    AssemblyDoc = swApp.ActiveDoc
    # Define both dimensions
    dim1 = AssemblyDoc.Parameter("D1@Sketch1")
    dim2 = AssemblyDoc.Parameter("D1@Base-Extrude")
    dim3 = AssemblyDoc.Parameter("D1@Sketch2")
    dim4 = AssemblyDoc.Parameter("D2@Sketch2")
    dim5 = AssemblyDoc.Parameter("D3@Sketch2")
    dim6 = AssemblyDoc.Parameter("D4@Sketch2")
    dim7 = AssemblyDoc.Parameter("D5@Sketch2")
    dim8= AssemblyDoc.Parameter("D1@CirPattern1")
    dim9= AssemblyDoc.Parameter("D1@Plane1")

    print(dim1.SystemValue)
    #dim2 = AssemblyDoc.Parameter("data@Sketch1@Part2.Part")
    # Setting new value for dimensions
    dim1.SystemValue = D1Sketch1
    dim2.SystemValue = D1BaseExtrude
    dim3.SystemValue = D1Sketch2
    dim4.SystemValue = D2Sketch2
    dim5.SystemValue = D3Sketch2
    dim6.SystemValue = D4Sketch2
    dim7.SystemValue = D5Sketch2
    dim8.SystemValue= D1CirPattern1
    dim9.SystemValue= D1Plane1
    # 获取模型文档对象
    # 执行重建操作
    #AssemblyDoc.EditRebuild3()
    #bool=AssemblyDoc.EditRebuild3()
    # 可选：保存零件文件（如果需要的话）
    #a=AssemblyDoc.Save3(1, int(1), int(1))
    boolstatus = AssemblyDoc.Save3(constants.swSaveAsOptions_Silent, Errors, Warnings)
    if boolstatus:
        print('文件保存成功')
    else:
        print(f'文件保存失败,出现如下错误：{Errors}')
        print(f'文件保存失败,出现如下警告：{Warnings}')
    return


if __name__ == '__main__':
    swApp = opendoc(path=path1,D1Sketch1 = 0.0678,
                D1BaseExtrude=0.034,
                D1Sketch2=0.07609,
                D2Sketch2=0.09078,
                D3Sketch2=0.00189,
                D4Sketch2=0.0056,
                D5Sketch2=0.00559,
                D1CirPattern1=18,
                D1Plane1=0.06898,
                D4Helix1=3.14,)
# Define Assembly as active document
'''AssemblyDoc = sw.ActiveDoc

# Define both dimensions
dim1 = AssemblyDoc.Parameter("D1@Sketch1")
#dim2 = AssemblyDoc.Parameter("data@Sketch1@Part2.Part")

# Setting new value for dimensions
new_value = 0.0678
dim1.SystemValue = new_value'''


