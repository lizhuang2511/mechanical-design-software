# -*- coding = utf-8 -*-
# @time:2023/9/19 14:02
# Author:lizhuang
# @File:螺栓连接ui.py
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
from decimal import Decimal
from math import *
from traits.api import Bool, HasTraits, Str, Instance, Button
from 数据库读取 import read_table_to_dataframe
from traitsui.api import View, HGroup, Group, Item, Handler, Label, spring

from traitsui.extras.has_dynamic_views import DynamicView, HasDynamicViews
class 螺栓计算(HasTraits):
    轴向载荷= Float(1)
    螺栓大小=Enum('M1','M1.2','M1.6','M2','M2.5','M3','M4','M5','M6','M8','M10','M12','M16','M20','M24','M30','M36','M42','M48','M56','M64')
    螺栓材料=Enum('10','Q215-A','Q235-A','35','45','15MnVB','40Cr','30CrMnSi')
    螺栓抗拉强度=Float(380)
    螺栓屈服强度=Float(210)
    拉压疲劳强度=Float(138)
    缺口应力集中因数=Float(3)
    螺栓小径=Float(0.729)
    尺寸因数=Float(1)
    垫片材料=Enum('金属或无垫片','皮革','铜皮或石棉','橡胶')
    相对刚度=Float(0.25)
    预紧力选项=Enum('控制预紧力','不控制预紧力')
    安全系数=Float(2)
    螺纹选项 = Enum('切制螺纹', '滚制搓制螺纹')
    制造工艺因数=Float(1)
    受力选项=Enum('受压螺母', '受拉螺母')
    受力不均匀因数=Float(1)
    说明=str('控制预紧力安全因数=1.5-2.5，不控制预紧力安全因数=2.5-5')
    j计算=Button('计算')
    许用应力=Float(0)
    计算应力=Float(0)

    def _垫片材料_changed(self):
        #数据=pd.read_excel(r'../连接计算/螺栓数据.xlsx',sheet_name='刚度',)
        数据 = read_table_to_dataframe('../连接计算/luosuanshuju.db', '刚度')
        self.相对刚度=float(数据.loc[数据['材料']==self.垫片材料,'相对刚度'])
        return
    def _螺栓材料_changed(self):
        #数据=pd.read_excel(r'../连接计算/螺栓数据.xlsx',sheet_name='螺栓材料',)
        数据=read_table_to_dataframe('../连接计算/luosuanshuju.db', '螺栓材料')
        self.螺栓抗拉强度=float(数据.loc[数据['螺栓材料']==str(self.螺栓材料),'螺栓抗拉强度'])
        self.螺栓屈服强度 = float(数据.loc[数据['螺栓材料'] == str(self.螺栓材料), '螺栓屈服强度'])
        self.拉压疲劳强度 = float(数据.loc[数据['螺栓材料'] == str(self.螺栓材料), '拉压疲劳强度'])
        self.缺口应力集中因数 = float(数据.loc[数据['螺栓材料'] == str(self.螺栓材料), '缺口应力集中因数'])
        return
    def _螺栓大小_changed(self):
        #数据 = pd.read_excel(r'../连接计算/螺栓数据.xlsx', sheet_name='螺栓大小',)
        数据 = read_table_to_dataframe('../连接计算/luosuanshuju.db', '螺栓大小')
        self.螺栓小径 = float(数据.loc[数据['螺栓大小'] == self.螺栓大小, '螺栓小径'])
        self.尺寸因数 = float(数据.loc[数据['螺栓大小'] == self.螺栓大小, '尺寸因数'])
        return

    def _预紧力选项_changed(self):
        if self.预紧力选项=='不控制预紧力':
            self.安全系数=3.7
        else:
            self.安全系数=2
        return
    def _螺纹选项_changed(self):
        if self.螺纹选项=='滚制搓制螺纹':
            self.制造工艺因数=1.25
        else:
            self.制造工艺因数=1
        return
    def _受力选项_changed(self):
        if self.受力选项=='受拉螺母':
            self.受力不均匀因数=1.55
        else:
            self.受力不均匀因数=1
        return
    @observe("j计算")
    def 计算应力2(self, event):
        self.许用应力=self.尺寸因数*self.制造工艺因数*self.受力不均匀因数*self.拉压疲劳强度/self.缺口应力集中因数/self.安全系数
        self.计算应力=self.相对刚度*2*self.轴向载荷*1000/(pi*self.螺栓小径**2)
        return
    显示2 = Group(VGrid(Item('轴向载荷', label='轴向载荷(kn)'),Item(label='-'),
                Item('垫片材料', style='simple', label='垫片材料'),Item('相对刚度', style='simple', label='相对刚度'),
                Item('螺栓材料', style='simple',label='螺栓材料'),Item('螺栓抗拉强度', label='螺栓抗拉强度)'),
                Item('螺栓屈服强度', style='simple', label='螺栓屈服强度'),Item('拉压疲劳强度', style='simple', label='拉压疲劳强度'),
                Item('缺口应力集中因数', style='simple', label='缺口应力集中因数'),Item(label='-'),label='材料和受力'),
                VGrid(Item('螺栓大小', style='simple', label='螺栓大小'),Item('螺栓小径', style='simple', label='螺栓小径'),
                Item('尺寸因数', style='simple', label='尺寸因数'),Item(label='-'),label='螺栓大小'),
                VGrid(Item('预紧力选项', style='custom', label=' '),Item('安全系数', style='simple', label='   安全系数'),
                Item('受力选项', style='custom', label=' '),Item('受力不均匀因数', style='simple', label='受力不均匀因数'),
                Item('螺纹选项', style='custom', label=' '),Item('制造工艺因数', style='simple', label='制造工艺因数'),label='系数'),
                Item('说明', style='simple', label='安全因数说明'),
                Item('j计算', style='simple', label=' '),
                Item('许用应力', style='simple', label='许用应力(mpa) '),
                Item('计算应力', style='simple', label='计算应力(mpa) '),
    style_sheet='*{font-size:20px}')
    traits_view = View(显示2,
                       title='受轴向载荷紧螺栓计算-动载荷                         制作：lizhuang',
                       resizable=True,
                       width=1200,
                       height=600,
                       kind="live",
                       )
from 静载荷螺栓连接ui import 静载荷轴向螺栓计算
from 横向载荷螺栓计算ui import 静载荷横向螺栓计算
class 螺栓总(HasTraits):
    foo = Instance(螺栓计算, ())
    foo2 = Instance(静载荷轴向螺栓计算, ())
    foo3 = Instance(静载荷横向螺栓计算, ())
    configure = Button('受轴向载荷紧螺栓计算-动载荷')
    configure2 = Button('受横向向载荷紧螺栓计算')
    configure3= Button('受轴向向载荷紧螺栓计算-静载荷')
    显示2 = Group(VGroup(Item(label='-')
                       ,Item('configure', show_label=False),
                       Item(label='-'),
                       Item('configure2', show_label=False),
                       Item(label='-'),
                       Item('configure3', show_label=False)
                       ),style_sheet='*{font-size:35px}')
    traits_view = View(显示2,
                       title='螺栓计算总界面         制作:lizhuang',
                       resizable=True,
                       width=400,
                       height=300,
                       kind="live",
                       )

    def _configure_changed(self):
        self.foo.configure_traits()
    def _configure3_changed(self):
        self.foo2.configure_traits()
    def _configure2_changed(self):
        self.foo3.configure_traits()


if __name__ == '__main__':
    demo = 螺栓总()
    demo.configure_traits()