# -*- coding = utf-8 -*-
#creat by lizhuang
from PyQt5 import QtWidgets
#from MainForm import Ui_MainForm
#from Children import Ui_Form
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog
import subprocess
import sys
from sympy.physics.continuum_mechanics.beam import Beam as sympyBeam

sys.path.append("../A开始界面")
import 解压2
#import ftp
import pip
import pandas as pd
import sys
import PyQt5
import wx
import pyface
#import PySide2
import xlwings
#import sqlite3
import tkinter
import tkinter.messagebox
import sympy as sy
import multiprocessing
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits.axisartist import Axes
import geatpy
import pyodbc
import importlib_metadata
#PyQt5-5.15.9.dist-info
import scipy.cluster
import future
from future import standard_library
#import cmocean
#import seaborn
#import sviewgui
import reportlab
#from pip._internal import main
import reportlab.lib
#main(['install', '--upgrade', 'pip'])
from os import listdir,path
#from pip._internal.utils.misc import get_installed_distributions
import re
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.backends.backend_svg
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('SimSun', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import fitz
'''sys.path.append("../筒瓦间隙计算")
import 热锻间隙计算界面'''
from PyQt5.QtGui import QPixmap
#from pyslvs_ui.__main__ import main
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        loadUi('../A开始界面/zhujian.ui',self)
        self.数据文件夹=self.数据文件夹创建()
        #self.安装包差异=self.安装包检查()
        #self.依赖包差异=self.依赖包检查()
        self.label_8.setPixmap(QPixmap("../A开始界面/logo.png"))
        self.label_7.setPixmap(QPixmap("../A开始界面/tichi.png"))
        '''self.fileOpen.triggered.connect(self.openMsg)  # 菜单的点击事件是triggered
        self.fileClose.triggered.connect(self.close)
        self.actionTst.triggered.connect(self.childShow)  # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中'''
    '''def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)  # 在状态栏显示文件地址'''
    def 更新文件调用(self,文件):
        '''self.label_3.setText('正在更新')
        self.label_3.repaint()
        ftp1 = ftp.FTP_OP("8.130.16.246", 'lizhuang', 'lizhuang2511', 21)
        ftp1.ftp_connect()
        ftp_filename = '/程序更新/'+文件+'.tar'
        local_filename = '../'+文件+'.tar'
        # 下载文件至本地
        ftp1.download_file(ftp_filename, local_filename)
        # 上传本机文件至ftp服务器
        # ftp.upload_file('/abc_upload.jpg', local_filenaem)
        ftp1.ftp_quit()
        解压2.untar('../'+文件+'.tar', '..')
        self.label_3.setText('更新完成')'''
        return
    def pilianggengxin(self):
        self.更新文件调用('主界面')
        return
    def gengxin(self):
        '''self.label.setText('正在更新')
        self.label.repaint()
        ftp1 = ftp.FTP_OP("8.130.16.246", 'lizhuang', 'lizhuang2511', 21)
        ftp1.ftp_connect()
        ftp_filename = '/程序更新/开始界面.tar'
        local_filename = '../开始界面.tar'
        # 下载文件至本地
        ftp1.download_file(ftp_filename, local_filename)
        # 上传本机文件至ftp服务器
        # ftp.upload_file('/abc_upload.jpg', local_filenaem)
        ftp1.ftp_quit()
        解压2.untar('../开始界面.tar', '..')
        self.label.setText('更新完成')'''
        return
    def 安装包检查(self):
        登记列表=['主界面']
        #print(type(登记列表))
        filePath='../'
        安装列表=listdir(filePath)
        #print(安装列表)
        in_a_not_in_b=[]
        a=登记列表
        b=安装列表
        for _a in a:
            if _a not in b:
                in_a_not_in_b.append(_a)
        print(in_a_not_in_b)
        if len(in_a_not_in_b)>0:
            self.label_3.setText('需要安装')
        return
    def 依赖包检查(self):
        '''登记列表=['numpy']
        #安装列表=main(['list'])
        #print(安装列表)
        installed_packages = get_installed_distributions()
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
        #print(installed_packages_list)
        d = []
        for i in range(len(installed_packages_list)):
            d.append(re.split(r'=', installed_packages_list[i])[0])
        print(d)
        安装列表=d
        a = 登记列表
        b = 安装列表
        in_a_not_in_b=[]
        for _a in a:
            if _a not in b:
                in_a_not_in_b.append(_a)
        print(in_a_not_in_b)
        if len(in_a_not_in_b) > 0:
            self.label_2.setText('需要安装')'''
        return
    def yilaibao(self):
        '''#print('检查依赖包’)
        #安装列表=main(['list'])
        #main(['install', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy'])
        #main(['install', '-i','https://pypi.tuna.tsinghua.edu.cn/simple','pip==21.2.4'])
        #main(['install', '--upgrade', 'pip==21.2.4'])
        #print(sys.modules.keys())'''
        return
    def 数据文件夹创建(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        return
    def childShow3(self,item, column):
        #print(item.text(column), column)
        print(item.whatsThis(column))
        print(item.text(column))
        if item.text(column) == '运动曲线绘制':
            sys.path.append("../运动学计算")
            import 主界面
            self.运动计算界面 = 主界面.MainWindow()
            self.运动计算界面.show()
        if item.text(column) == '曲线对比数据查看':
            sys.path.append("../绘图对比")
            import 绘图对比界面
            self.绘图对比 = 绘图对比界面.MainWindow()
            self.绘图对比.show()
            print('已经打开')
        if item.text(column) == '台大设计软件':
            from pyslvs_ui.main_window import MainWindow
            self.台大软件=MainWindow()
            self.台大软件.new()
            #台大,main()
            '''import os
            os.system('python -m pyslvs_ui')
            print('已经打开')'''
            #main()
        if item.text(column) == 'n2静力计算':
            sys.path.append("../静力学")
            import n2界面程序2
            self.n2静力 = n2界面程序2.MainWindow()
            self.n2静力.show()
            print('已经打开')
        if item.text(column) == '普通压力机变频电机功率计算':
            sys.path.append("../电机飞轮")
            import 电机飞轮界面
            self.电机功率计算 = 电机飞轮界面.MainForm()
            self.电机功率计算.show()
            print('已经打开')
        #if item.text(column) == '热模锻算法':
        #    self.热锻铜瓦间隙 = 热锻间隙计算界面.wreduanjianxi()
        #    self.热锻铜瓦间隙.show()
            '''from traits.api import HasTraits, Str, Range, Enum

            class Person(HasTraits):
                name = Str('Jane Doe')
                age = Range(low=0)
                gender = Enum('female', 'male')

            person = Person(age=30)
            from traitsui.api import Item, RangeEditor, View

            person_view = View(
                Item('name'),
                Item('gender'),
                Item('age', editor=RangeEditor(mode='spinner', low=0, high=150)),
                buttons=['OK', 'Cancel'],
                resizable=True,
            )

            person.configure_traits(view=person_view)
            print('已经打开')
        if item.text(column) == 'ml优化计算':
            self.ml优化界面1 = ml优化界面.MainWindow()
            self.ml优化界面1.show()'''
            print('已经打开')
        if item.text(column) == '小松六杆计算':
            sys.path.append("../机构运动计算2")
            import 小松计算界面
            self.小松界面 = 小松计算界面.MainWindow()
            self.小松界面.show()
            print('已经打开')
        if item.text(column) == 'N2系列优化':
            sys.path.append("../优化程序")
            import n2优化界面
            self.n2优化 = n2优化界面.MainWindow()
            self.n2优化.pushButton.clicked.connect(n2优化界面.为了并发)
            self.n2优化.show()
            print('已经打开')
        if item.text(column) == '齿轮计算':
            sys.path.append("../齿轮计算")
            import 齿轮计算界面新
            self.齿轮计算 = 齿轮计算界面新.MainForm()
            self.齿轮计算.show()
            print('已经打开')
        if item.text(column) == '齿轮计算iso':
            sys.path.append("../gearbox")
            from traitui import 齿轮强度界面
            demo = 齿轮强度界面()
            demo.configure_traits()
            print('已经打开')
        if item.text(column) == '下顶料曲线绘制':
            sys.path.append("../凸轮计算")
            import fn下顶料界面
            self.下顶料计算 = fn下顶料界面.MainForm()
            self.下顶料计算.show()
            print('已经打开')

        if item.text(column) == 'N2精度补偿计算':
            sys.path.append("../设计探索")
            import n2探索界面程序
            self.n2探索计算 = n2探索界面程序.MainWindow()
            self.n2探索计算.show()
            print('已经打开')
        if item.text(column) == '齿轮几何计算':
            sys.path.append("../齿轮几何计算")
            import 齿轮几何计算界面
            import 齿轮计算小松方法
            demo = 齿轮几何计算界面.齿轮几何界面()
            demo.configure_traits()
            print('已经打开')
        if item.text(column) == '键连接':
            sys.path.append("../连接计算")
            from 平键 import 平键校核
            from 螺栓连接ui import 螺栓总
            from 销的剪切 import 销计算
            from 花键连接 import SplineParameters
            print('已经打开')
            demo2=平键校核()
            demo2.configure_traits()
        if item.text(column) == '梁模型':
            sys.path.append("../beamCalculator")
            from beam_calculator_main_window import Window
            self.梁计算 = Window()
            self.梁计算.show()
            print('已经打开')
        if item.text(column) == 'v带计算':
            sys.path.append("../皮带计算")
            from 皮带计算ui import 皮带计算
            print('已经打开')
            demo2=皮带计算()
            demo2.configure_traits()
        if item.text(column) == '螺栓连接':
            sys.path.append("../连接计算")
            from 平键 import 平键校核
            from 螺栓连接ui import 螺栓总
            from 销的剪切 import 销计算
            from 花键连接 import SplineParameters
            print('已经打开')
            demo2=螺栓总()
            demo2.configure_traits()
        if item.text(column) == '销计算':
            sys.path.append("../连接计算")
            from 平键 import 平键校核
            from 螺栓连接ui import 螺栓总
            from 销的剪切 import 销计算
            from 花键连接 import SplineParameters
            print('已经打开')
            demo2=销计算()
            demo2.configure_traits()
        if item.text(column) == '离合器计算':
            sys.path.append("../离合器计算")
            from 离合器计算界面 import Widget2
            self.离合器计算 =Widget2()
            self.离合器计算.show()
            print('已经打开')
        if item.text(column) == 'fn动力学':
            sys.path.append("../fn六连杆mbdyn动力计算")
            from fn界面程序动力 import MainWindow10
            self.fn动力学 =MainWindow10()
            self.fn动力学.show()
            print('已经打开')
        if item.text(column) == 'FN系列优化':
            sys.path.append("../FN优化计算程序")
            import fn优化界面
            self.fn系列优化 =fn优化界面.MainWindow()
            self.fn系列优化.pushButton.clicked.connect(fn优化界面.为了并发)
            self.fn系列优化.show()
            print('已经打开')
        if item.text(column) == 'ml优化计算':
            sys.path.append("../优化程序")
            import ml优化界面
            self.ml系列优化 =ml优化界面.MainWindow()
            #self.ml系列优化.pushButton.clicked.connect(ml优化界面.为了并发)
            self.ml系列优化.show()
            print('已经打开')
        if item.text(column) == '涡轮计算':
            sys.path.append("../涡轮蜗杆计算")
            from 涡轮蜗杆输入界面 import 涡轮蜗杆输入界面
            demo = 涡轮蜗杆输入界面()
            demo.configure_traits()
            print('已经打开')
        if item.text(column) == '轴承设计':
            sys.path.append("../滚动轴承设计")
            from 滚动轴承主界面 import 滚动轴承计算
            demo = 滚动轴承计算()
            demo.configure_traits()
            print('已经打开')
        if item.text(column) == '花键连接':
            sys.path.append("../连接计算")
            from 平键 import 平键校核
            from 螺栓连接ui import 螺栓总
            from 销的剪切 import 销计算
            from 花键连接 import SplineParameters
            demo = SplineParameters()
            demo.configure_traits()
            print('已经打开花键连接')
        if item.text(column) == '螺纹传动':
            sys.path.append("../螺纹传动")
            from 螺纹传动ui import ThreadInfo
            demo = ThreadInfo()
            demo.configure_traits()
            print('已经打开')
        if item.text(column) == '链传动':
            sys.path.append("../链传动")
            from 几何界面 import ChainParameters
            demo = ChainParameters()
            demo.configure_traits()
            print('已经打开')
        if item.text(column) == '压缩弹簧':
            sys.path.append("../弹簧设计")
            from 弹簧设计界面 import HelicalSpringDesignUI
            demo2 = HelicalSpringDesignUI()
            demo2.configure_traits()
            print('已经打开')
        if item.text(column) == '轴疲劳计算':
            sys.path.append("../beamCalculator")
            from 轴疲劳计算 import StressAnalysis
            demo2 = StressAnalysis()
            demo2.configure_traits()
            print('已经打开')
        if item.text(column) == 'FN伺服曲线规划':
            sys.path.append("../伺服曲线规划程序")
            import FN伺服曲线规划软件
            import 曲柄连杆机构压印工艺界面
            self.伺服曲线规划 =FN伺服曲线规划软件.MainWindow()
            self.伺服曲线规划.show()
            print('已经打开')
        if item.text(column) == '曲柄连杆伺服曲线规划':
            sys.path.append("../伺服曲线规划程序")
            import 压印工艺界面
            import 曲柄连杆机构压印工艺界面
            self.曲柄连杆机构压印工艺界面 =曲柄连杆机构压印工艺界面.MainWindow()
            self.曲柄连杆机构压印工艺界面.show()
            print('已经打开')
        if item.text(column) == '凸轮设计':
            sys.path.append("../凸轮计算")
            from 凸轮计算ui import CamDesignParameters
            demo3 = CamDesignParameters()
            demo3.configure_traits()
            print('已经打开')
        if item.text(column) == '配合查询':
            sys.path.append("../公差计算")
            import subprocess
            # 指定要运行的exe文件的路径
            exe_path = r"../公差计算/Tolerance.exe"
            # 如果需要传递参数给exe文件，可以这样做
            args = [exe_path]
            # 使用subprocess运行exe文件，并捕获输出
            result = subprocess.run(args, capture_output=True, text=True)
            # 输出exe文件的执行结果
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            print('已经打开')
        if item.text(column) == '间隙计算':
            sys.path.append("../公差计算")
            from 公差带ui import GapCalculator,calculate_gaps
            demo3 = GapCalculator()
            demo3.configure_traits()
            print('已经打开')
        if item.text(column) == '同轴度、对称度、圆跳动和全跳动公差':
            import subprocess
            # 指定要运行的exe文件的路径
            exe_path = r"../公差计算/同轴度、对称度、圆跳动和全跳动公差.exe"
            # 如果需要传递参数给exe文件，可以这样做
            args = [exe_path]
            # 使用subprocess运行exe文件，并捕获输出
            result = subprocess.run(args, capture_output=True, text=True)
            # 输出exe文件的执行结果
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            print('已经打开')
        if item.text(column) == '圆度、圆柱度公差':
            import subprocess
            # 指定要运行的exe文件的路径
            exe_path = r"../公差计算/圆度、圆柱度公差.exe"
            # 如果需要传递参数给exe文件，可以这样做
            args = [exe_path]
            # 使用subprocess运行exe文件，并捕获输出
            result = subprocess.run(args, capture_output=True, text=True)
            # 输出exe文件的执行结果
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            print('已经打开')
        if item.text(column) == '平行度、垂直度、倾斜度公差':
            import subprocess
            # 指定要运行的exe文件的路径
            exe_path = r"../公差计算/平行度、垂直度、倾斜度公差.exe"
            # 如果需要传递参数给exe文件，可以这样做
            args = [exe_path]
            # 使用subprocess运行exe文件，并捕获输出
            result = subprocess.run(args, capture_output=True, text=True)
            # 输出exe文件的执行结果
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            print('已经打开')
        if item.text(column) == '直线度、平面度公差':
            import subprocess
            # 指定要运行的exe文件的路径
            exe_path = r"../公差计算/直线度、平面度公差.exe"
            # 如果需要传递参数给exe文件，可以这样做
            args = [exe_path]
            # 使用subprocess运行exe文件，并捕获输出
            result = subprocess.run(args, capture_output=True, text=True)
            # 输出exe文件的执行结果
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            print('已经打开')
        if item.text(column) == 'notebookopen':
            import subprocess

            # 定义启动Jupyter Notebook的命令，并指定笔记本目录
            notebook_dir =r".."  # 替换为你的笔记本目录路径
            command = ["jupyter", "notebook", "--notebook-dir", notebook_dir]
            #command = ["jupyter", "lab", "--notebook-dir", notebook_dir]

            # 使用subprocess运行命令
            subprocess.Popen(command,shell=True)
        return
if __name__ == "__main__":
    import sys
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())