# -*- coding = utf-8 -*-
# @time:2023/10/8 19:46
# Author:lizhuang
# @File:设计参数界面.py
# @Software:PyCharm
# -*- coding = utf-8 -*-
# @time:2023/10/8 19:29
# Author:lizhuang
# @File:滚动轴承主界面.py
# @Software:PyCharm
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
class 设计参数界面1(HasTraits):
    fr=Float(5500)
    fa=Float(2700)
    d=Float(55)
    n=Float(1250)
    lh=Float(5000)
    t=Float(120)
    润滑方式 = Enum('油润滑', '油脂润滑',)
    '''@observe("j计算力")
    def 计算力(self, event):
        print(self.ld)
        return'''
    显示2 = Group(Item('fr', label='径向力'),
                Item('fa', label='轴向力'),
                Item('d', label='轴径直径'),
                Item('n', label='转速'),
                Item('lh', label='要求寿命'),
                Item('t', label='工作温度'),
                Item('润滑方式', label='润滑方式'),style_sheet='*{font-size:25px}'
                )
    traits_view = View(显示2,
                       title='轴承计算                         制作：lizhuang',
                       resizable=True,
                       kind="modal",
                       buttons=ModalButtons
                       )
if __name__ == '__main__':
    demo = 设计参数界面1()
    demo.configure_traits()