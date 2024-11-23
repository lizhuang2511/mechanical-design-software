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
import os
import 批量导入
from PyQt5.QtWidgets import QFileDialog
#import 图像处理
class piliangdaoru(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        loadUi('../批量导入/daoru.ui',self)
    def dakai(self):
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        filePath= QFileDialog.getExistingDirectory(None,桌面)
        self.lineEdit.clear()
        self.lineEdit.setText(filePath)
        print(filePath)
        return
    def daoru(self):
        PATH=str(self.lineEdit.text())
        批量导入.批量更改(PATH)
        return
if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
       app = QApplication(sys.argv)
    Widget= piliangdaoru()
    Widget.show()
    sys.exit(app.exec_())

