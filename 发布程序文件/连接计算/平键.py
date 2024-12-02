from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float
from traitsui.api import Item, Group, View,CheckListEditor,Handler
import pandas as pd
import re
from traitsui.menu import ModalButtons
import sys
import PyQt5
import wx
import pyface
#import PySide2
class 平键校核(HasTraits):
    传递的扭矩 = Int(840000)
    轴的直径=Int(60)
    材料=Enum('钢','铸铁')
    载荷类型 = Enum('静载荷','轻微冲击载荷','冲击载荷')
    键的长度= Enum(20,36,45,56,70,90,110,140,160,180,200,220,250,280,320,360,400)
    键的类型 = Enum('A型','B型','C型')
    许用挤压应力 = Int
    截面尺寸bxh = Enum('2 x 2','3 x 3','4 x 4','5 x 5','6 x 6','8 x 7','10 x 8','12 x 8','14 x 9','16 x 10','18 x 11','20 x 12','22 x 14',
'25 x 14','28 x 16','32 x 18','36 x 20','40 x 22','45 x 25','50 x 28','56 x 32','63 x 32','70 x 36','80 x 40','90 x 45','100 x 50')
    b=Int
    h=Int
    L=Int
    高度系数=Float(0.4)
    直接力=Float
    j计算=Button('计算应力')
    j计算力 = Button('计算力')
    打印显示 = Str("")
    def 截面尺寸分割(self,值):
        尺寸=re.split("[ ]",值)
        return 尺寸
    def 选择许用应力(self,材料,载荷):
        dic={'连接工作方式':['静连接','静连接'],
             '材料':['钢','铸铁'],
             '静载荷':[135,75],
             '轻微冲击载荷':[110,60],
             '冲击载荷':[85,45]}
        df=pd.DataFrame(dic)
        许用挤压应力=int(df.loc[df.loc[:,'材料']==材料,载荷])
        self.许用挤压应力=许用挤压应力
        return df
    def _载荷类型_changed(self):
        self.选择许用应力(self.材料,self.载荷类型)
        return
    def _材料_changed(self):
        self.选择许用应力(self.材料,self.载荷类型)
        return
    def _截面尺寸bxh_changed(self):
        尺寸 = self.截面尺寸分割(self.截面尺寸bxh)
        self.b = int(尺寸[0]);
        self.h = int(尺寸[2])
        return
    def _键的长度_changed(self):
        self.L=self.键的长度
        return
    @observe("j计算力")
    def 计算力(self, event):
        self.直接力=2*self.传递的扭矩/self.轴的直径
        return
    @observe("j计算")
    def 计算应力(self, event):
        #print(int(self.键的长度+1))
        k=self.高度系数*self.h
        挤压应力值=self.直接力/(k*self.L)
        剪切应力值=self.直接力/(self.b*self.L)
        #print(计算应力值)
        self.打印显示='剪切应力值='+str(int(剪切应力值))+'    挤压应力值='+str(int(挤压应力值))
        #pyDatView.main2(sys.argv[1:])
        return 剪切应力值
    显示=Group(Group(
        Item(''),
        Group(
        Item('传递的扭矩',label='传递的扭矩(Nm)',height=-1),
        Item('轴的直径',label='轴的直径(mm)'),orientation='horizontal',layout='split'),
        Group(
            Item('j计算力', label=' '), Item('直接力', label='直接力'),
            Item('键的长度', style='simple', id="键的长度", label='键的长度(mm)'),
            Item('L', label='l(mm)', height=-1)
    , orientation='horizontal',
            layout='split'),
        Group(
            Item('截面尺寸bxh',style='simple', id="截面尺寸bxh",label='截面尺寸bxh(mm)'),
            Item('b', label='b(mm)', style='simple', id="b", height=-1, width=-1),
            Item('h', style='simple', id="h", label='h(mm)'), orientation='horizontal', layout='split')
        ,
        Group(
            Item('材料', label='材料', style='simple', id="材料", height=-1, width=-1),
            Item('载荷类型',style='simple', id="载荷类型"),
            Item('键的类型',style='simple', id="键的类型"), orientation='horizontal', layout='split'),
        Group(
            Item('许用挤压应力'),
            Item('高度系数'),
            Item('j计算', label='计算')
            , orientation='horizontal', layout='split'),
        layout='split'),
        Group(Item('打印显示', style='custom', label='打印显示')),orientation='horizontal')

    traits_view = View(
        显示,
        title='键的计算',
        resizable=True,
        width=800,
        height=400,
        kind="modal",
        buttons=ModalButtons
    )
        #return False
if __name__ == '__main__':
    demo = 平键校核()
    #demo.截面尺寸分割('2 x 2')
    #a=demo.选择许用应力('铸铁','静载荷')
    demo.configure_traits()