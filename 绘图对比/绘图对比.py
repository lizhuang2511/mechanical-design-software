
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.optimize import root,fsolve
import re
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import numpy as np
import pandas as pd
class 绘图对比():
    def __init__(self,对比文件1=r'C:\Users\Administrator\Desktop\数据文件\行程120中间位置90度.csv',对比文件2=r'C:\Users\Administrator\Desktop\数据文件\行程120下死点90度.csv'):
        self.对比文件1=对比文件1
        self.对比文件2=对比文件2
        self.对比文件3 = 'N2伺服计算数据2'
        self.文件路径=self.数据文件夹()
    def 读取文件(self):
        #路径1=self.文件路径+'/'+self.对比文件1+'.csv'
        数据1=pd.read_csv(self.对比文件1,sep=",")
        #路径2 = self.文件路径 + '/' + self.对比文件2 + '.csv'
        数据2=pd.read_csv(self.对比文件2,sep=",")
        #路径3 = self.文件路径 + '/' + self.对比文件3 + '.csv'
        #数据3 = pd.read_csv(路径3, sep=",")
        #return 数据1,数据2,数据3
        return 数据1, 数据2
    def 获取文件名(self):
        文件名1 = re.split("[/]", self.对比文件1)
        文件名1=文件名1[-1]
        self.文件名1 = re.split("[.]", 文件名1)[0]
        print(self.文件名1)
        文件名2 = re.split("[/]", self.对比文件2)
        文件名2 = 文件名2[-1]
        self.文件名2 = re.split("[.]", 文件名2)[0]
        print(self.文件名2)
        return
    def 绘图(self,数据1,数据2):
        self.获取文件名()
        fig, ax = plt.subplots()
        ax.set_title("角度-滑块位置曲线对比")
        ax.set_xlabel("角度（°）")
        ax.set_ylabel("距离下死点位置(mm)")
        ax.plot(数据1['角度'],数据1['距离下死点位置'],label=self.文件名1)
        ax.plot(数据2['角度'],数据2['距离下死点位置'],label=self.文件名2)
        ax.legend(loc=0, ncol=2)
        ax.set_xlim(0, 360)
        x_major_locator = MultipleLocator(20)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.grid(linestyle='--')
        plt.show()
        fig, ax = plt.subplots()
        ax.set_title("角度-滑块速度曲线")
        ax.set_xlabel("角度（°）")
        ax.set_ylabel("滑块速度（mm/s）")
        ax.plot(数据1['角度'], 数据1['滑块速度'], label=self.文件名1)
        ax.plot(数据2['角度'], 数据2['滑块速度'], label=self.文件名2)
        ax.legend(loc=0, ncol=2)
        ax.set_xlim(0, 360)
        x_major_locator = MultipleLocator(20)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.grid(linestyle='--')
        plt.show()
        fig, ax = plt.subplots()
        ax.set_title("滑块位置-滑块速度曲线")
        ax.set_xlabel("距离下死点位置(mm)")
        ax.set_ylabel("滑块速度（mm/s）")
        ax.plot(数据1['距离下死点位置'], 数据1['滑块速度'], label=self.文件名1)
        ax.plot(数据2['距离下死点位置'], 数据2['滑块速度'], label=self.文件名2)
        ax.set_xlim(0, 350)
        x_major_locator = MultipleLocator(30)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.grid(linestyle='--')
        ax.legend(loc=0, ncol=2)
        plt.show()
        fig, ax = plt.subplots()
        ax.set_title("角度-滑块加速度曲线")
        ax.set_xlabel("角度（°）")
        ax.set_ylabel("滑块加速度")
        ax.plot(数据1['角度'], 数据1['滑块加速度'], label=self.文件名1)
        ax.plot(数据2['角度'], 数据2['滑块加速度'], label=self.文件名2)
        ax.set_xlim(0, 360)
        x_major_locator = MultipleLocator(20)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.grid(linestyle='--')
        ax.legend(loc=0, ncol=2)
        plt.show()
        return
    def 绘图压力曲线(self,数据1,数据2):
        self.获取文件名()
        最大位移=max(数据1['距离下死点位置'])
        最大力=max(数据1['发生力'])
        数据1 = 数据1[数据1['滑块速度'] < 0]
        数据2 = 数据2[数据2['滑块速度'] < 0]
        数据1 = 数据1[数据1['距离下死点位置'] < (最大位移 / 2)]
        数据2 = 数据2[数据2['距离下死点位置'] < (最大位移 / 2)]
        fig, ax = plt.subplots()
        ax.set_title("距离下死点位置(mm)-能力发生曲线对比")
        ax.set_xlabel("位置")
        ax.set_ylabel("发生力")
        ax.plot(数据1['距离下死点位置'], 数据1['发生力'], label=self.文件名1)
        ax.plot(数据2['距离下死点位置'], 数据2['发生力'], label=self.文件名2)
        ax.legend(loc=0, ncol=2)
        ax.set_xlim(0, 350/2)
        x_major_locator = MultipleLocator(30)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.grid(linestyle='--')
        ax.set_xlim(0,最大位移 / 2)
        ax.set_ylim(0, 最大力+(最大力/20))
        plt.show()
        return
    def 绘制能力曲线(self):
        self.绘图压力曲线(self.读取文件()[0], self.读取文件()[1])
        return
    def 绘制多图(self):
        self.绘图(self.读取文件()[0], self.读取文件()[1])
        return
    def 数据文件夹(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        return dirs

    def 绘图3图对比(self,数据1,数据2,数据3):
        fig, ax = plt.subplots()
        ax.set_title("伺服肘杆机构时间-滑块位置曲线对比")
        ax.set_xlabel("时间（s）")
        ax.set_ylabel("距离下死点位置(mm)")
        ax.plot(数据1['时间'],数据1['距离下死点位置'],label='曲柄连杆机构')
        ax.plot(数据2['时间重置'],数据2['距离下死点位置'],label='肘杆机构')
        ax.plot(数据3['时间重置'], np.flipud(数据3['距离下死点位置']), label='伺服肘杆机构',linestyle='--')
        ax.legend(loc=0, ncol=2)
        plt.show()
        return
    def 绘图3图对比2(self):
        self.绘图3图对比(self.读取文件()[0], self.读取文件()[1],self.读取文件()[2])
        return
if __name__=="__main__":
    绘图对比=绘图对比()
    数据1=绘图对比.读取文件()[0]
    绘图对比.绘图3图对比2()