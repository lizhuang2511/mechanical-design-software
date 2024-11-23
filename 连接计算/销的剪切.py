# -*- coding = utf-8 -*-
# @time:2023/8/8 14:38
# Author:lizhuang
# @File:销的剪切.py
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

from traitsui.extras.has_dynamic_views import DynamicView, HasDynamicViews
class 销计算(HasTraits):
    剪切力= Float(1)
    销轴直径=Float(12)
    计算应力=Float(0)
    j计算 = Button('计算')
    说明 = str('销35，45钢剪应力80-100mpa，65mn120-150mpa')
    @observe("j计算")
    def 计算应力2(self, event):
        self.计算应力=self.剪切力/(pi*(self.销轴直径/2)**2)
        return

    显示2 = Group(VGrid(Item('剪切力', label='剪切力(n)'), Item('销轴直径',label='销轴直径'),
                      Item('j计算', style='simple', label=''),Item('计算应力', style='simple', label='计算应力'),
                       ),Item('说明', style='simple', label='说明'),style_sheet='*{font-size:35px}')
    traits_view = View(显示2,
                       title='销计算                         制作：lizhuang',
                       resizable=True,
                       kind="live",
                       )
if __name__ == '__main__':
  from math import *

  demo = 销计算()
  demo.configure_traits()