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
from traitsui.api import View, VGroup, Item, ImageEditor
from decimal import Decimal
from 齿轮几何计算 import 齿轮精度计算
from 齿轮计算小松方法 import 齿轮主参数计算
from PyQt5 import QtCore
class HouseHandler(Handler):

    def object_pool_changed(self,info):
        if info.object.m:
            #print info.ui.control
            #print info.ui.control.children()
            '''qtObject = info.ui.control
            palette = qtObject.palette()
            qtObject.setAutoFillBackground(True)
            palette.setColor(qtObject.backgroundRole(),QtCore.Qt.red)
            qtObject.setPalette(palette)'''
            #or with style sheets
            #info.ui.control.setStyleSheet('background-color: red')
            info.ui.control.setStyleSheet('background-color: None')
        else:
            info.ui.control.setStyleSheet('background-color: None')
class 齿轮几何界面(HasTraits):
    B=Float(0);BC=Float(0);ai=Float(0);alf=Float(20);alfb=Float(0);alfc=Float(0);au=Float(0.05);ai=Float(0);
    ax=Float(0);bi=Float(0);bu=Float(0);d1=Float(0);d2=Float(0);db1=Float(0);db2=Float(0);
    dk1=Float(0);dk2=Float(0);dr1=Float(0);dr2=Float(0);dz1=Float(0);
    dz2=Float(0);g=Float(0);h=Float(0);hk1=Float(0);hk2=Float(0);
    inva=Float(0);invαb=Float(0);k=Float(0);kf1=Float(0);kf2=Float(0);
    m=Float(10);si1=Float(0);si2=Float(0.000);sm1=Float(0);sm2=Float(0);
    su1=Float(0);su2=Float(0);w1=Float(0); w2=Float(0);
    x1=Float(0);x2=Float(0.5162);
    y=Float(0);yebx=Float(0);
    z1=Float(98);z2=Float(15);
    zm1=Float(0);zm2=Float(0);
    打印显示 = Str("")
    j计算 = Button('计算精度')
    j校核 = Button('校核')
    大齿轮行程次数 = Float(35)
    大齿轮齿厚 =Float(180)
    小齿轮齿厚 = Float(180)
    大齿轮扭矩 = Float(95870)
    传动效率 = Float(0.93)
    大齿轮齿形系数 = Float(0.142)
    齿形系数sf1 =Float(2.08)
    齿形系数sf =Float(1.8)
    齿形系数y = Float(0.104)
    大齿轮弯曲应力=Float(0)
    小齿轮弯曲应力=Float(0)
    大齿轮齿面应力=Float(0)
    小齿轮齿面应力=Float(0)
    j计算强度 = Button('计算强度')
    打印显示2 = Str("")
    j查y = Button('查y')
    j查sf=Button('查sf')
    string_trait = Str("应力小于30")
    print(1)
    调字体=Font()
    @observe("j计算")
    def 计算精度(self, event):
        齿轮精度计算1=齿轮精度计算()
        齿轮精度计算1.m=self.m;
        齿轮精度计算1.alf = self.alf;
        齿轮精度计算1.z1 = self.z1;
        齿轮精度计算1.z2 = self.z2;
        齿轮精度计算1.x1 = self.x1;
        齿轮精度计算1.x2 =self.x2;
        齿轮精度计算1.au = self.au;
        齿轮精度计算1.ai = self.ai;
        齿轮精度计算1.渐开线函数()
        齿轮精度计算1.垮齿厚()
        齿轮精度计算1.校核啮合角()
        齿轮精度计算1.齿侧间隙()
        齿轮精度计算1.重合度()
        齿轮精度计算1.数据处理()
        self.B=齿轮精度计算1.BC;self.BC=齿轮精度计算1.BC;self.alf=齿轮精度计算1.alf;self.alfb=齿轮精度计算1.alfb;self.alfc=齿轮精度计算1.alfc;self.ai=齿轮精度计算1.ai;
        self.ax=齿轮精度计算1.ax;self.bi=齿轮精度计算1.bi;self.bu=齿轮精度计算1.bu;self.d1=齿轮精度计算1.d1;self.d2=齿轮精度计算1.d2;self.db1=齿轮精度计算1.db1;self.db2=齿轮精度计算1.db2;
        self.dk1=齿轮精度计算1.dk1;self.dk2=齿轮精度计算1.dk2;self.dr1=齿轮精度计算1.dr1;self.dr2=齿轮精度计算1.dr2;self.dz1=齿轮精度计算1.dz1;
        self.dz2=齿轮精度计算1.dz2;self.g=齿轮精度计算1.g;self.h=齿轮精度计算1.h;self.hk1=齿轮精度计算1.hk1;self.hk2=齿轮精度计算1.hk2;
        self.inva=齿轮精度计算1.inva;self.invαb=齿轮精度计算1.invαb;self.k=齿轮精度计算1.k;self.kf1=齿轮精度计算1.kf1;self.kf2=齿轮精度计算1.kf2;
        self.m=齿轮精度计算1.m;self.si1=齿轮精度计算1.si1;self.si2=齿轮精度计算1.si2;self.sm1=齿轮精度计算1.sm1;self.sm2=齿轮精度计算1.sm2;
        self.su1=齿轮精度计算1.su1;self.su2=齿轮精度计算1.su2;self.w1=齿轮精度计算1.w1; self.w2=齿轮精度计算1.w2;
        self.x1=齿轮精度计算1.x1;self.x2=齿轮精度计算1.x2;
        self.y=齿轮精度计算1.y;self.yebx=齿轮精度计算1.yebx;
        self.z1=齿轮精度计算1.z1;self.z2=齿轮精度计算1.z2;
        self.zm1=齿轮精度计算1.zm1;self.zm2=齿轮精度计算1.zm2;
        print(self.d1)
        return

    @observe("j计算强度")
    def 计算强度(self, event):
        齿轮主参数计算1=齿轮主参数计算()
        齿轮主参数计算1.m = self.m;
        齿轮主参数计算1.alf = self.alf;
        齿轮主参数计算1.z1 = self.z1;
        齿轮主参数计算1.z2 = self.z2;
        齿轮主参数计算1.x1 = self.x1;
        齿轮主参数计算1.x2 = self.x2;
        齿轮主参数计算1.au = self.au;
        齿轮主参数计算1.ai = self.ai;
        齿轮主参数计算1.大齿轮行程次数=self.大齿轮行程次数
        齿轮主参数计算1.大齿轮齿厚=self.大齿轮齿厚
        齿轮主参数计算1.小齿轮齿厚=self.小齿轮齿厚
        齿轮主参数计算1.大齿轮扭矩=self.大齿轮扭矩
        齿轮主参数计算1.传动效率=self.传动效率
        齿轮主参数计算1.大齿轮齿形系数=self.大齿轮齿形系数
        齿轮主参数计算1.齿形系数sf1=self.齿形系数sf1
        齿轮主参数计算1.齿形系数sf=self.齿形系数sf
        齿轮主参数计算1.齿形系数y=self.齿形系数y
        齿轮主参数计算1.渐开线函数()
        齿轮主参数计算1.垮齿厚()
        齿轮主参数计算1.计算弯曲应力()
        齿轮主参数计算1.计算齿面应力()
        self.大齿轮弯曲应力=齿轮主参数计算1.大齿轮弯曲应力
        self.小齿轮弯曲应力=齿轮主参数计算1.小齿轮弯曲应力
        self.大齿轮齿面应力=齿轮主参数计算1.大齿轮齿面应力
        self.小齿轮齿面应力=齿轮主参数计算1.小齿轮齿面应力
        return

    @observe("j查y")
    def 查y(self, event):
        popup = 齿形y(
            name='William Murchison',
            dept='Receiving',
            email='wmurchison@acme.com',
            picture=ImageResource('img', search_path='./'),
        )
        popup.configure_traits()
        return

    @observe("j查sf")
    def 查sf(self, event):
        popup = 齿形sf(
            name='William Murchison',
            dept='Receiving',
            email='wmurchison@acme.com',
            picture=ImageResource('img_2', search_path='./'),
        )
        popup.configure_traits()
        return
    显示 = Group(HGroup(
                VGroup(Item(label='-'),
                VGrid(Item('m', label='齿轮模数',style_sheet='*{font-size:30px}'),Item('alf', label='压力角',tooltip='28'),
                      Item('z1', label='大齿轮齿数'),Item('z2', label='小齿轮齿数'),
                      Item('x1', label='大齿轮变位'), Item('x2', label='小齿轮变位'),
                      Item('au', label='中心距公差上限'), Item('ai', label='中心距公差下限')),
                      Item('j计算',label="                                ",style_sheet='*{font-size:35px}' ),
                VGrid(
                    Item('zm1', label='大齿轮跨齿数'), Item('zm2', label='小齿轮跨齿数'),
                      Item('sm1', label='大齿轮跨齿厚'), Item('sm2', label='小齿轮夸齿厚'),
                      Item('su1', label='大齿轮跨齿厚公差上限'), Item('su2', label='小齿轮跨齿厚公差上限'),
                      Item('si1', label='大齿轮跨齿厚公差下限'), Item('si2', label='小齿轮跨齿厚公差下限'),
                      Item('bu', label='齿侧间隙上限'), Item('bi', label='齿侧间隙下限'),
                      Item('ax', label='中心距'), Item('yebx', label='重合度'),
                      Item('d1', label='分度圆直径大齿轮',id='d1',style='simple'), Item('d2', label='分度圆直径小齿轮'),
                   ),
                    Item('alfc', label='正算值'),Item('invαb', label='反算值'),
                       #Item('调字体', style='custom', label='Custom')
                       ),label='几何计算'),

                #Item('打印显示', style='custom', label='打印显示'),label='几何计算'),
                HGroup(
                    VGroup(Item(label='-'),
                           VGrid(Item('大齿轮行程次数', label='大齿轮行程次数'), Item('传动效率', label='传动效率'),
                                 Item('小齿轮齿厚', label='小齿轮齿厚'), Item('大齿轮齿厚', label='大齿轮齿厚'),
                                 Item('大齿轮扭矩', label='大齿轮扭矩'),Item(label='-'),
                                 Item('大齿轮齿形系数', label='大齿轮齿形系数y'),Item('j查y',label="查询y图表",),
                                 Item('齿形系数sf1', label='小齿轮齿形系数sf1'),Item('j查sf',label="查询sf图表",),
                                 Item('齿形系数sf', label='小齿轮齿形系数sf'),
                                 Item('齿形系数y', label='小齿轮齿形系数y')),
                           Item(label='-'),
                           Item('j计算强度', label="                                ",style_sheet='*{font-size:35px}' ),
                           Item(label='-'),
                           VGrid(
                               Item('大齿轮弯曲应力', label='大齿轮弯曲应力'), Item('小齿轮弯曲应力', label='小齿轮弯曲应力'),
                               Item('大齿轮齿面应力', label='大齿轮齿面应力'), Item('小齿轮齿面应力', label='小齿轮齿面应力'),
                           ),Item('string_trait', style='readonly', label='判断条件')),label='强度校核'),layout='tabbed',style_sheet='*{font-size:25px}')
                    #Item('打印显示2', style='custom', label='打印显示2'),label='强度校核'),)

    traits_view = View(显示,
                       title='齿轮计算',
                       resizable=True,
                       kind="live",
                       width = 1000,
                       height = 500,
                       handler=HouseHandler(),

        )
class 齿形y(HasTraits):
    picture = Image()
    显示=Item(
                    'picture',
                    editor=ImageEditor(
                        scale=True,
                        preserve_aspect_ratio=True,
                        allow_upscaling=True,
                    ))
    view=View(显示)
class 齿形sf(HasTraits):
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
    demo = 齿轮几何界面()
    demo.configure_traits()

