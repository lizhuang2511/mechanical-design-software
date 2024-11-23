import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
class 拉深电机能量():
    def __init__(self,压力机滑块行程次数=25,压力=800,深度=20,电机运行系数=1.3,系数c=0.7,压机效率=0.4, \
                 压力机滑块行程次数与名义次数比=1,压边力=0,拉深垫工作行程=0):#t,#mm
        self.压力机滑块行程次数=压力机滑块行程次数/60
        self.压力=压力*10000
        self.深度=深度/1000
        self.压边力=压边力
        self.拉深垫工作行程=拉深垫工作行程/1000
        self.电机运行系数=电机运行系数
        self.系数c=系数c
        self.压力机效率=压机效率
        self.压力机滑块行程次数与名义次数比=压力机滑块行程次数与名义次数比
        return
    def 电机所需功率(self):
        电机所需功率=self.电机运行系数*(self.工件变形功()+self.拉伸垫功())/self.压力机工作时间()/self.压力机效率
        电机所需功率=int(电机所需功率/1000)
        return 电机所需功率
    def 工件变形功(self):
        工件变形功=self.系数c*self.压力*self.深度
        return 工件变形功
    def 拉伸垫功(self):
        拉伸垫功=self.压边力*self.拉深垫工作行程
        return 拉伸垫功
    def 压力机工作时间(self):
        t=1/self.压力机滑块行程次数/self.压力机滑块行程次数与名义次数比
        return t
class 冲压电机(拉深电机能量):
    def __init__(self, 压力机滑块行程次数=25, 压力=800, 冲裁厚度=20, 电机运行系数=1.3, 压机效率=0.4, \
                 压力机滑块行程次数与名义次数比=1):  # t,#mm
        self.压力机滑块行程次数 = 压力机滑块行程次数 / 60
        self.压力 = 压力 * 10000
        self.冲裁厚度 = 冲裁厚度 / 1000
        self.电机运行系数 = 电机运行系数
        self.压力机效率 = 压机效率
        self.压力机滑块行程次数与名义次数比 = 压力机滑块行程次数与名义次数比
        return
    def 工件变形功(self):
        工件变形功 = 0.315 * self.压力 *self.冲裁厚度
        return 工件变形功
    def 拉伸垫功(self):
        拉伸垫功 = 0
        return 拉伸垫功
if __name__ == '__main__':
   电机能量=拉深电机能量()
   电机所需功率=电机能量.电机所需功率()
   print(电机所需功率)
   冲压电机=冲压电机()
   冲压电机所需功率=冲压电机.电机所需功率()
   print(冲压电机所需功率)
