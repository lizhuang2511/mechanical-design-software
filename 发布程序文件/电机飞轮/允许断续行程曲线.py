import numpy as np
class 允许断续行程曲线():
    def __init__(self):
        self.i=5.89
        self.主轴回转数=25
        self.被驱动gd=20#飞轮转动惯量
        self.衬套外径=450
        self.衬套内径=400
        self.面数=9
        self.断续转速=10
        self.制动扭矩=717
    def 计算(self):
        self.驱动轴回转数 = self.主轴回转数 * self.i
        self.衬套有效径=(self.衬套外径+self.衬套内径)/2
        self.衬里周速 = np.pi * self.衬套有效径*self.驱动轴回转数/60/1000
        self.t=60/self.断续转速
        self.衬套面积 =np.pi/4*(self.衬套外径-self.衬套内径)**2/100
        self.被驱动能量=self.被驱动gd*self.驱动轴回转数**2/7160
        self.发热常数=self.被驱动能量/self.衬套面积/self.面数*self.cpm
        self.单位吸收能量=self.被驱动能量/self.衬套面积/self.面数
        self.结合时间=self.被驱动gd*self.主轴回转数/375/self.制动扭矩
        self.能量吸收率=self.单位吸收能量/self.结合时间
        return
if __name__ == "__main__":
    测试=允许断续行程曲线()
