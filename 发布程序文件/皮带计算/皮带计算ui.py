# -*- coding = utf-8 -*-
# @time:2023/9/2 16:34
# Author:lizhuang
# @File:皮带计算ui.py
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
from 表格类 import MainForm3
from 表格类宽 import MainForm4
from math import *
# Dictionary of defined states and cities.
from reportlab.pdfgen import canvas
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
from datetime import datetime
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', '../皮带计算/联想小新黑体 常规.ttf')) #注册字体
import os
cities = {
    '普通V带': ['Z型', 'A型', 'B型', 'C型', 'D型','E型'],
    '窄V带(基准宽度制)': ['SPZ型', 'SPA型', 'SPB型', 'SPC型'],
    '窄V带(有效宽度制)': ['9N型', '15N型', '25N型'],
}


class AddressHandler(Handler):
    """
    Handler class to redefine the possible values of 'city' based on 'state'.
    This handler will be assigned to a view of an Address, and can listen and
    respond to changes in the viewed Address.
    """

    # Current list of available cities:
    cities = List(Str)

    def object_leixing_changed(self, info):
        """
        This method listens for a change in the *state* attribute of the
        object (Address) being viewed.

        When this listener method is called, *info.object* is a reference to
        the viewed object (Address).

        """
        # Change the list of available cities
        self.cities = cities[info.object.leixing]
        print('a')
        # As default value, use the first city in the list:
        info.object.带型 = self.cities[0]

class 皮带计算(HasTraits):
    leixing = Enum(list(cities.keys())[0], list(cities.keys()))
    p = Float(10)
    n1 = Float(1000)
    n2 = Float(500)
    i = Float(2)
    ka=Float()
    j查询系数 = Button('查询系数')
    jpdd = Button('计算pd')
    pdd=Float(0)
    带型=Str()
    j查询带型=Button('查询带型')
    dd1=Float(0.00)
    j查询小直径 = Button('查询小直径')
    dd20=Float()
    滑动率=Float(0.015)
    j计算dd2 = Button('计算参考大带轮直径')
    dd2 = Float(0.00)
    jdd2= Button('选定大带轮直径')
    a0=Float(0.00)
    a0min=Float(0.00)
    a0max=Float(0.00)
    j计算中心距范围 = Button('计算中心距范围')
    ld0=Float(0.00)
    j计算基准长度 = Button('计算基准长度')
    ld=Float(0.00)
    j查询ld=Button('查询ld')
    aa=Float(0.00)
    j计算实际轴间距= Button('计算实际轴间距')
    p1=Float(2.8)
    detp=Float(0.5)
    j查询detp = Button('查询单v带功率填入')
    kalf=Float(0.88)
    kl=Float(0.96)
    j查询kalf = Button('查询kalf')
    j查询kl = Button('查询kl')
    v=Float(0.00)
    alf=Float(0.00)
    z=Float(0.00)
    j计算值 = Button('计算值')
    vm=Float(0.00)
    j查询vm = Button('查询vm')
    f0=Float(0.00)
    fr=Float(0.00)
    j计算力 = Button('计算力')
    带型图 = '14.1-2.bmp'
    文件路径=Directory(os.path.join(os.path.expanduser("~"), 'Desktop'))
    j保存pdf=Button('保存pdf')
    项目名称=str('报告')
    def _leixing_changed(self):
        if self.leixing=='窄V带(基准宽度制)':
            self.带型图='14.1-3.bmp'
        elif self.leixing=='普通V带':
            self.带型图 = '14.1-2.bmp'
        elif self.leixing == '窄V带(有效宽度制)':
            self.带型图 = '14.1-4.bmp'
        print('c')
        return
    def _带型_changed(self):
        print('b')
        return
    def _n1_changed(self):
        self.i=self.n1/self.n2
        return
    def _n2_changed(self):
        self.i=self.n1/self.n2
        return
    @observe("j查询系数")
    def 查询系数(self, event):
        self.a = MainForm4(表名称='V带工况系数KA')
        self.a.signal_0.connect(self.jisuanconghe)
        self.a.show()
        return
    @observe("jpdd")
    def 计算pd(self, event):
        self.pdd=self.ka*self.p
        return
    def jisuanconghe(self,a):
        self.ka=float(a)
        return
    @observe("j查询小直径")
    def 查询小直径(self, event):
        if self.leixing=='窄V带(有效宽度制)':
            表='窄V带轮（有效宽度制）直径系列'
        else:
            表 = '普通和窄V带（基准宽度制）直径系列'
        self.a = MainForm3(表名称=表)
        self.a.signal_0.connect(self.shezhixiaozhijing)
        self.a.show()
        return
    def shezhixiaozhijing(self,a):
        self.dd1=float(a)
        return
    @observe("j查询带型")
    def 带图(self, event):
        popup = 带图(
            name='William Murchison',
            dept='Receiving',
            email='wmurchison@acme.com',
            picture=ImageResource(self.带型图, search_path='../皮带计算/图片'),
        )
        popup.configure_traits()
        return

    @observe("j计算dd2")
    def j计算dd2u(self, event):
        self.dd20 = self.dd1 * self.i*(1-self.滑动率)
        return

    @observe("jdd2")
    def 查询大带轮直径(self, event):
        if self.leixing=='窄V带(有效宽度制)':
            表='窄V带轮（有效宽度制）直径系列'
        else:
            表 = '普通和窄V带（基准宽度制）直径系列'
        self.a = MainForm3(表名称=表)
        self.a.signal_0.connect(self.shezhidd2)
        self.a.show()
        return

    def shezhidd2(self,a):
        self.dd2=float(a)
        print(float(a))
        return
    @observe("j计算中心距范围")
    def j计算a0ma(self, event):
        self.a0max = 2*(self.dd1+self.dd2)
        self.a0min = 0.7 * (self.dd1 + self.dd2)
        self.a0=self.a0min
        return
    @observe("j计算基准长度")
    def j计算基准长度1(self, event):
        self.ld0 = 2*self.a0+pi/2*(self.dd1+self.dd2)+(self.dd2-self.dd1)**2/(4*self.a0)#计算带长
        return
    @observe("j查询ld")
    def 查询ld长度(self, event):
        if self.leixing=='窄V带(有效宽度制)':
            表='有效宽度制V带的基准长度系列'
        elif self.leixing=='普通V带':
            表 = '普通V带的基准长度'
        elif self.leixing == '窄V带(基准宽度制)':
            表 = '基准宽度制V带的基准长度系列'
        self.a = MainForm3(表名称=表)
        self.a.signal_0.connect(self.szld)
        self.a.show()
        return
    def szld(self,a):
        self.ld=float(a)
        return
    @observe("j计算实际轴间距")
    def j计算实际间距(self, event):
        self.aa = self.a0+(self.ld-self.ld0)/2
        return
    @observe("j查询detp")
    def j查询detpw(self, event):
        if self.带型=='SPZ型':
          图片名称='SPZ型窄V带的额定功率.png'
        if self.带型=='SPA型':
          图片名称='SPA型窄V带的额定功率.png'
        if self.带型=='SPB型':
          图片名称='SPB型窄V带的额定功率.png'
        if self.带型=='SPC型':
          图片名称='SPC型窄V带的额定功率.png'
        if self.带型=='A型':
          图片名称='A型V带的额定功率.png'
        if self.带型=='B型':
          图片名称='B型V带的额定功率.png'
        if self.带型=='C型':
          图片名称='C型V带的额定功率.png'
        if self.带型=='D型':
          图片名称='D型V带的额定功率.png'
        if self.带型=='E型':
          图片名称='E型V带的额定功率.png'
        if self.带型=='Z型':
          图片名称='Z型V带的额定功率.png'
        if self.带型=='9N型':
          图片名称='9N、9J行窄V带饿额定功率.png'
        if self.带型=='15N型':
          图片名称='15N、15J型窄V带的额定功率.png'
        if self.带型=='25N型':
          图片名称='25N、25J型窄V带的额定功率.png'
        popup = 带图(
            name='William Murchison',
            dept='Receiving',
            email='wmurchison@acme.com',
            picture=ImageResource(图片名称, search_path='../皮带计算/图片'),
        )
        popup.configure_traits()
        return
    @observe("j查询kalf")
    def 查询kalf(self, event):
        self.a = MainForm3(表名称='包角修正系数Ka')
        self.a.signal_0.connect(self.sezhikalf)
        self.a.show()
        return
    def sezhikalf(self,a):
        self.kalf=float(a)
        return
    @observe("j查询kl")
    def 查询kl(self, event):
        if self.leixing=='窄V带(有效宽度制)':
            表='带长修正系数'
        elif self.leixing=='普通V带':
            表 = '带长修正系数（普通V带同窄V带）'
        elif self.leixing == '窄V带(基准宽度制)':
            表 = '带长修正系数（普通V带同窄V带）'
        self.a = MainForm3(表名称=表)
        self.a.signal_0.connect(self.sezhikl)
        self.a.show()
        return
    def sezhikl(self,a):
        self.kl=float(a)
        return
    @observe("j计算值")
    def 计算值(self, event):
        self.v = (pi*self.dd1*self.n1)/60/1000
        self.alf=180-(self.dd2-self.dd1)/self.aa*57.3
        self.z=self.pdd/((self.p1+self.detp)*self.kalf*self.kl)
        return
    @observe("j查询vm")
    def 查询vm(self, event):
        self.a = MainForm3(表名称='V带每米长的质量')
        self.a.signal_0.connect(self.sevm)
        self.a.show()
        return
    def sevm(self,a):
        self.vm=float(a)
        return

    @observe("j计算力")
    def 计算力(self, event):
        self.f0 = 500*(2.5/self.kalf-1)*(self.pdd/(self.z*self.v))+self.vm*self.v**2
        self.fr = 2*self.f0*self.z*sin((self.alf/180*pi)/2)
        return
    @observe("j保存pdf")
    def 计算保存pdf(self, event):
        data_array = [str(self.p), str(self.n1), str(self.n2),
                      str(self.a0), str(self.dd1),
                      str(self.pdd), str(self.z),
                      str(self.alf),
                      str(self.v), str(self.fr), str(self.ld),
                      str(self.aa),
                      str(self.带型),]
        unit_data_array = ["RPM", "RPM", "mm", "mm", "-", "-", "kW", "-", "°", "mm", "N", "mm", "mm"]
        today = datetime.now()
        today = str(today)
        report_name = self.文件路径+'/'+str(self.项目名称)+'.pdf'
        result_file = canvas.Canvas(report_name)
        result_file.setFont('song', 10)  # 设置字体字号
        result_file.setTitle("Design Report 设计报告 ")
        result_file.setFontSize(20, leading=None)
        result_file.drawString(120, 750, "Transmission System Design - Flat Belt")
        result_file.setFontSize(14, leading=None)
        result_file.drawString(150, 735, "---------------------------------------------------------------")
        result_file.drawString(250, 720, "Design Report")
        result_file.setFontSize(10, leading=None)
        global_ks=1.3
        driveTypeId=0
        # ----- Input Data -----
        result_file.drawString(245, 680, "INPUT PARAMETERS")
        result_file.drawString(120, 650, "Power 功率: ")
        result_file.drawString(120, 630, "Pinion Speed 小带轮速度: ")
        result_file.drawString(120, 610, "大带轮速度: ")
        result_file.drawString(120, 590, "Center Distance 中心距: ")
        result_file.drawString(120, 570, "Smaller/Pinion Pulley Diameter 小带轮直径: ")
        result_file.drawString(120, 550, "大带轮直径: ")
        if global_ks == 1.0:
            result_file.drawString(350, 550, "Normal")
        elif global_ks == 1.2:
            result_file.drawString(350, 550, "Steady")
        elif global_ks == 1.3:
            result_file.drawString(350, 550, str(self.dd2))
        else:
            result_file.drawString(350, 550, "Shock")
        result_file.drawString(120, 530, "带的类型 : ")
        if driveTypeId == 0:
            result_file.drawString(350, 530, str(self.leixing))
        else:
            result_file.drawString(350, 530, "Cross")
        result_file.drawString(245, 480, "OUTPUT PARAMETERS")
        result_file.drawString(120, 450, "Design Power 设计功率: ")
        result_file.drawString(120, 430, "Number Of Plies 带的数量: ")
        result_file.drawString(120, 410, "带轮包角 : ")
        result_file.drawString(120, 390, "带速: ")
        result_file.drawString(120, 370, "轴上力 : ")
        result_file.drawString(120, 350, "Belt Length (Tensioned) 带长: ")
        result_file.drawString(120, 330, "Output Pulley Diameter : 中心距")
        result_file.drawString(120, 310, "Belt Type 带的类型: ")
        # ----- Output Data -----
        x = 350
        y = 650
        hpId=0
        for var in data_array:
            if y == 550:
                y = 450
            result_file.drawString(x, y, var)
            y = y - 20
        if hpId == 0:
            result_file.drawString(450, 650, "kW")
        if hpId == 1:
            result_file.drawString(450, 650, "hp")
        x = 450
        y = 630
        for var1 in unit_data_array:
            if y == 510:
                y = 450
            result_file.drawString(x, y, var1)
            y = y - 20
        result_file.setFontSize(6, leading=None)
        result_file.drawString(100, 210, "Project by Ranjitroshan.V.S and Raghavan Kannan")
        result_file.drawString(100, 190, today)
        print(self.文件路径)
        result_file.save()
        return
    显示2 = Group(
                HGroup(VGroup(
                              Item('p', label='功率(kw)'),
                              Item('n1', label='主动转速(r/min)'),
                              Item('n2', label='被动转速(r/min)'),
                              Item('i', label='传动比'),
                    Item('leixing', label='带的类型'),
                ),label='初始条件'),
                HGroup(VGroup(VGrid(
                              Item('ka', label='系数'),Item('j查询系数', label=' '),
                              Item('jpdd', label=' '),Item('pdd', label='计算功率KW'),label='设计功率'),
                    VGrid(
                        Item('带型', label='带型',editor=EnumEditor(name='handler.cities'),), Item('j查询带型', label=' '),
                         label='选定带形'),
                    VGrid(
                        Item('dd1', label='dd1(mm)'), Item('j查询小直径', label=' '),
                        label='小带轮基准直径'),
                    VGrid(
                        Item('滑动率', label='滑动率'),Item(label='-'),
                        Item('dd20', label='dd20(mm)'), Item('j计算dd2', label=' '),
                        Item('dd2', label='选择直径(mm)'),Item('jdd2', label='选择直径(mm)'),
                        label='大带轮基准直径'),
                ),label='选定带形和直径')
                ,HGroup(VGroup(VGrid(
                              Item('a0max', label='a0max(mm)'),Item('a0min', label='a0min(mm)'),
                              Item('j计算中心距范围', label='j计算中心距范围'),Item('a0', label='轴间距(mm)'),label='初定轴间距'),
            VGrid(
                Item('ld0', label='参考长度(mm)'), Item('j计算基准长度', label='计算基准长度'),
                Item('ld', label='标准长度(mm)'), Item('j查询ld', label='查询'), label='所需基准长度'),
            VGrid(
                Item('aa', label='轴间距(mm)'), Item('j计算实际轴间距', label='j计算实际轴间距'),
                label='实际轴间距')
        ),
            label='轴间距的确定'),HGroup(VGroup(
                              Item('p1', label='单v带的功率(kw)'),
                              Item('detp', label='单v带功率增量'),
                              Item('j查询detp', label='查询功率'),
                ),label='单v带的功率'),
        HGroup(VGroup(VGrid(
            Item('kalf', label='带轮包角系数'), Item('j查询kalf', label=' '),
            Item('kl', label='带长修正系数'), Item('j查询kl', label=' '), label='设计功率'),
            Item('j计算值', label='计算值'),
        Item('v', label='带速(m/s)'),
        Item('alf', label='包角(°)'),
        Item('z', label='根数'),),label='带速包角和根数'),
        HGroup(VGroup(VGrid(
            Item('vm', label='v带质量（kg）'), Item('j查询vm', label=' '),
            Item('j计算力', label='计算力'),
            Item('f0', label='单根v带预紧力（N）'),
            Item('fr', label='轴上力(N)'),
             ),Item('文件路径', style='simple', label='pdf保存路径'),Item('项目名称', style='simple', label='项目名称'),Item('j保存pdf', style='simple', label='pdf保存')), label='各项力计算'),
                layout='tabbed',style_sheet='*{font-size:25px}')
    traits_view = View(显示2,
                       title='皮带计算                         制作：lizhuang',
                       resizable=True,
                       width=1200,
                       height=600,
                       handler=AddressHandler,
                       kind="live",
                       )
class 带图(HasTraits):
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
    demo = 皮带计算()
    demo.configure_traits()