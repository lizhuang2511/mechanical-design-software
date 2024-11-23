import pandas as pd
from pygments import formatters, lexers
import sviewgui.sview as sv
#数据=pd.read_csv('../静力学/n2运动数据.csv',sep=' ')
数据 = pd.read_csv('../静力学/n2运动数据.csv', sep=' ')#图像处理.打开图像()
a=sv.Csviwer()
a.loadData(数据)
a.show()
