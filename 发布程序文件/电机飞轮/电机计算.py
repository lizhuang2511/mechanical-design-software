import numpy as np
import matplotlib.pyplot as plt
压力机吨位=np.linspace(80,800,1000)*1000*10
成型速度=0.2#m/s
电机功率=压力机吨位*成型速度
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
fig, ax = plt.subplots()
ax.set_title( "电机功率曲线")
ax.plot(压力机吨位/10000,电机功率/1000)
plt.show()
#计划机fn800只要90kw就可以了
