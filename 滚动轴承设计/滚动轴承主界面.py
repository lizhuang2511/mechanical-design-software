# -*- coding = utf-8 -*-
# @time:2023/10/8 19:29
# Author:lizhuang
# @File:滚动轴承主界面.py
# @Software:PyCharm
#from traits.etsconfig.api import ETSConfig
#ETSConfig.toolkit = 'qt'
#from pyface.ui.qt4.init import toolkit_object
#toolkit = toolkit_object
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password, Bool, Instance
from traitsui.api import Item, Group, View,CheckListEditor,Handler,VGrid,HGroup,VGroup,Font
import pandas as pd
import re
#from traitsui.menu import ModalButtons
import sys
from pyface.api import ArrayImage, Image, ImageResource
from traitsui.api import View, VGroup, Item, ImageEditor,EnumEditor
from traits.api import HasTraits, Directory
from decimal import Decimal
from math import *
# Dictionary of defined states and cities.
from reportlab.pdfgen import canvas
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
from datetime import datetime
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', '../皮带计算/联想小新黑体 常规.ttf')) #注册字体
import os
from 设计参数界面 import 设计参数界面1
from 计算当量动载荷 import 计算当量动载荷1
from 校核轴承寿命 import 校核轴承寿命1
from 选择轴承型号 import MainForm3
from PyQt5 import QtWidgets
class 滚动轴承计算(HasTraits):
    j设计参数 = Button('设计参数')
    j选择轴承型号 = Button('选择轴承型号')
    j计算当量动载荷 = Button('计算当量动载荷')
    j计算寿命 = Button('计算寿命')
    '''fr = Float(5500)
    fa = Float(2700)
    d = Float(55)
    n = Float(1250)
    lh = Float(5000)
    t = Float(120)
    润滑方式 = Enum('油润滑', '油脂润滑')'''
    设计参数界面2=设计参数界面1()
    计算当量动载荷2 = 计算当量动载荷1()
    校核轴承寿命2 = 校核轴承寿命1()
    轴承设计信息=Str("c")
    def 打印设置信息(self):
        #self.轴承设计信息='径向力'+str(self.a.lh)
        return
    @observe("j设计参数")
    def 设计参数(self, event):
        #self.设计参数界面2=设计参数界面1()
        self.设计参数界面2.configure_traits()
        self.打印设置信息()
        return
    @observe("j计算当量动载荷")
    def 计算当量动载荷(self, event):
        #self.计算当量动载荷2=计算当量动载荷1(fr=self.设计参数界面2.fr,fa=self.设计参数界面2.fa,
             #                  co=self.myshow.cor,cr=self.myshow.cr,lh1=self.设计参数界面2.lh,
             #                  n=self.设计参数界面2.n)
        self.计算当量动载荷2.fr = self.设计参数界面2.fr; self.计算当量动载荷2.fa = self.设计参数界面2.fa;
        self.计算当量动载荷2.co = self.myshow.cor; self.计算当量动载荷2.cr = self.myshow.cr; self.计算当量动载荷2.lh1 = self.设计参数界面2.lh;
        self.计算当量动载荷2.n = self.设计参数界面2.n
        self.计算当量动载荷2.leixing = self.myshow.Btype;
        self.计算当量动载荷2.configure_traits()
        print('a')
        self.打印设置信息()
        return
    @observe("j选择轴承型号")
    def 选择轴承型号(self, event):
        self.myshow = MainForm3()
        self.myshow.show()
        self.d=self.myshow.d
        return
    @observe("j计算寿命")
    def 计算寿命(self, event):
        #self.校核轴承寿命2=校核轴承寿命1(c=self.计算当量动载荷2.cr,p=self.计算当量动载荷2.p,n=self.设计参数界面2.n,
        #                     t=self.设计参数界面2.t,lh1=self.设计参数界面2.lh)
        self.校核轴承寿命2.c = self.计算当量动载荷2.cr; self.校核轴承寿命2.p = self.计算当量动载荷2.p; self.校核轴承寿命2.n = self.设计参数界面2.n;
        self.校核轴承寿命2.t = self.设计参数界面2.t; self.校核轴承寿命2.lh1 = self.设计参数界面2.lh
        self.校核轴承寿命2.configure_traits()
        self.打印设置信息()
        return
    显示2 = Group(Item('j设计参数', label=' ',style='custom'),
                Item('j选择轴承型号', label=' ',style='custom'),
                Item('j计算当量动载荷', label=' '),
                Item('j计算寿命', label=' '),
                Item('轴承设计信息', label=' '),style_sheet='*{font-size:25px}')
    traits_view = View(显示2,
                       title='轴承计算                         制作：lizhuang',
                       resizable=True,
                       width=600,
                       height=300,
                       kind="live",
                       )
if __name__ == '__main__':
    demo = 滚动轴承计算()
    demo.configure_traits()