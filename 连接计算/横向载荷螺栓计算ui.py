# -*- coding = utf-8 -*-
# @time:2023/9/20 19:49
# Author:lizhuang
# @File:横向载荷螺栓计算ui.py
# @Software:PyCharm
# -*- coding = utf-8 -*-
# @time:2023/9/20 15:45
# Author:lizhuang
# @File:静载荷螺栓连接.py
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

from traitsui.api import View, HGroup, Group, Item, Handler, Label, spring
from 数据库读取 import read_table_to_dataframe
class 静载荷横向螺栓计算(HasTraits):
        横向载荷= Float(1)
        可靠性系数=Float(1.6)
        螺栓大小 = Enum('M1', 'M1.2', 'M1.6', 'M2', 'M2.5', 'M3', 'M4', 'M5', 'M6', 'M8', 'M10', 'M12', 'M16', 'M20', 'M24',
                    'M30', 'M36', 'M42', 'M48', 'M56', 'M64')
        机械性能等级=Enum('Class 3.6','Class 4.6','Class 4.8','Class 5.6','Class 5.8','Class 6.8','Class 8.8','Class 9.8','Class 10.9','Class 12.9')
        螺栓屈服强度=Float(180)
        螺栓小径=Float(0.729)
        接合面摩擦因数=Float(0.15)
        安全系数=Float(3.5)
        结合面数= Float(1)
        j计算 = Button('计算')
        预紧力=Float(0)
        许用应力=Float(0)
        计算应力=Float(0)

        def _螺栓大小_changed(self):
            数据 = read_table_to_dataframe('../连接计算/luosuanshuju.db', '螺栓大小')
            #数据 = pd.read_excel(r'../连接计算/螺栓数据.xlsx', sheet_name='螺栓大小',)
            self.螺栓小径 = float(数据.loc[数据['螺栓大小'] == self.螺栓大小, '螺栓小径'])
            return
        def _机械性能等级_changed(self):
            数据 = read_table_to_dataframe('../连接计算/luosuanshuju.db', '等级和屈服强度')
            #数据 = pd.read_excel(r'../连接计算/螺栓数据.xlsx', sheet_name='等级和屈服强度',)
            self.螺栓屈服强度 = float(数据.loc[数据['EN ISO 898'] == self.机械性能等级, '屈服强度'])
            return
        @observe("j计算")
        def 计算应力2(self, event):
            self.预紧力=self.横向载荷*self.可靠性系数/self.结合面数/self.接合面摩擦因数
            self.许用应力=self.螺栓屈服强度/self.安全系数
            self.计算应力=1.3*self.预紧力/((pi/4)*self.螺栓小径**2)
            return
        显示2 = Group(VGrid(Item('横向载荷', label='横向载荷(kn)'), Item('可靠性系数',label='可靠性系数'),
                          Item('螺栓大小', label='螺栓大小'), Item('螺栓小径',label='螺栓小径'),
                          Item('机械性能等级', label='机械性能等级'), Item('螺栓屈服强度',label='螺栓屈服强度'),
                          Item('接合面摩擦因数', label='接合面摩擦因数'),Item('安全系数', label='安全系数'),
                          Item('结合面数', label='结合面数')),
                    Item('j计算', label='  '),
                    Item('预紧力', label='预紧力'),
                    Item('许用应力', label='许用应力'),
                    Item('计算应力', label='计算应力'),
                    style_sheet='*{font-size:20px}')

        traits_view = View(显示2,
                           title='受横向载荷紧螺栓计算-静载荷                         制作：lizhuang',
                           resizable=True,
                           width=1200,
                           height=600,
                           kind="live",
                           )
if __name__ == '__main__':
    demo =静载荷横向螺栓计算()
    demo.configure_traits()