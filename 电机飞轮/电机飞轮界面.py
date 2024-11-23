from PyQt5 import QtWidgets
#from MainForm import Ui_MainForm
#from Children import Ui_Form
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog
import subprocess
from PyQt5.QtGui import QPixmap
import sys
sys.path.append("../开始界面")
import pip
from pip._internal import main
#main(['install', '--upgrade', 'pip'])
from os import listdir,path
#from pip._internal.utils.misc import get_installed_distributions
import re
import 电机计算新
class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        loadUi('../电机飞轮/ui/zhucuangti.ui',self)
        #self.安装包差异=self.安装包检查()
        #self.依赖包差异=self.依赖包检查()

        #self.child = ChildrenForm()  # self.child = children()生成子窗口实例self.child
        #self.child2 = ChildrenForm2()
        #self.gridLayout_2.addWidget(self.child)
        self.bangzu=bangzu()
        '''self.fileOpen.triggered.connect(self.openMsg)  # 菜单的点击事件是triggered
        self.fileClose.triggered.connect(self.close)
        self.actionTst.triggered.connect(self.childShow)  # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中'''
    def childShow(self):
        #self.gridLayout.deleteLater()
        #self.gridLayout.addWidget(self.child)
        #self.gridLayout.itemAt(0).widget().deleteLater()
        child = ChildrenForm()
        for i in range(self.gridLayout_2.count()):
            self.gridLayout_2.itemAt(i).widget().deleteLater()
        self.gridLayout_2.addWidget(child)  # 添加子窗口
        child.show()
        return
    def childShow2(self):
        #self.gridLayout.deleteLater()
        child2=ChildrenForm2()
        for i in range(self.gridLayout_2.count()):
            self.gridLayout_2.itemAt(i).widget().deleteLater()
        self.gridLayout_2.addWidget(child2)  # 添加子窗口
        child2.show()
        print(5)
        return
    def dakai(self):
        self.bangzu.show()
        return
class ChildrenForm2(QtWidgets.QWidget):
    def __init__(self):
        super(ChildrenForm2, self).__init__()
        loadUi('../电机飞轮/ui/congya.ui',self)
    def jisuan(self):
        冲压电机=电机计算新.冲压电机(压力机滑块行程次数=float(self.lineEdit_9.text()),压力=float(self.lineEdit_3.text()),  \
                            冲裁厚度=float(self.lineEdit_4.text()),  \
                           电机运行系数=float(self.lineEdit_5.text()), \
                        压机效率=float(self.lineEdit_8.text()), \
                       压力机滑块行程次数与名义次数比=float(self.lineEdit.text())/float(self.lineEdit_9.text()))
        计算能量=冲压电机.电机所需功率()
        self.lineEdit_2.setText(str(计算能量))
        return
    def shzhixiaolv(self):
        if str(self.comboBox_2.currentText())=='单级传动快速压力机':
            if str(self.comboBox_3.currentText())=='自动送料':
                self.lineEdit_8.setText(str(0.25))
            elif str(self.comboBox_3.currentText())=='手工送料':
                self.lineEdit_8.setText(str(0.2))
        elif str(self.comboBox_2.currentText())=='多级传动慢速压力机':
            if str(self.comboBox_3.currentText())=='自动送料':
                self.lineEdit_8.setText(str(0.4))
            elif str(self.comboBox_3.currentText())=='手工送料':
                self.lineEdit_8.setText(str(0.3))
        elif str(self.comboBox_2.currentText())=='带拉深垫压力机':
            if str(self.comboBox_3.currentText())=='手工送料':
                self.lineEdit_8.setText(str(0.45))
        return
    def dianjiyunxing(self):
        if self.lineEdit_9.text()=='':
            self.lineEdit_5.setText(str(''))
        elif float(self.lineEdit_9.text())<20:
            self.lineEdit_5.setText(str(1.2))
        elif float(self.lineEdit_9.text())>=20 and float(self.lineEdit_9.text())<=100:
            self.lineEdit_5.setText(str(1.3))
        elif float(self.lineEdit_9.text()) > 100:
            self.lineEdit_5.setText(str('1.4-1.6'))
        return
class ChildrenForm(QtWidgets.QWidget):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        loadUi('../电机飞轮/ui/lashen.ui',self)
        #self.label.setPixmap(QPixmap("../电机飞轮/ui/运行系数.jpg"))
    def jisuan(self):
        拉深电机能量=电机计算新.拉深电机能量(压力机滑块行程次数=float(self.lineEdit_9.text()),压力=float(self.lineEdit_3.text()),  \
                            深度=float(self.lineEdit_4.text()),系数c=float(self.lineEdit_10.text()),  \
                           电机运行系数=float(self.lineEdit_5.text()), 压机效率=float(self.lineEdit_8.text()), \
                       压力机滑块行程次数与名义次数比=float(self.lineEdit.text())/float(self.lineEdit_9.text()), \
                            压边力=float(self.lineEdit_7.text()), \
                            拉深垫工作行程=float(self.lineEdit_6.text()))
        计算能量=拉深电机能量.电机所需功率()
        self.lineEdit_2.setText(str(计算能量))
        return
    def bianhuaxisu(self):
        拉深系数=list([0.55,0.60,0.65,0.70,0.75,0.80])
        系数c=list([0.8,0.77,0.74,0.70,0.67,0.64])
        位置=拉深系数.index(float(self.comboBox.currentText()))
        self.lineEdit_10.setText(str(系数c[位置]))
        return
    def shzhixiaolv(self):
        if str(self.comboBox_2.currentText())=='单级传动快速压力机':
            if str(self.comboBox_3.currentText())=='自动送料':
                self.lineEdit_8.setText(str(0.25))
            elif str(self.comboBox_3.currentText())=='手工送料':
                self.lineEdit_8.setText(str(0.2))
        elif str(self.comboBox_2.currentText())=='多级传动慢速压力机':
            if str(self.comboBox_3.currentText())=='自动送料':
                self.lineEdit_8.setText(str(0.4))
            elif str(self.comboBox_3.currentText())=='手工送料':
                self.lineEdit_8.setText(str(0.3))
        elif str(self.comboBox_2.currentText())=='带拉深垫压力机':
            if str(self.comboBox_3.currentText())=='手工送料':
                self.lineEdit_8.setText(str(0.45))
        return
    def dianjiyunxing(self):
        if self.lineEdit_9.text()=='':
            self.lineEdit_5.setText(str(''))
        elif float(self.lineEdit_9.text())<20:
            self.lineEdit_5.setText(str(1.2))
        elif float(self.lineEdit_9.text())>=20 and float(self.lineEdit_9.text())<=100:
            self.lineEdit_5.setText(str(1.3))
        elif float(self.lineEdit_9.text()) > 100:
            self.lineEdit_5.setText(str('1.4-1.6'))
        return
class bangzu(QtWidgets.QWidget):
    def __init__(self):
        super(bangzu, self).__init__()
        loadUi('../电机飞轮/ui/bangzu.ui',self)
        self.label_2.setPixmap(QPixmap("../电机飞轮/ui/bangzhu1.jpg"))
        self.label.setPixmap(QPixmap("../电机飞轮/ui/bangzu2.jpg"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())