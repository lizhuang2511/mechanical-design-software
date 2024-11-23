# -*- coding = utf-8 -*-
# @time:2023/10/20 16:16
# Author:lizhuang
# @File:excel公式python版本.py
# @Software:PyCharm
import pandas as pd
from math import *
import sqlite3
import matplotlib
#matplotlib.use('TkAgg')  # 或者尝试其他后端，如 'Agg', 'GTK3Agg' 等
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
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


import numpy as np
import scipy

def CAprox(InputList, ReqVal):
    # Split the input string by semicolon
    values = InputList.split(';')

    # Convert the string values to floats
    values = [float(v) for v in values if v]  # Remove empty strings

    # Determine the midpoint of the values list
    #mid = len(values) // 2
    X=[]
    y=[]
    for i in range(len(values)):
        # Split the values into X and y arrays
        if i % 2 == 0:#偶数
            X.append(values[i])
        else:
            y.append(values[i])

        # Call the Linear function (not provided, so we'll assume it exists)
    # Note: In Python, the function call would typically look like this:
    # result = Linear(some_arguments)
    # But since we don't have the Linear function, we'll just return a placeholder value
    # You should replace this with the actual Linear function call once you have it
    # 使用numpy的polyfit函数进行线性拟合，得到线性方程的系数
    coefficients = np.polyfit(X, y, 3)

    # 输出线性方程的系数
    print('Coefficients:', coefficients)

    # 使用得到的系数生成拟合线
    polynomial = np.poly1d(coefficients)
    y_fit = polynomial(ReqVal)
    return y_fit

import numpy as np
from scipy.interpolate import interp1d


def lagrange_interpolation(x_values, y_values, x_new):
    # 拉格朗日插值实现
    def lagrange_polynomial(x, xi, yi):
        product = 1
        for i in range(len(xi)):
            if xi[i] != xi[xi.index(xi[i]) - 1]:  # 避免除以零和重复项
                product *= (x - xi[i]) / (xi[xi.index(xi[i]) - 1] - xi[i])
        return product * yi[xi.index(xi[i]) - 1]

    total = 0
    for i in range(len(x_values)):
        total += lagrange_polynomial(x_new, np.delete(x_values, i), np.delete(y_values, i))
    return total


def table_approximation(table_values, xval, yval, approx_type):
    # Extract x and y values, assuming table_values has headers
    x_values = table_values[1:, 0].astype(float)
    y_values = table_values[0, 1:].astype(float)
    table_data = table_values[1:, 1:].astype(float)

    # Check if xval and yval are within the interpolation range
    if xval < x_values.min() or xval > x_values.max():
        raise ValueError(
            f"xval {xval} is outside the interpolation range for x_values ({x_values.min()} to {x_values.max()}).")
    if yval < y_values.min() or yval > y_values.max():
        raise ValueError(
            f"yval {yval} is outside the interpolation range for y_values ({y_values.min()} to {y_values.max()}).")

        # Interpolate in the X direction
    x_interpolated_values = []
    for row in table_data:
        if approx_type[:2] == "LI":
            x_interpolated_values.append(interp1d(x_values, row, kind='linear')(xval))
        else:
            x_interpolated_values.append(lagrange_interpolation(x_values, row, xval))

    x_interpolated_values = np.array(x_interpolated_values)

    # Interpolate in the Y direction
    if approx_type[2:] == "LI":
        result = interp1d(y_values, x_interpolated_values, kind='linear')(yval)
    else:
        result = lagrange_interpolation(y_values, x_interpolated_values, yval)

    return result
def INDIRECT(表,行,列):
    return 5
def PulleyMass(Dout, Dshaft, Width, Thick, Density):
    d1 = Dshaft + 2 * Thick
    d2 = Dout - 2 * Thick
    if Thick > Width:
        Thick = Width
    volume = (Dout ** 2) / 4 * math.pi * Width
    if d1 < d2:
        volume -= (d2 ** 2) / 4 * math.pi * (Width - Thick)
        volume += (d1 ** 2) / 4 * math.pi * (Width - Thick)
    if Dshaft < 0.5 * Dout:
        volume -= (Dshaft ** 2) / 4 * math.pi * Width
    return volume * Density
def ODD(n):
    return n % 2 != 0


import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


def linear_interp(x_values, y_values, xval):
    # Simple linear interpolation between two points
    if x_values[0] == xval:
        return y_values[0]
    elif x_values[-1] == xval:
        return y_values[-1]
    else:
        for i in range(len(x_values) - 1):
            if x_values[i] <= xval <= x_values[i + 1]:
                slope = (y_values[i + 1] - y_values[i]) / (x_values[i + 1] - x_values[i])
                return y_values[i] + slope * (xval - x_values[i])
    raise ValueError("xval is out of bounds")

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
#matplotlib.use('TkAgg')  # 或者尝试其他后端，如 'Agg', 'GTK3Agg' 等
import matplotlib.pyplot as plt
# 输入数据（行名和列名的值）
def yuce(xxx,yyy):
    x_data = np.array([11, 13, 15, 17, 19, 21, 23, 25, 100])
    y_data = np.array([0, 0.1, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2])
    z_data = np.array([
        [31.29, 31.29, 31.29, 31.78, 31.98, 32.47, 32.47, 32.86, 32.86],
        [31.29, 31.29, 31.29, 31.78, 31.98, 32.47, 32.47, 32.86, 32.86],
        [27.96, 30.02, 30.21, 30.41, 30.41, 31, 31.49, 31.89, 31.89],
        [25.9, 27.57, 28.45, 28.94, 29.33, 29.63, 29.92, 30.51, 30.51],
        [24.13, 26.09, 27.08, 27.76, 28.15, 28.45, 29.04, 29.72, 29.72],
        [22.46, 24.53, 25.7, 26.59, 27.08, 27.57, 27.96, 28.55, 28.55],
        [21.29, 23.35, 24.72, 25.6, 26.39, 26.78, 27.46, 27.96, 27.96],
        [18.64, 21.19, 22.76, 24.03, 24.62, 25.21, 25.8, 26.19, 26.19],
        [16.68, 19.33, 21.09, 22.17, 23.35, 23.94, 24.53, 25.11, 25.11]
    ])
    # 将输入数据转换成适合curve_fit的形式（需要是一维数组）
    x_flat = x_data.repeat(len(y_data))
    y_flat = np.tile(y_data, len(x_data))
    z_flat = z_data.flatten()


    # 定义要拟合的二元函数形式（这里以二次多项式为例）
    def func(variables, a, b, c, d, e, f):
        x, y = variables
        return a + b * x + c * y + d * x ** 2 + e * y ** 2 + f * x * y


    # 使用curve_fit进行拟合
    popt, pcov = curve_fit(func, np.vstack((x_flat, y_flat)), z_flat)

    # 输出拟合参数
    print("拟合参数:", popt)


    # 使用拟合函数预测新的数据点
    def predict(x_new, y_new, popt):
        return func((x_new, y_new), *popt)

    zhi = predict(xxx, yyy, popt)

    return zhi
import openpyxl
import numpy as np
def monik8(x, y,):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from scipy.optimize import curve_fit

    # 假设的拟合函数（这只是一个例子，实际上你需要根据你的数据来定义这个函数）
    def fitted_func(variables, a, b, c):
        x, y = variables
        return a * x + b * y + c  # 这是一个线性函数，仅作为示例

    # 输入数据（这里只是示例数据，你应该使用你自己的数据）
    row_values = np.array([1, 2, 3, 4])
    column_values = np.array([20, 40, 60, 80])
    table_values = np.array([
        [0.69, 0.8, 0.9, 1.0],
        [0.83, 0.95, 1.07, 1.19],
        [1.00, 1.14, 1.28, 1.42],
        [1.20, 1.36, 1.52, 1.68]
    ])

    # 将二维数据展平为一维，以便与curve_fit一起使用
    x_flat = row_values.repeat(column_values.size)
    y_flat = np.tile(column_values, row_values.size)
    z_flat = table_values.flatten()

    # 使用curve_fit进行拟合（注意：这里的拟合函数和参数只是示例，并不适用于上述数据）
    # 你需要根据你的数据调整拟合函数和初始参数猜测
    popt, pcov = curve_fit(fitted_func, np.vstack((x_flat, y_flat)), z_flat, p0=[0, 0, 0])
    zhi=fitted_func((x,y), *popt)  # 使用拟合的参数计算z值
    return zhi
def nihedongtai(xxx,yyy):
    x_values = np.array([9.52, 15.87, 25.4, 38.1, 50.8, 63.5, 88.9])
    y_values = np.array([1,
                         4,
                         10,
                         50,
                         100,
                         400,
                         1000,
                         2000,
                         3000,
                         4000,
                         ])
    z_values = np.array(
        [[7.61, 7.69, 7.87, 8.19, 8.7, 9.24, 10.71],
         [8.73, 8.83, 9.04, 9.4, 9.99, 10.61, 12.3],
         [9.58, 9.68, 9.91, 10.31, 10.95, 11.64, 13.49],
         [11.25, 11.37, 11.64, 12.11, 12.86, 13.67, 15.84],
         [12.05, 12.18, 12.47, 12.98, 13.79, 14.65, 16.98],
         [13.84, 13.99, 14.32, 14.91, 15.83, 16.82, 18],  # 注意这里的18值可能需要处理
         [15.18, 15.34, 15.7, 16.35, 18, 18, 18],  # 同上
         [16.26, 16.44, 16.83, 18, 18, 18, 18],  # 同上
         [16.94, 17.12, 18, 18, 18, 18, 18],  # 同上
         [17.43, 17.62, 18, 18, 18, 18, 18]]
    )
    #print(z_values)
    # 创建插值函数
    interp_func = interp2d(x_values, y_values, z_values, kind='cubic')

    # 现在你可以使用这个函数来插值任意的(x, y)点
    # 例如，插值点(0.5, 0.5)
    x_new = xxx
    y_new = yyy
    z_new = interp_func(x_new, y_new)


    return z_new
def nihejingtai(xxx,yyy):

    x_data = np.array([6,	25.4,	50	,1000
])
    y_data = np.array([0,
5,
10,
30,
])
    z_data = np.array([
        [12	,10,	9,	8

],
        [20,	15,	10	,10

],
        [30	,20	,20,	20
],
        [40	,30,	30	,30
],

    ])
    # 将输入数据转换成适合curve_fit的形式（需要是一维数组）
    interp_func = interp2d(x_data, y_data, z_data, kind='linear')

    # 现在你可以使用这个函数来插值任意的(x, y)点
    # 例如，插值点(0.5, 0.5)
    x_new = xxx
    y_new = yyy
    z_new = interp_func(x_new, y_new)
    return z_new
def nihemoca(xxx,yyy):

    x_data = np.array([1,2,3	,5,7
])
    y_data = np.array([20,
40,
80,
160,
])
    z_data = np.array([
        [0.69	,0.8	,0.87	,0.98,	1.04


],
        [0.83,	0.93,	1	,1.09	,1.15


],
        [1	,1.12,	1.19	,1.27,	1.32

],
        [1.24,	1.38,	1.45,	1.53,	1.57

],

    ])
    # 将输入数据转换成适合curve_fit的形式（需要是一维数组）
    interp_func = interp2d(x_data, y_data, z_data,kind='cubic')

    # 现在你可以使用这个函数来插值任意的(x, y)点
    # 例如，插值点(0.5, 0.5)
    x_new = xxx
    y_new = yyy
    z_new = interp_func(x_new, y_new)
    return z_new

if __name__ == '__main__':
    '''T_Results='T_Results'
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
    print(dd)'''
    # 示例用法
    # 假设我们有一个二维numpy数组作为输入表格
    '''table_values = np.array([
        [0, 1, 2, 3],
        [0, 1, 4, 9],
        [0, 2, 5, 12],
        [0, 3, 6, 15]
    ])

    xval = 1.5
    yval = 1.5
    approx_type = "LILI"  # 使用线性插值在X和Y方向上
    result = table_approximation(table_values, xval, yval, approx_type)
    print(result)'''
    _i_1=5
    _K2_prop = CAprox('1;1.25; 2; 1.1; 3; 1; 5; 0.9; 7; 0.85; 12; 0.8; 100; 0.75', _i_1)
    print(_i_1)
    _C_Pitch=4.8
    _K4_prop = CAprox('20;1.2;40;1;60;0.9;80;0.85;160;0.7;1000;0.7', _C_Pitch)
    print(_K4_prop )