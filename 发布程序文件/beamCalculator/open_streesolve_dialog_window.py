# -*- coding = utf-8 -*-
# @time:2023/4/17 11:16
# Author:lizhuang
# @File:open_streesolve_dialog_window.py
# @Software:PyCharm
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel
#from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel,QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import pandas as pd
class open_streesolve_dialog_window(QtWidgets.QDialog):
    def __init__(self,user_beam,niuju=10000000):
        super(open_streesolve_dialog_window, self).__init__()
        # self.setupUi(self)
        # self.setupUi(self)
        loadUi('../beamCalculator/UiFiles/open_streesolve_dialog_window.ui', self)
        self.user_beam2 = user_beam
        self.lineEdit.setText(str(int(niuju)))
        print('Python')
    def streescalc(self):
        self.user_beam2.calculate()
        self.弯矩=float(self.lineEdit_3.text())
        self.扭矩 = float(self.lineEdit.text())
        TENSILE_MODULUS = 210000  # 拉伸模量
        self.切变模量=TENSILE_MODULUS/2*(1+0.3)
        self.user_beam2.calculatestree(self.弯矩,self.扭矩)
        self.user_beam2.calculatezhuanjiao(self.切变模量, self.扭矩)
        self.lineEdit_5.setText(str(int(self.user_beam2.thy)));
        self.lineEdit_6.setText(str(int(self.user_beam2.tx)));
        self.lineEdit_7.setText(str(int(self.user_beam2.jiaodu)));
        a = pd.DataFrame([[30,21]],columns=["wan","niu"])
        a['wan']=self.user_beam2.thy
        a['niu'] = self.user_beam2.tx
        a.to_csv(self.wenjianjia()+'/弯扭距.csv')
        return
    def wenjianjia(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        return dirs
if __name__ == '__main__': 
  test=open_streesolve_dialog_window()