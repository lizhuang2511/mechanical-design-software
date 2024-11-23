import numpy as np
class 驱动轴承寿命计算():
    def __init__(self):
        self.齿轮荷重=33900
        self.系数=1
        self.回转速度=296
        self.基本定格荷重=200000
        self.spm=60
    def 计算(self):
        self.载荷=1.3*self.系数*self.齿轮荷重
        self.总时间=60/self.spm
        self.受力时间=self.总时间*0.2
        self.空载时间=self.总时间*0.8
        self.空载受力=self.载荷*0.1
        self.平均受力=((self.载荷**(10/3)*self.受力时间+self.空载时间*self.空载受力**(10/3))/(self.空载时间+self.受力时间))**(3/10)
        self.寿命时间=16650/self.回转速度*(self.基本定格荷重/self.平均受力)**(10/3)
        self.年数=self.寿命时间/16/25/12#10年以上全周期负荷超过百分70
        return
if __name__=="__main__":
    测试=驱动轴承寿命计算()
    测试.计算()