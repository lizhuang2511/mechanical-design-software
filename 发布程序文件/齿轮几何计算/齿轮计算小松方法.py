import numpy as np
import pandas as pd
from 齿轮几何计算 import 齿轮精度计算
class 齿轮主参数计算(齿轮精度计算):
    def __init__(self):
        self.z2 = 21
        self.z1 = 100
        self.m = 12
        self.x1=0.5
        self.x2=0
        self.alf = 20
        self.au = 0.05;
        self.ai = 0;
        self.大齿轮行程次数 = 35
        self.大齿轮齿厚 = 180
        self.小齿轮齿厚 = 180
        self.大齿轮扭矩 = 95870
        self.传动效率 = 0.93
        self.大齿轮齿形系数 = 0.142
        self.齿形系数sf1 = 2.08
        self.齿形系数sf = 1.8
        self.齿形系数y = 0.104
    def 计算弯曲应力(self):
        self.小齿轮齿形系数 = self.齿形系数sf1 ** 2 / self.齿形系数sf**2 * self.齿形系数y
        self.小齿轮行程次数 = self.大齿轮行程次数 *self.z1 / self.z2
        self.小齿轮扭矩=self.大齿轮扭矩/self.传动效率/(self.z1 / self.z2)
        小齿轮啮合直径=self.ax*self.z2/(self.z2+self.z1)*2
        self.小齿轮啮合直径=小齿轮啮合直径
        大齿轮啮合直径=self.ax*self.z1/(self.z2+self.z1)*2
        self.大齿轮啮合直径=大齿轮啮合直径
        self.大齿轮速度=np.pi*大齿轮啮合直径*0.001*self.大齿轮行程次数/60
        self.小齿轮速度=np.pi*小齿轮啮合直径*0.001*self.小齿轮行程次数/60
        self.大齿轮速度系数=10/(10+self.大齿轮速度)
        self.小齿轮速度系数=10/(10+self.小齿轮速度)
        self.大齿轮齿面受力=((self.大齿轮扭矩/self.传动效率) / 10 * 100) / (self.大齿轮啮合直径 / 2 / 10)
        self.小齿轮齿面受力=(self.小齿轮扭矩 / 10 * 100) / (self.小齿轮啮合直径 / 2 / 10)
        节距=self.m*np.pi
        self.大齿轮弯曲应力=self.大齿轮齿面受力/(self.大齿轮速度系数*self.大齿轮齿厚*节距*self.大齿轮齿形系数)
        self.小齿轮弯曲应力 = self.小齿轮齿面受力 / (self.小齿轮速度系数 * self.小齿轮齿厚 * 节距 * self.小齿轮齿形系数)
        return
    def 计算齿面应力(self):
        self.大齿轮齿面应力=self.大齿轮齿面受力*(self.z2+self.z1)/(0.1*self.小齿轮啮合直径*0.1*self.大齿轮齿厚 \
                                    *2*self.z1)
        self.小齿轮齿面应力 = self.小齿轮齿面受力 * (self.z2 + self.z1) / (0.1 * self.小齿轮啮合直径 * 0.1 * self.小齿轮齿厚 \
                                                                   * 2 * self.z1)
        return
if __name__=="__main__":
    测试=齿轮主参数计算()
    测试.渐开线函数()
    测试.垮齿厚()
    测试.计算弯曲应力()
    测试.计算齿面应力()
