# -*- coding = utf-8 -*-
# @time:2023/5/24 11:53
# Author:lizhuang
# @File:零件尺寸计算.py
# @Software:PyCharm
from PyQt5 import QtWidgets
#from MainForm import Ui_MainForm
#from Children import Ui_Form
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap,QFont
#import numpy as np
from math import pi,log
import pandas as pd
from mdbb数据1 import 读取数据库
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QTableWidget,QTableWidgetItem,QHeaderView
class MainForm3(QtWidgets.QWidget):
    def __init__(self):
        super(MainForm3, self).__init__()
        loadUi('../滚动轴承设计/lingjiancicun.ui',self)
        self.tableWidget1=self.findChild(QTableWidget,'tableWidget')
        self.零件数据=读取数据库(表名称='深沟球轴承')
        #self.textBrowser.setPlainText(self.数据[1])
        self.填充表格()
        self.Btype='深沟球轴承'
        self.Bcode='609'
        self.d=9
        self.D=24
        self.B=7
        self.cr=3350
        self.cor=1400
        self.nlimz=22000
        self.nlimy=30000
    def leixingxuan(self):
        print(self.comboBox.currentText())
        self.零件数据 = 读取数据库(表名称=str(self.comboBox.currentText()))
        self.填充表格()
        return
    def 填充表格(self):
        处理数据=self.零件数据
        列数=len(self.零件数据)
        行数=处理数据
        self.tableWidget1.setColumnCount(len(处理数据.columns))
        self.tableWidget1.setRowCount(len(处理数据.index))
        for i in range(len(处理数据.index)):
            for j in range(len(处理数据.columns)):
                self.tableWidget1.setItem(i, j, QTableWidgetItem(str(处理数据.iloc[i, j])))
        self.tableWidget1.setHorizontalHeaderLabels(处理数据.columns.tolist())
        # 设置单元格字体大小
        font = QFont("Arial", 12)
        self.tableWidget1.setFont(font)

        # 设置表头字体大小
        header_font = QFont("Arial", 14)
        self.tableWidget1.horizontalHeader().setFont(header_font)
        self.tableWidget1.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget1.verticalHeader().setDefaultSectionSize(30)
        # 设置单元格居中显示
        #self.tableWidget1.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter)
        #self.tableWidget1.verticalHeader().setDefaultAlignment(Qt.AlignVCenter)
        return
    def xianshiyaliji(self,行数,列数):
        print(行数,列数)
        if str(self.comboBox.currentText())=='推力滚子轴承':
            self.lineEdit.setText(str(float(self.零件数据.loc[行数, 'Ca'])*1000))
            self.Btype = str(self.comboBox.currentText())
            self.Bcode = str(self.零件数据.loc[行数,'Bcode'])
            self.d = int(self.零件数据.loc[行数,'d'])
            self.D = int(self.零件数据.loc[行数,'DD'])
            self.T = int(self.零件数据.loc[行数,'T1'])
            self.cr = float(self.零件数据.loc[行数,'Ca'])*1000
            self.cor = float(self.零件数据.loc[行数,'Coa'])*1000
            #self.nlimz =int(self.零件数据.loc[行数,'nlimz'])
            self.nlimy = int(self.零件数据.loc[行数,'nlimy'])
        elif str(self.comboBox.currentText())=='推力球轴承':
            self.lineEdit.setText(str(float(self.零件数据.loc[行数, 'Ca'])*1000))
            self.Btype = str(self.comboBox.currentText())
            self.Bcode = str(self.零件数据.loc[行数, 'Bcode'])
            self.d = int(self.零件数据.loc[行数, 'd'])
            self.D = int(self.零件数据.loc[行数, 'DD'])
            self.T = int(self.零件数据.loc[行数, 'T'])
            self.cr = float(self.零件数据.loc[行数, 'Ca'])*1000
            self.cor = float(self.零件数据.loc[行数, 'Coa'])*1000
            self.nlimz = int(self.零件数据.loc[行数, 'nlimz'])
            self.nlimy = int(self.零件数据.loc[行数, 'nlimy'])
        else:
            self.lineEdit.setText(str(float(self.零件数据.loc[行数, 'Cr'])*1000))
            self.Btype = str(self.comboBox.currentText())
            self.Bcode = str(self.零件数据.loc[行数, 'Bcode'])
            self.d = int(self.零件数据.loc[行数, 'd'])
            self.D = int(self.零件数据.loc[行数, 'DD'])
            self.B = int(self.零件数据.loc[行数, 'B'])
            self.cr = float(self.零件数据.loc[行数, 'Cr'])*1000
            self.cor = float(self.零件数据.loc[行数, 'Cor'])*1000
            self.nlimz = int(self.零件数据.loc[行数, 'nlimz'])
            self.nlimy = int(self.零件数据.loc[行数, 'nlimy'])
        return
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm3()
    myshow.show()
    sys.exit(app.exec_())