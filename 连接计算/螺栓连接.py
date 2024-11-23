import numpy as np
import math as mt
class 螺栓连接计算():
    def __init__(self):
        self.qd=98#材料拉深强度
        self.RW=36#螺栓外径
        self.RD=26.211#底部外径
        self.DR=0.438#螺栓谷底的r
        self.thea=60#螺丝牙角度
        self.T0=75000#期初拧紧力矩
        self.F0=3000#轴力
    def 计算应力(self):
        self.P0=self.T0/0.18/self.RW#公式有
        k=1-(self.RD/self.RW)
        k2=self.RD/self.DR
        self.z1=3.9+0.016*self.qd
        self.z2=1-mt.exp(-0.07*self.RD)
        self.z3=1-mt.exp(-0.082*k2)
        self.z4=1-mt.exp(-12*k)
        self.z5=1-mt.exp(-1.7*(np.pi-np.deg2rad(self.thea)))
        self.beta=1+(self.z1*self.z2*self.z3*self.z4*self.z5)#实际疲劳极限比为0.43
        self.thplxu=self.qd*0.43#疲劳极限容许值
        self.yljz=self.thplxu/self.beta#应力集中系数容许
        self.tht0=self.P0/3.14/self.RD**2*4#小于应力集中系数容许
        self.tht=self.F0/3.14/self.RD**2*4#小于应力集中系数容许
        self.thzh=self.tht0+self.tht#小于31
        return
if __name__ == '__main__':
    测试=螺栓连接计算()
    测试.计算应力()