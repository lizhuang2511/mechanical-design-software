# -*- coding = utf-8 -*-
# @time:2023/4/17 20:58
# Author:lizhuang
# @File:fuzhuui.py
# @Software:PyCharm
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel
#from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel,QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import pandas as pd
class fuzhuui(QtWidgets.QDialog):
    def __init__(self):
        super(fuzhuui, self).__init__()
        # self.setupUi(self)
        # self.setupUi(self)
        loadUi('../beamCalculator/UiFiles/fuzhu.ui', self)
        print('Python')
    def calc(self):
        self.扭矩=float(self.lineEdit.text())
        self.齿轮直径 = float(self.lineEdit_2.text())
        self.系数=float(self.lineEdit_4.text())
        self.载荷=int(self.扭矩/(self.齿轮直径/2))/self.系数
        self.lineEdit_3.setText(str(int(self.载荷)))
        a = pd.DataFrame([[30, 21]], columns=["niuju", "zaihe"])
        a['niuju'] = self.扭矩
        a['zaihe'] = self.载荷
        a.to_csv(self.wenjianjia() + '/弯载荷.csv')
        return self.载荷
    def wenjianjia(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        return dirs
if __name__ == '__main__': 
  test=fuzhuui()
  test.show()