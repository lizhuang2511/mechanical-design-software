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
class 计算当量动载荷1(HasTraits):
    fr=Float(5500)
    fa=Float(2700)
    co=Float(3520)
    a=Float(0)
    fp=Float(1.2)
    e=Float(1.454)
    x=Float(0.56)
    y=Float(1.71)
    p=Float(0)
    k1=Float(0)
    n=Float(0)
    j计算 = Button('计算')
    j查询动载荷系数=Button('查询动载荷系数')
    j查询负荷系数 = Button('查询负荷系数')
    leixing = str('深沟球轴承')
    cr=Float(0)
    cr1=Float(0)
    lh1=Float(0)
    j计算判断系数 = Button('计算判断系数')
    @observe("j计算")
    def 计算力(self, event):
        self.p=self.fp*(self.x*self.fr+self.y*self.fa)
        self.cr1=self.p*pow((60*self.n*self.lh1/1e6),1/3)
        return
    @observe("j计算判断系数")
    def 计算判断系数(self, event):
        self.e=self.fa/self.fr
        self.k1=self.fa/self.co
        return
    @observe("j查询动载荷系数")
    def 查询动载荷系数(self, event):
        if self.leixing == '角接触球轴承':
            图片名称 = '角接触球轴承系数.png'
        if self.leixing == '深沟球轴承':
            图片名称 = '深沟球轴承系数.png'
        if self.leixing == '推力球轴承':
            图片名称 = '推力轴承系数.png'
        if self.leixing == '推力滚子轴承':
            图片名称 = '推力轴承系数.png'
        if self.leixing == '调心球轴承':
            图片名称 = '其他向心球轴承系数.png'
        popup = 系数图(
            name='William Murchison',
            dept='Receiving',
            #email='wmurchison@acme.com',
            picture=ImageResource(图片名称, search_path='../滚动轴承设计/图片'),
        )
        popup.configure_traits()
        return
    @observe("j查询负荷系数")
    def 查询负荷系数(self, event):
        图片名称 = '工况系数.png'
        popup = 系数图(
            name='William Murchison',
            dept='Receiving',
            #email='wmurchison@acme.com',
            picture=ImageResource(图片名称, search_path='../滚动轴承设计/图片'),
        )
        popup.configure_traits()
        return
    显示2 = Group(Item('leixing', label='轴承类型'),
                Item('cr', label='轴承动载荷'),
                Item('fr', label='径向力'),
                Item('fa', label='轴向力'),
                Item('co', label='额定静载荷'),
                Item('a', label='接触角'),
                Item('fp', label='负荷系数'),
                Item('j查询负荷系数', label=''),
                Item('e', label='判断系数'),
                Item('k1', label='相对轴向载荷'),
                Item('j计算判断系数', label=' '),
                Item('x', label='径向载荷系数'),
                Item('y', label='轴向载荷系数'),
                Item('j查询动载荷系数', label=''),
                Item('p', label='当量动载荷'),
                Item('cr1', label='所需额定动载荷'),
                Item('j计算', label=''),style_sheet='*{font-size:25px}'
                )
    traits_view = View(显示2,
                       title='轴承计算                         制作：lizhuang',
                       resizable=True,
                       kind="live",
                       buttons=ModalButtons
                       )
class 系数图(HasTraits):
    picture = Image()
    显示=Item(
                    'picture',
                    editor=ImageEditor(
                        scale=True,
                        preserve_aspect_ratio=True,
                        allow_upscaling=True,
                    ))
    view=View(显示)
if __name__ == '__main__':
    demo = 计算当量动载荷1()
    demo.configure_traits()