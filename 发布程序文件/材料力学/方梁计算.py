# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:43:26 2022

@author: lizhuang
"""
import sympy 
import numpy as np
import pandas as pd
import sviewgui.sview as sv
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.optimize import root,fsolve
from scipy.integrate import cumtrapz
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
class 方梁弯曲计算():
    def __init__(self):
        self.梁的高度=30#mm
        self.梁的宽度=20
        self.梁的长度=450#mm
        self.均布受力=10#n/mm
        self.梁的弹性模量=2e+11
        self.结果=pd.DataFrame()
    def 内力计算(self):
        fa,fb=sympy.symbols('fa,fb')
        结果=sympy.solve([fb*self.梁的长度-self.均布受力*self.梁的长度*(self.梁的长度/2),self.均布受力*self.梁的长度-fa-fb],[fa,fb])
        res=[]
        for i,j in 结果.items():
           res.append(j)
        fa=np.float64(结果[fa])   
        fb=np.float64(结果[fb])   
        return fa,fb
    def 弯矩(self):
        结果=pd.DataFrame()
        #结果['弯矩']=np.range
        位置=np.linspace(0,self.梁的长度,1000)
        结果['位置']=位置
        弯矩1=[]
        fa=self.内力计算()[0]
        for i in range(len(位置)):
            弯矩=(fa*位置[i]-self.均布受力*(位置[i])*(位置[i]/2))/1000
            弯矩1.append(弯矩)
        结果['弯矩']=弯矩1
        最大弯矩=max(弯矩1)
        print(max(弯矩1))
        弯矩1=np.array(弯矩1)
        位移=位置
        return 最大弯矩,弯矩1,位移,结果
    def 弯矩画图(self):
        DATA = self.弯矩()[3]## Put Your DataFrame Object name here ##  
        #- Axes Setting ---------- 
        fig, ax = plt.subplots()
        ax.set_xlabel( "位置")
        ax.set_ylabel( "弯矩" )
        ax.set_xlim(min(DATA['位置'].replace([np.inf, -np.inf], np.nan ).dropna() ) - abs( min(DATA['位置'].replace([np.inf, -np.inf], np.nan ).dropna() )/10), max(DATA['位置'].replace([np.inf, -np.inf], np.nan).dropna()) + abs(max(DATA['位置'].replace([np.inf, -np.inf], np.nan).dropna())/10)  )
        ax.set_ylim( min(DATA['弯矩'].replace([np.inf, -np.inf], np.nan ).dropna() ) - abs( min(DATA['弯矩'].replace([np.inf, -np.inf], np.nan ).dropna() )/10), max(DATA['弯矩'].replace([np.inf, -np.inf], np.nan).dropna()) + abs(max(DATA['弯矩'].replace([np.inf, -np.inf], np.nan).dropna())/10)  )
        #- PLOT ------------------ 
        ax.scatter(DATA["位置"].replace([np.inf, -np.inf], np.nan), DATA["弯矩"].replace([np.inf, -np.inf], np.nan), s = 5.0, alpha =1.0,edgecolor="black",linewidth= 0.0)
        plt.show() 
        return
    def 中性轴惯性矩(self):
        惯性矩=((self.梁的高度**3)*self.梁的宽度)/12/(1e+12)
        print(惯性矩)
        return 惯性矩
    def 点到中性轴的距离(self):
        y1=self.梁的高度/2/1000
        #y1=(self.梁的高度/2-self.梁的高度/4)/1000
        print(y1)
        return y1
    def 计算应力(self):#pa
        应力1=(self.弯矩()[0]*self.点到中性轴的距离())/self.中性轴惯性矩()
        print(应力1)
        return 应力1
class 圆梁弯曲计算(方梁弯曲计算):
    def __init__(self):
       self.梁的高度=30#mm
       self.梁的长度=450#mm
       self.均布受力=10#n/mm
       self.梁的弹性模量=2e+11
       self.结果=pd.DataFrame() 
    def 中性轴惯性矩(self):
       惯性矩=(self.梁的高度**4)/4/(1e+12)
       print(惯性矩)
       return 惯性矩 
    def 角度导数(self):
       角度导数=(-self.弯矩()[1])/(self.梁的弹性模量*self.中性轴惯性矩())
       return 角度导数
    def 角度(self):
        #角度=self.弯矩()[2]
        #for i in range(len(角度)):
        角度=cumtrapz(self.角度导数(),self.弯矩()[2])
        return 角度
    def 位移(self):
        位移=cumtrapz(self.角度(),self.弯矩()[2])
        return 位移
if __name__=="__main__":
    '''a=方梁弯曲计算()
    z=a.内力计算()
    zz=a.弯矩()
    a.中性轴惯性矩()
    a.计算应力()'''
    b=圆梁弯曲计算()
    b.计算应力()
    zz=b.位移()