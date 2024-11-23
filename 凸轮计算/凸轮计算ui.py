# -*- coding = utf-8 -*-
# @time:2024/11/4 14:23
# Author:lizhuang
# @File:凸轮计算ui.py
# @Software:PyCharm
import traits.api as tr
import traitsui.api as ui
from traitsui.api import View, Item, Group, Tabbed, HGroup, VGroup
import numpy as np
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password
from 转换凸轮python import cam_zhidong,huitufanhui,sanwwei

# Traits 类定义
class CamDesignParameters(tr.HasTraits):
    r0 = tr.Float(120, label="理论基园半径")
    h = tr.Float(80, label=" 行程")
    delta01 = tr.Float(122, label="推程运动角")
    deltax01 = tr.Float(58, label="远休止角")
    delta02 = tr.Float(122, label="回程运动角")
    deltax02 = tr.Float(58, label="近休止角")
    e = tr.Float(0, label="偏心距")
    rt = tr.Float(80, label="滚子半径")
    n = tr.Int(10, label="凸轮转速 (r/min)")
    M = Enum(["内等距","外等距"])#"M 取值 (-1 内等距, 1 外等距)")
    index1 = tr.Int(15, label="推程运动规律标号")
    index3 = tr.Int(35, label="回程运动规律标号")
    N1 = Enum(["顺时针","逆时针"])#tr.Int(1, label="N1 取值 (1 逆时针, -1 顺时针)")
    N2 = Enum(["偏距左侧","偏距右侧"])#tr.Int(2, label="N2 取值 (1 偏距右侧, -1 偏距左侧)")
    jcalculate = Button('绘图')
    jcalculate1 = Button('三维')
    # 按钮点击事件处理函数
    @observe("jcalculate ")
    def calculate(self, event):
        if self.M=="内等距":
           self.MM=-1
        else:
           self.MM = 1
        if self.N1=="顺时针":
           self.N11=-1
        else:
           self.N11 = 1
        if self.N2=="偏距左侧":
           self.N22=-1
        else:
           self.N22 = 1
        self.zhi = cam_zhidong(
            self.r0+self.rt, self.h, self.delta01, self.deltax01,
            self.delta02, self.deltax02, self.e, self.rt,
            self.n, self.MM, self.index1, self.index3, self.N11, self.N22
        )
        self.result, self.result2 ,self.result3= huitufanhui(self.zhi, self.delta01, self.deltax01, self.delta02,self.r0)


    @observe("jcalculate1")
    def calculate1(self, event):
        sanwwei(self.result, self.result2,self.result3)
    # TraitsUI 视图定义
    view = View(
        VGroup(
            HGroup(
                Item('r0', label='基园半径'),
                Item('h', label='行程'),
                Item('delta01', label='推程运动角'),
                Item('deltax01', label='远休止角'),
            ),
            HGroup(
                Item('delta02', label='回程运动角'),
                Item('deltax02', label='近休止角'),
                Item('e', label='偏心距'),
                Item('rt', label='滚子半径'),
            ),
            HGroup(
                Item('n', label='凸轮转速'),
                Item('M', label='M 取值'),
                Item('index1', label='推程规律标号'),
                Item('index3', label='回程规律标号'),
            ),
            HGroup(
                Item('N1', label='N1 取值'),
                Item('N2', label='N2 取值'),
            ),
            Item('jcalculate', label='计算并绘图'),
            Item('jcalculate1', label='生成3维'),
        style_sheet='*{font-size:25px}'
        ),
        title='凸轮机构设计参数输入',
        width=1000,
        height=300,
    )

# 运行 TraitsUI 界面
if __name__ == "__main__":
    params = CamDesignParameters()
    params.configure_traits()
