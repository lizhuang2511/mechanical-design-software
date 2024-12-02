import numpy as  np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.optimize import root,fsolve
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
class 热锻铜瓦间隙计算():
    def __init__(self,直径=300,杆一角速度=10,杆二角速度=10):
        self.直径=直径/1000
        self.杆一角速度=杆一角速度
        self.杆二角速度=杆二角速度
        self.滑动速度 = self.滑动速度1()
    def 滑动速度1(self):
        滑动速度=(self.杆一角速度-self.杆二角速度)*self.直径/2
        return abs(滑动速度)
    def 铜瓦间隙(self):
        百分比=0.7701*self.滑动速度**0.2669#筒瓦间隙/公称直径
        铜瓦间隙=百分比*self.直径*100
        return  铜瓦间隙#um丝
    def 测试画图(self):
        self.滑动速度=np.linspace(0.3,90,1000)
        plt.plot(self.滑动速度,self.铜瓦间隙())
        plt.show()
        return
    def 定spm画图(self):
        直径=np.linspace(100,1000,1000)
        self.直径=直径/1000
        plt.plot(直径, self.铜瓦间隙())
        plt.show()
        return
if __name__=="__main__":
    热锻铜瓦间隙计算=热锻铜瓦间隙计算()
    #热锻铜瓦间隙计算.定spm画图()
    print(热锻铜瓦间隙计算.铜瓦间隙())
