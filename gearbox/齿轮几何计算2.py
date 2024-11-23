# -*- coding = utf-8 -*-
# @time:2024/8/13 11:15
# Author:lizhuang
# @File:齿轮几何计算.py
# @Software:PyCharm
from math import *
import numpy as np
def 计算k( 螺旋角=15, 压力角=20, z=130, xn=0, 模数=14):
    压力角 = np.deg2rad(压力角)
    螺旋角 = np.deg2rad(螺旋角)
    at = np.arctan(np.tan(压力角) / np.cos(螺旋角))
    betb = np.arccos(np.cos(螺旋角) * np.cos(压力角) / np.cos(at))
    zv = z / (np.cos(betb) ** 2 * np.cos(螺旋角))
    # zv = z / (np.cos(螺旋角) ** 2 * np.cos(螺旋角))
    anh = 压力角
    bath = 螺旋角
    invan = tan(anh) - anh;
    # 计算跨齿数和公法线长度
    ath = atan(tan(anh) / cos(bath));
    invan = tan(anh) - anh;
    invat = tan(ath) - ath;
    zp = z * invat / invan;
    if xn == 0:
        k = round(压力角 / np.pi * zp + 0.5)
    else:
        k = round(zv / np.pi * np.arccos(zv * np.cos(压力角) / (zv + 2 * xn)) + 0.5)
    Mn = 模数
    wxx = cos(anh) * (pi * (k - 0.5) + zp * invan);
    detw = sin(anh) * 2 * xn
    Wkn = Mn * (wxx + detw)
    print('跨齿数', k, '公法线', Wkn)
    return k, Wkn


def 最小侧间隙计算(中心距=1050.8, 模数=14, 压力角=20, 中心距偏差=-0.05, jn=0, Ebns1u=0.05, Ebns1d=0.05, Ebns2u=0.05, Ebns2d=0.05):
    压力角 = np.deg2rad(压力角)
    # jbmin=abs(-2/3*(0.06+0.0005*abs(中心距)+0.03*模数)-中心距偏差*2*np.tan(压力角)*np.cos(压力角)+jn)
    jbmin = abs(-2 / 3 * (0.06 + 0.0005 * abs(中心距) + 0.03 * 模数))
    Esns1u = Ebns1u / cos(压力角)#上偏差
    Esns2u = Ebns2u / cos(压力角)
    Esns1d = Ebns1d / cos(压力角)
    Esns2d = Ebns2d / cos(压力角)
    tsn1 = Esns1d - Esns1u
    tsn2 = Esns2d - Esns2u
    jbn = abs(Esns1u + Esns2u) * cos(压力角)#间隙小原始
    jbnmax = abs(Esns1u + Esns2u) * cos(压力角) + 中心距偏差 * 2 * np.tan(压力角) * np.cos(压力角) - jn
    print(jbmin, jbn, jbnmax, tsn1, tsn2)
    return jbmin, jbn, jbnmax, tsn1, tsn2