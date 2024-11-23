from math import *
import numpy as np
import pandas as pd
#import sviewgui.sview as sv
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
l=1775*0.001
作用=(1775/2-(670+158/2))*0.001
坐标=np.linspace(0,l,100)#时间
弯矩=np.linspace(0,l,100)
for i in range(len(坐标)):
    if 坐标[i]<作用:
        弯矩[i]=-3000000*坐标[i]
    if 坐标[i] >作用 and 坐标[i]<l-作用:
        弯矩[i] = -3000000 * 坐标[i]+3000000*(坐标[i]-作用)
    if 坐标[i]>l-作用:
        弯矩[i] = -3000000 * (l-坐标[i])
plt.plot(坐标,弯矩)
plt.show()
