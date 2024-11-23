# -*- coding = utf-8 -*-
# @time:2023/10/20 16:16
# Author:lizhuang
# @File:excel公式python版本.py
# @Software:PyCharm
import pandas as pd
from math import *
import sqlite3
def Atan(a):
    a=atan(a)
    return a
def read_table_to_dataframe(database_file, table_name):
    # 连接到数据库
    conn = sqlite3.connect(database_file)

    # 读取数据库中的数据表到 DataFrame
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)

    # 关闭数据库连接
    conn.close()

    return df
def CellTransmitVal(计算值,输入值,判断值):#如果有输入选择输入值，如果没有输入选择没有输入的值
    if 判断值==True:
        输出=输入值
    else:
        输出 = 计算值
    return 输出
def IF(condition, true_value, false_value):
    if condition:
        return true_value
    else:
        return false_value
def INDEX(表名,行,列):
    文件路径='../螺纹传动/luowenchuandong.xlsx'
    数据=pd.read_excel(open(文件路径,'rb'),sheet_name=表名)
    #数据 = read_table_to_dataframe('../涡轮蜗杆计算/wilumwogan.db', 表名)
    #列=str(列)
    print(列)
    #行=str(str(行)+'.0')
    #行 = str(str(行))
    print(行)
    赛选数据=数据.loc[数据.行号 == 行, 列]
    print(赛选数据)
    #赛选数据.reset_index()
    #print(type(赛选数据))
    #列=str(列)
    数 = 赛选数据.values[0]
    if type(数)==str:
        值 = 赛选数据.values[0]
    else:
        值=float(赛选数据.values[0])
    #值 = 赛选数据.values[0]
    return 值
def INDEX2(表名,行,列):
    文件路径='../螺纹传动/luowenchuandong.xlsx'
    数据=pd.read_excel(open(文件路径,'rb'),sheet_name=表名)
    #数据 = read_table_to_dataframe('../涡轮蜗杆计算/wilumwogan.db', 表名)
    列=str(列)
    print(列)
    行=str(str(行)+'.0')
    print(行)
    赛选数据=数据.loc[数据.行号 == 行, 列]
    print(赛选数据)
    #赛选数据.reset_index()
    #print(type(赛选数据))
    #列=str(列)
    数=赛选数据.values[0]
    值=赛选数据.values[0]
    #值 = 赛选数据.values[0]
    return 值
def CHOOSE(a,b,c,d,e=1):
    a=int(a)
    biao=[b,c,d,e]
    zhi=biao[a-1]
    return zhi
def OR(a,b):
    if a==False and b==False:
        值=False
    else:
        值=True
    return 值
def AND(a,b):
    if a==True and b==True:
        值=True
    else:
        值=False
    return 值
def LN(a):
    值=log(a)
    return 值
def LOG(a):
    值=log10(a)
    return 值
def ROUND(a,b):
    值=round(a,b)
    return 值
def T_Lubrication(_vgm=1,_KW=1,行号=1,列号=4):
    print(_vgm,_KW,type(_vgm),type(_KW))
    list=[[min(0.028+0.026*1/(_vgm+0.17)**0.76,0.1),	min(0.055+0.015*1/(_vgm+0.2)**0.87,0.1),	min(0.000000000024*_KW**-3.1,0.0000004),	min(0.00000000545*_KW**-1.23,0.0000004),	min(0.00000000009*_KW**-3.7,0.0000004),	0.028+0.026*1/(_vgm+0.17)**0.76,	0.055+0.015*1/(_vgm+0.2)**0.87],
        [min(0.026+0.017*1/(_vgm+0.17)**0.92,0.096),	min(0.055+0.015*1/(_vgm+0.2)**0.87,0.1),	0.000000000318*_KW**-2.24,	0.0000000166*_KW**-1.17,	min(0.00000000009*_KW**-3.7,0.0000004),	0.026+0.017*1/(_vgm+0.17)**0.92,	0.055+0.015*1/(_vgm+0.2)**0.87],
        [min(0.02+0.02*1/(_vgm+0.2)**0.97,0.094),	min(0.034+0.015*1/(_vgm+0.19)**0.97,0.1),	0.000000000127*_KW**-2.24,	0.0000000166*_KW**-1.17,	0.000000000058*_KW**-1.58,	0.02+0.02*1/(_vgm+0.2)**0.97,	0.034+0.015*1/(_vgm+0.19)**0.97],
        [min(0.033+0.079*1/(_vgm+0.2)**1.55,0.1),	min(0.055+0.015*1/(_vgm+0.2)**0.87,0.1),	min(0.000000000065*_KW**-2.68,0.0000004),	min(0.00000000545*_KW**-1.23,0.0000004),	min(0.00000000009*_KW**-3.7,0.0000004),	0.033+0.079*1/(_vgm+0.2)**1.55,	0.055+0.015*1/(_vgm+0.2)**0.87],
        [min(0.027+0.0056*1/(_vgm+0.15)**1.63,0.096),	min(0.055+0.015*1/(_vgm+0.2)**0.87,0.1),	0.000000000558*_KW**-1.91,	0.0000000166*_KW**-1.17,	min(0.00000000009*_KW**-3.7,0.0000004),	0.027+0.0056*1/(_vgm+0.15)**1.63,	0.055+0.015*1/(_vgm+0.2)**0.87],
        [min(0.024+0.0032*1/(_vgm+0.1)**1.71,0.094),	min(0.034+0.015*1/(_vgm+0.19)**0.97,0.1),	0.000000000223*_KW**-1.91,	0.0000000166*_KW**-1.17,	0.000000000058*_KW**-1.58,	0.024+0.0032*1/(_vgm+0.1)**1.71,	0.034+0.015*1/(_vgm+0.19)**0.97]]
    行号=行号-1;列号=列号-4
    值=list[行号][列号]
    return 值
def convert_to_dms(degrees):
    degrees=float(degrees)
    deg=int(degrees)
    minutes=(degrees-deg)*60
    min_int=int(minutes)
    seconds=(minutes-min_int)*60
    return f"{deg}°{min_int}'{seconds:.2f}\""
def dms2dd(degrees, minutes, seconds):
   dd = degrees + float(minutes)/60 + float(seconds)/3600
   return dd

def vlookup(值,表,列):
    文件路径 = '../螺纹传动/luowenchuandong.xlsx'
    数据 = pd.read_excel(open(文件路径, 'rb'), sheet_name=表)
    赛选数据 = 数据.loc[数据['v'] == 值, 列]
    值 = 赛选数据.values[0]
    return 值
import math
def vlookup4(值,表,列):
    文件路径 = '../螺纹传动/luowenchuandong.xlsx'
    数据 = pd.read_excel(open(文件路径, 'rb'), sheet_name=表)
    数据=数据.loc[1:,:]
    数据['差值']=abs(数据['v']-float(值))
    print(type(数据['差值']))
    minhang=min(数据['差值'])
    赛选数据 = 数据.loc[数据['差值']==minhang, 列]
    值 = 赛选数据.values[0]
    return 值

def Pmax_SecFormula(SR, Eta, Sy, AA, EE):
    if SR < 0.00001:
        SR = 0.00001
    if Eta < 0.0001:
        Eta = 0.0001

    S1 = EE * (3.1416 / SR) ** 2
    if S1 > Sy:
        S1 = Sy

    if Eta < 1:
        pom = 1
    else:
        pom = Eta

    S1 = S1 / pom / 3
    P = S1 * AA
    dP = P / 3

    for i in range(1, 41):
        S1 = P / AA * (1 + Eta * (1 / math.cos(SR / 2 * (P / (EE * AA)) ** 0.5)))
        if S1 > Sy:
            P -= dP
            dP /= 2
            P += dP
        else:
            if S1 < 0:
                P -= dP
                dP /= 2
                P += dP
            else:
                P += dP

    return P


import math


def Smax_SecFormula(SR, Eta, Sy, AA, EE):
    if SR < 0.00001:
        SR = 0.00001
    if Eta < 0.0001:
        Eta = 0.0001

    S1 = EE * (3.1416 / SR) ** 2
    if S1 > Sy:
        S1 = Sy

    if Eta < 1:
        pom = 1
    else:
        pom = Eta

    S1 = S1 / pom / 3
    P = S1 * AA
    dP = P / 3

    for i in range(1, 31):
        S1 = P / AA * (1 + Eta * (1 / math.cos(SR / 2 * (P / (EE * AA)) ** 0.5)))
        if S1 > Sy:
            P -= dP
            dP /= 2
            P += dP
        else:
            if S1 < 0:
                P -= dP
                dP /= 2
                P += dP
            else:
                P += dP

    return P / AA
if __name__ == '__main__':
    T_Results='T_Results'
    _Results=5
    a=INDEX(T_Results, _Results, 6)
    T_MatTblWorm='T_MatTblWorm'
    _MatP=6
    _VHV1 = INDEX(T_MatTblWorm, _MatP, 58)  # 齿的边缘硬度VHV[HV]
    print(a)
    print(_VHV1)
    print(LN(5))
    print(LOG(5))
    print(ROUND(5.2,1))
    d = 120
    m = 30
    s = 45
    dd = dms2dd(d, m, s)
    print(dd)