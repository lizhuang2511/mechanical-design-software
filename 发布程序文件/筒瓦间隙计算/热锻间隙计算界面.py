# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:05:14 2022

@author: lizhuang
"""
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel,QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import sys
import pandas as pd
from pygments import formatters, lexers
sys.path.append("../sviewguiBD")
import sviewgui2.sview as sv
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import 热模锻计算筒瓦
#import 图像处理
class wreduanjianxi(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        loadUi('../筒瓦间隙计算/jianxi.ui',self)
        self.读取=sv.Csviwer()
    def dkaisv(self):
        数据 = pd.read_csv('../静力学/n2运动数据.csv', sep=' ')
        #图像处理.打开图像()
        self.读取.loadData(数据)
        self.读取.show()
        return
    def jisuanjianxi(self):
        计算=热模锻计算筒瓦.热锻铜瓦间隙计算(直径=float(self.lineEdit_3.text()),杆一角速度=float(self.lineEdit.text()), \
                            杆二角速度=float(self.lineEdit_2.text()))
        滑动速度=计算.滑动速度1()
        print(滑动速度)
        铜瓦间隙=计算.铜瓦间隙()
        self.lineEdit_4.setText(str(round(滑动速度,3)))
        self.lineEdit_5.setText(str(round(铜瓦间隙,3)))
        return
if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
       app = QApplication(sys.argv)
    Widget= wreduanjianxi()
    Widget.show()
    sys.exit(app.exec_())

