# -*- coding = utf-8 -*-
# @time:2023/10/10 20:48
# Author:lizhuang
# @File:校核轴承寿命.py
# @Software:PyCharm
# -*- coding = utf-8 -*-
# @time:2023/10/10 18:12
# Author:lizhuang
# @File:计算当量动载荷.py
#from traits.etsconfig.api import ETSConfig
#ETSConfig.toolkit = 'qt'
#from pyface.ui.qt4.init import toolkit_object
#toolkit = toolkit_object
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password
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
from traitsui.menu import ModalButtons
class 校核轴承寿命1(HasTraits):
    c=Float(5500)
    p=Float(2700)
    n=Float(3520)
    t=Float(15)
    ee=Float(3)
    lh1=Float(0)
    lh=Float(1)
    ft=Float(1)
    j计算 = Button('计算')
    @observe("j计算")
    def 计算力(self, event):
        self.lh=(1e6/(60*self.n))*(self.ft*self.c/self.p)**self.ee
        return
    显示2 = Group(Item('c', label='额定动载荷'),
                Item('p', label='当量动载荷'),
                Item('n', label='轴承转速'),
                Item('t', label='工作温度'),
                Item('ee', label='寿命系数'),
                Item('lh1', label='要求寿命'),
                Item('lh', label='计算寿命'),
                Item('j计算', label=''),style_sheet='*{font-size:25px}'
                )
    traits_view = View(显示2,
                       title='轴承计算                         制作：lizhuang',
                       resizable=True,
                       kind="modal",
                       buttons=ModalButtons
                       )
if __name__ == '__main__':
    demo = 校核轴承寿命1()
    demo.configure_traits()