# -*- coding = utf-8 -*-
# @time:2023/9/2 20:03
# Author:lizhuang
# @File:表格类.py
# @Software:PyCharm
from PyQt5 import QtWidgets
#from MainForm import Ui_MainForm
#from Children import Ui_Form
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap,QFont
#import numpy as np
from math import pi,log
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QTableWidget,QTableWidgetItem,QHeaderView
from mdbb数据 import 读取数据库
from PyQt5.QtCore import QObject,pyqtSignal
class MainForm3(QtWidgets.QWidget):
    signal_0 = pyqtSignal(str)
    def __init__(self,表名称='V带工况系数KA'):
        super(MainForm3, self).__init__()
        loadUi('../皮带计算/biao.ui',self)
        self.tableWidget1=self.findChild(QTableWidget,'tableWidget')
        self.零件数据=读取数据库(表名称=表名称)
        self.填充表格()
        self.值=0
    def 填充表格(self):
        处理数据 = self.零件数据
        列数 = len(self.零件数据)
        行数 = 处理数据
        self.tableWidget1.setColumnCount(len(处理数据.columns))
        self.tableWidget1.setRowCount(len(处理数据.index))
        for i in range(len(处理数据.index)):
            for j in range(len(处理数据.columns)):
                self.tableWidget1.setItem(i, j, QTableWidgetItem(str(处理数据.iloc[i, j])))
        self.tableWidget1.setHorizontalHeaderLabels(处理数据.columns.tolist())
        # 设置单元格字体大小
        font = QFont("Arial", 12)
        self.tableWidget1.setFont(font)
        self.tableWidget1.setWordWrap(True)
        # 设置表头字体大小
        header_font = QFont("Arial", 14)
        self.tableWidget1.horizontalHeader().setFont(header_font)
        #self.tableWidget1.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        #self.tableWidget1.verticalHeader().setDefaultSectionSize(100)
        # 设置单元格居中显示
        # self.tableWidget1.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter)
        # self.tableWidget1.verticalHeader().setDefaultAlignment(Qt.AlignVCenter)
        return
    def xianshiyaliji(self, 行数, 列数):
        print(行数,列数)
        self.值=self.零件数据.iloc[行数,列数]
        self.值=str(self.值)
        #print(self.值)
        return self.值
    def suchuxinxi(self):
        self.signal_0.emit(self.值)
        self.close()
        return
if __name__ == '__main__':
  import sys
  app = QApplication.instance()
  if app is None:
      app = QApplication(sys.argv)
  Widget = MainForm3(表名称='普通V带的基准长度系列')
  Widget.show()
  sys.exit(app.exec_())