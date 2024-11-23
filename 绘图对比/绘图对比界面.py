
"""
Created on Sat Jan  8 22:05:14 2022
bug：
@author: lizhuang
"""
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel
from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget,QAbstractItemView#Qlabel,QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
#from random import randint
from PyQt5 import QtCore, QtGui
#import ziyuan_rc
import sys
#from PyQt5.QtCore import QEventLoop, QTimer
import pandas as pd
#import sys
sys.path.append("../绘图对比")
from 绘图对比 import 绘图对比
sys.path.append("../主界面")
import 主界面
import subprocess
from PyQt5.QtWidgets import QFileDialog
class MainWindow(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        loadUi('../绘图对比/huituduibi.ui',self)
    def huatu(self):
        绘图对比1=绘图对比(str(self.lineEdit.text()),str(self.lineEdit_2.text()))
        绘图对比1.绘制多图()
        print('正在绘制')
        return
    def huatunengli(self):
        绘图对比1=绘图对比(str(self.lineEdit.text()),str(self.lineEdit_2.text()))
        绘图对比1.绘制能力曲线()
        print('正在绘制')
        return
    def dakaiwenjianjia(self):
        import os
        桌面=os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面+'/数据文件'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        start_directory = 桌面+'/数据文件'
        os.startfile(start_directory)
        return
    def 返回路径(self):
        filePath, name = QFileDialog.getOpenFileName(self, "Open File",
                                                  self.sujuwenjiac(), "csv files (*.csv)")
        #A=QTextCodec.codecForName('utf-8')
        #c=A.fromUnicode(filePath).data().decode('GB2312')
        '''A = QTextCodec.codecForName('GB2312')
        b = A.toUnicode(filePath).data()'''
        #print(b)
        #print(c)
        ''''#A=QTextStream(filePath)
        A=filePath.setCodec("UTF-8")
        c=A.readAll()'''

        #filePath='r'+"'"+filePath+"'"
        #print(filePath.decode('unicode'))
        return filePath
    def wenjianlujing2(self):
        #print(type(filename))
        filename=self.返回路径()
        #print(unicode(filename,'utf8'))
        with open(self.sujuwenjiac()+'/test.txt', 'w') as f:
            f.write(filename)
        f.close()
        print('配置路径')
        '''with open("./test.txt", "r", encoding='utf-8') as f:  # 打开文本
            data = f.read()  # 读取文本
            print(data)'''
        self.lineEdit_2.clear()
        self.lineEdit_2.setText(filename)
        #self.lujing=str('r'+'"'+filename+'"')
        #print(self.lujing)
        '''if self.pushButton.text() == "读取滑块位置数据路径":
            if self.pushButton.isChecked():
                self.excel_path = filename
                self.textEdit_2.append("需要读取的Excel路径为:" + filename)
                self.textEdit_2.append("文件格式为:" + filetype)
        self.pushButton.toggle()'''
        return
    def wenjianlujing1(self):
        #print(type(filename))
        filename=self.返回路径()
        #print(unicode(filename,'utf8'))
        with open(self.sujuwenjiac()+'/test.txt', 'w') as f:
            f.write(filename)
        f.close()
        print('配置路径')
        '''with open("./test.txt", "r", encoding='utf-8') as f:  # 打开文本
            data = f.read()  # 读取文本
            print(data)'''
        self.lineEdit.clear()
        self.lineEdit.setText(filename)
        #self.lujing=str('r'+'"'+filename+'"')
        #print(self.lujing)
        '''if self.pushButton.text() == "读取滑块位置数据路径":
            if self.pushButton.isChecked():
                self.excel_path = filename
                self.textEdit_2.append("需要读取的Excel路径为:" + filename)
                self.textEdit_2.append("文件格式为:" + filetype)
        self.pushButton.toggle()'''
        return
    def sujuwenjiac(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        return dirs
if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
       app = QApplication(sys.argv)
    Widget= MainWindow()
    Widget.show()
    sys.exit(app.exec_())

