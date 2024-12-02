import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.optimize import root,fsolve
import numpy as np
import pandas as pd
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
def 多项式(a,b,c,d,x):
    y=a*x**3+b*x**2+c*x+d
    return y
开式轴承直径=np.linspace(0,1000,1000)
半开式轴承直径=np.linspace(0,2000,1000)
导轨长度=np.linspace(0,2000,1000)
开式摆动轴承油量=多项式(1.447e-7,-7.371e-5,0.1357,-0.583,开式轴承直径)
开式转动轴承油量=多项式(-7.077e-9,8.159e-5,0.06086,0.2908,开式轴承直径)
半开式摆动轴承油量=多项式(1.812e-8,-1.844e-5,0.067,-0.6297,半开式轴承直径)
半开式转动轴承油量=多项式(-8.865e-10,2.042e-5,0.03045,0.2405,半开式轴承直径)
水平导轨油量=多项式(1.263e-8,-2.122e-5,0.03749,-2.002,导轨长度)
垂直导轨油量=多项式(8.644e-12,5.465e-9,0.009588,0.03063,导轨长度)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()
ax1.set_ylim(0,120)
#ax3=ax1.twiny()
# Add some extra space for the second axis at the bottom
fig.subplots_adjust(bottom=0.2)

X = np.linspace(0,1,1000)
Y = np.cos(X*20)

ax1.plot(开式轴承直径,开式摆动轴承油量)
ax1.plot(开式轴承直径,开式转动轴承油量)
ax1.set_xlabel("开式轴承直径(mm)")
ax1.set_xlim(0,1000)
#new_tick_locations = np.array([.2, .5, .9])
y_major_locator=MultipleLocator(10)
ax1.yaxis.set_major_locator(y_major_locator)
# Move twinned axis ticks and label from top to bottom
ax2.xaxis.set_ticks_position("bottom")
ax2.xaxis.set_label_position("bottom")

# Offset the twin axis below the host
ax2.spines["bottom"].set_position(("axes", -0.15))

# Turn on the frame for the twin axis, but then hide all
# but the bottom spine
ax2.set_frame_on(True)
x_major_locator=MultipleLocator(50)
ax1.xaxis.set_major_locator(x_major_locator)
ax2.patch.set_visible(False)
biaoqian=[0,250,500,750,1000]
标签2=np.linspace(0,1000,21).tolist()
ax1.set_xticks(标签2)
标签1=标签2
for i in range(len(标签1)):
    if 标签1[i] in biaoqian:
        标签1[i]=int(标签1[i])
    else:
        标签1[i]=''
ax1.set_xticklabels(标签1)

# as @ali14 pointed out, for python3, use this
# for sp in ax2.spines.values():
# and for python2, use this
'''for sp in ax2.spines.itervalues():
    sp.set_visible(False)
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(tick_function(new_tick_locations))'''

ax2.spines["bottom"].set_visible(True)
ax2.plot(半开式轴承直径,半开式摆动轴承油量,label="摆动运动的轴承")
ax2.plot(半开式轴承直径,半开式转动轴承油量,label="旋转运动的轴承")
ax2.plot(导轨长度,水平导轨油量,label="水平运动的导轨")
ax2.plot(导轨长度,垂直导轨油量,label="垂直运动的导轨")
ax2.set_xlabel("半开轴承直径或导轨长度(mm)")
ax2.set_xlim(0,2000)
x_major_locator2=MultipleLocator(100)
ax2.xaxis.set_major_locator(x_major_locator2)
biaoqian2=[0,500,1000,1500,2000]
标签3=np.linspace(0,2000,21).tolist()
ax2.set_xticks(标签3)
标签1=标签3
for i in range(len(标签1)):
    if 标签1[i] in biaoqian2:
        标签1[i]=int(标签1[i])
    else:
        标签1[i]=''
ax2.set_xticklabels(标签1)
ax1.grid(linestyle='--')
ax1.set_title('润滑油脂消耗曲线',size=16)
ax1.set_ylabel('润滑剂数量(cm^3/10^3)',size=12)
plt.legend(loc="upper left")
plt.show()