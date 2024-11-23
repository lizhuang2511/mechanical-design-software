import pandas as pd
import numpy as np
class 飞轮能力计算():
    def __init__(self):
        self.spm=50
        self.d1=1300
        #self.d2=780
        #self.d3=656
        self.d5=1080
        self.b1=330
        #self.b2=0
        self.mrpm=1450
        self.frpm=305.6
        self.ke=2000
        self.电机功率=22
    def 计算能量(self):
        self.文件路径=r'C:\Users\Administrator\Desktop\数据文件\FN计算数据.csv'
        冲压运动数据表=pd.read_csv(self.文件路径)
        self.s = max(冲压运动数据表['距离下死点位置'])
        self.s2=self.s/2
        冲压运动数据表 = 冲压运动数据表.loc[冲压运动数据表['滑块速度'] < 0, ['距离下死点位置','发生力']]
        self.冲压运动数据表=冲压运动数据表.loc[冲压运动数据表['距离下死点位置'] < self.s2, ['距离下死点位置','发生力']]
        self.差分位置=np.diff(self.冲压运动数据表['距离下死点位置'])
        self.差分位置=np.append(self.差分位置,0)
        self.发生力=np.array(self.冲压运动数据表['发生力'])
        self.能量=-np.sum(self.发生力*self.差分位置)/1000*10000/4#n*m
        self.功率=self.能量/(60/self.spm)/1000
        return
    def 飞轮惯性(self):
        self.w1=np.pi/4*(self.d1**2-self.d5**2)*self.b1*0.0073*0.001
        k=(1/8)*(self.d1**2+self.d5**2)*0.000001
        self.i=k*self.w1+13
        return
    def 时间校核断续(self):
        self.马达扭矩 = self.电机功率 * 974 / self.mrpm
        self.cpm=self.spm*0.6#断续运转
        self.kf=5.58*self.i*(self.frpm/100)**2
        self.se=1-np.sqrt(1-self.ke/self.kf)#降速比
        self.t1=4*self.i*(self.frpm/self.mrpm)**2*self.se/375/self.马达扭矩*self.mrpm
        self.断续运转容许回复时间=60/self.cpm-(10/self.spm)
        self.必要扭矩 = self.i * (self.frpm / self.mrpm) ** 2 * 4 * self.mrpm * self.se / 375 / self.断续运转容许回复时间
        self.必要容量 = self.必要扭矩 * self.mrpm / 974 * 1.25
        #容许回复时间
        return
    def 时间校核连续(self):
        self.马达扭矩=self.电机功率*974/self.mrpm
        self.kf= 5.58 * self.i * (self.frpm / 100) ** 2#飞轮能量
        self.se = 1 - np.sqrt(1 - self.ke / self.kf)
        self.连续运转容许回复时间=60/(self.spm*(1-self.se/2))
        self.必要扭矩 = self.i * (self.frpm / self.mrpm) ** 2 * 4 * self.mrpm * self.se / 375 / self.连续运转容许回复时间
        self.t1=4*self.i*(self.frpm/self.mrpm)**2*self.se/375/self.马达扭矩*self.mrpm
        self.必要容量=self.必要扭矩*self.mrpm/974*1.25
        return
if __name__ == '__main__':
    测试=飞轮能力计算()
    测试.计算能量()
    测试.飞轮惯性()
    测试.时间校核连续()
    测试.时间校核断续()
