# -*- coding = utf-8 -*-
# @time:2023/9/1 20:14
# Author:lizhuang
# @File:皮带计算.py
# @Software:PyCharm
from math import *
class 皮带传动():
    def __init__(self):
        print('Python')
        self.p = 10
        self.n1 = 1000
        self.n2 = 500
    def 计算功率(self,ka=1.4):
        self.ka=ka
        self.pca = self.ka * self.p
        return self.pca
if __name__ == '__main__': 
  test=皮带传动()
  #已知条件
  p=10
  n1=1000
  n2=500
  i=n1/n2
  #确定计算功率
  ka=1.4#数据库筛选
  pca=ka*p
  #选择v带带形
  #确定带轮的基准直径并验算带速
  dd1=90#参考表8-6或者8-8
  dd2=i*dd1
  print('参考大带轮直径=',dd2)
  #验算带速
  v1=pi*dd1*n1/(60*1000)
  v2 = pi * dd2 * n2 / (60 * 1000)
  #计算大带轮直径根据图表圆整
  dd22=180
  dd2=dd22
  #确定中心距，选择v带的基准长度
  a00min=0.7*(dd1+dd2)
  a00max=2*(dd1+dd2)
  print('参考中心距',a00min,a00max)
  a00 = 540#初定中心距
  ld0=2*a00+pi/2*(dd1+dd2)+(dd2-dd1)**2/(4*a00)#计算带长
  print('参考带长=',ld0)
  ld=1600#查表选定带长
  a0=a00+(ld-ld0)/2#近视中心距
  print('近视中心距=',a0)
  a0min=a0-0.015*ld
  a0max=a0+0.03*ld
  print('调整中心距范围',a0min,a0max)
  a0=586#调整a0
  alf1=180-(dd2-dd1)*(57.3/a0)#要求大于90度验算带轮包角
  print('压力角为',alf1)
  p0=2.8
  detp0=0.5
  kalf=0.99#包角修正系数
  kl=0.96  #查表长度系数
  z=pca/((p0+detp0)*kalf*kl) #确定v带根数少于10根
  print('推荐带数',z)
  z=5#圆整
  #确定初始拉力
  q=0.12#带的质量
  v=pi*dd1*n1/60/1000
  print('带速v',v)
  f0min=(500*(2.5-kalf)*pca)/(kalf*(z*v))+q*v**2
  print('最小初始拉力',f0min)
  kk=1
  f0=kk*f0min
  #压轴力
  fp=2*z*f0*sin(alf1*pi/180/2)
  print('压轴力',fp)




