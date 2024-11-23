# -*- coding = utf-8 -*-
# @time:2023/7/30 10:10
# Author:lizhuang
# @File:traitui.py
# @Software:PyCharm
#from traits.etsconfig.api import ETSConfig
#ETSConfig.toolkit = 'qt'
#from pyface.ui.qt4.init import toolkit_object
#toolkit = toolkit_object
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password
from traitsui.api import Item, Group, View,CheckListEditor,Handler,VGrid,HGroup,VGroup,Font,TextEditor
import pandas as pd
import re
#from traitsui.menu import ModalButtons
import sys
from pyface.api import ArrayImage, Image, ImageResource
from traitsui.api import View, VGroup, Item, ImageEditor
from decimal import Decimal
from gearclass import  gearclass
from 读取齿轮数据库 import 读取数据库
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
from datetime import datetime
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('SimSun', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
from pdf阅读3 import PdfViewer
import sys
import os

# 获取当前文件的绝对路径
current_path = os.path.abspath(__file__)

# 获取当前文件的上一级目录
parent_path = os.path.dirname(current_path)

# 获取上一级目录的上一级目录
grandparent_path = os.path.dirname(parent_path)

print("当前文件的绝对路径:", current_path)
print("上一级目录:", parent_path)
print("上上一级目录:", grandparent_path)
#sys.path.append("../三维模块")
import 齿轮三维
class test():
    def __init__(self):
        print('Python')
硬齿轮材料=读取数据库(表名称='GEARHBSH 的副本')
软齿轮材料=读取数据库(表名称='GEARHBSS 的副本')
print(list(硬齿轮材料.loc[:,'材料名称及热处理']))
弯曲应力极限类型=读取数据库(表名称='GEARFLIM')
接触应力极限类型=读取数据库(表名称='GEARHLIM')
class HouseHandler(Handler):
    def object_pool_changed(self,info):
        if info.object.module:
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
class 齿轮强度界面(HasTraits):
    module = Float(10);helix_angle = Float(15);pressure_angle = Float(20)
    #name = 'Kiruna'
    v40 = Float(160)
    #namem1 = 'AISI 2010'
    #classificationm1 = 'NV(nitrocar)'
    sh_limitm1 =Float(1500)
    sf_limitm1 = Float(460)
    #em1 = Float(206000.)
    #poissonm1 =Float( 0.3)
    #densitym1 = Float(7.83e-6)
    #brinellm1 = Float(286.6667)
    #namem2 = 'AISI 2010'
    #classificationm2 = 'NV(nitrocar)'
    sh_limitm2 = Float(1500)
    sf_limitm2 = Float(460)
    #em2 = Float(206000.)
    #poissonm2 = Float(0.3)
    #densitym2 = Float(7.83e-6)
    #brinellm2 = Float(286.6667)#布式硬度
    z1 =Float(17)
    x1 = Float(0.35)  # 变位系数
    b1 = Float(180 ) # 齿轮宽度
    bs1 =Float (180)  # 见30页bs
    #sr1 = None  # 见30页sr
    rz1 = Float(0.8)  # 齿轮表面粗糙度
    precision_grade1 = Float(6.0 ) # 齿轮等级
    shaft_diameter1 = Float(77)  # 轴直径
    schema1 = Enum([1,2,3,4,5]) # 支撑类型
    l1 = Float(266)  # 支撑距离
    s1 = Float(0)  # 支撑距离
    backlash1 = Float(0.017)  # 齿轮侧间隙
    gear_crown1 =Float (1 ) # 齿轮顶
    helix_modification1 = Float(1)  # 螺旋修改齿轮修型
    #favorable_contact1 = True  # 有利的接触
    gear_condition1 = Float(1 ) # 齿轮条件
    z2 = Float(85)
    x2 = Float(-0.35 ) # 变位系数
    b2 = Float(180)  # 齿轮宽度
    bs2 = Float(180 ) # 见30页bs
    #sr2 = None  # 见30页sr
    rz2 = Float(0.8)  # 齿轮表面粗糙度
    precision_grade2 = Float(6.0 ) # 齿轮等级
    shaft_diameter2 =Float (77 ) # 轴直径
    schema2 = Enum([1,2,3,4,5])# 支撑类型
    l2 = Float(266)  # 支撑距离
    s2 = Float(0)  # 支撑距离
    backlash2 = Float(0.017)  # 齿轮侧间隙
    gear_crown2 = Float(1 ) # 齿轮顶
    helix_modification2 =Float (1)  # 螺旋修改齿轮修型
    #favorable_contact2 = True  # 有利的接触
    gear_condition2 = Float(1 ) # 齿轮条件
    #rpm_in = Float(1450.0)  # 转速
    #p = Float(40.0 ) # 名义功率
    niu2 = Float(41185)  # 名义功率
    rpm_in2 = Float(60)
    l= Float(10000.0 ) # 使用时间小时
    #gear_box_type = Float(2 ) # 齿轮数量
    ka = Float(1)  # 使用系数
    sh_min = Float(1.2 ) # 接触应力安全系数
    sf_min = Float(1.4)  # 许用应力安全系数
    ha_p = Float(1)
    hf_p = Float(1.25 ) # 齿根高系数
    rho_fp = Float(0.38)  # 齿根圆角半径
    x = Float(0)
    rho_ao = Float(0)
    delta_ao =Float( 0)
    nc = Float(10)
    j计算 = Button('计算')
    j生成大齿轮 = Button('生成大齿轮')
    j生成小齿轮 = Button('生成小齿轮')
    安全系数大弯曲=Float(0)
    安全系数小弯曲=Float(0)
    安全系数小接触=Float(0)
    sigmafone=Float(0)
    sigmaftow=Float(0)
    sigmafpone=Float(0)
    sigmafptow=Float(0)
    sigmahone = Float(0)
    sigmahtow = Float(0)
    sigmahpone =Float(0)
    sigmahptow = Float(0)
    string_trait = Str("查阅安全系数")
    fenduyuanxiao=Float(0)
    fenduyuanda = Float(0)
    zhongxinju=Float(0)
    chonghedu=Float(0)
    中心距偏差 =  Float(-0.05)
    jn =  Float(0)
    Ebns1u =  Float(0.05)
    Ebns1d =  Float(0.05 )
    Ebns2u =  Float(0.05)
    Ebns2d =  Float(0.05)
    j计算精度 = Button('计算精度')
    大齿轮跨齿数 = Float(0)
    小齿轮跨齿数 = Float(0)
    大齿轮跨齿距 = Float(0)
    小齿轮跨齿距 = Float(0)
    jbmin=Float(0,lable='推荐最小侧间隙')
    jbn=Float(0,lable='最小侧间隙原始')
    jbnmax=Float(0,lable='最小侧间隙转换')
    tsn1=Float(0)
    tsn2=Float(0)
    小齿轮材料选择=Enum(list(硬齿轮材料.loc[:,'材料名称及热处理']))
    小齿轮硬度=Int(52)
    大齿轮材料选择=Enum(list(软齿轮材料.loc[:,'材料名称及热处理']))
    大齿轮硬度=Int(230)
    硬度参考值小齿轮=Str()
    硬度参考值大齿轮 = Str()
    材料等级选择=Enum('ML','MQ','ME')
    chsoseswbanben = Enum([2022,2023,2024])
    def 查找应力值(self,name='ML',handness=52,type=11):
        nax1=str(name+'x1')
        nax2=str(name+'x2')
        nay1=str(name+'y1')
        nay2=str(name+'y2')
        FX1=int(弯曲应力极限类型.loc[弯曲应力极限类型['极限应力类别序号']==type,nax1])
        print(FX1)
        FX2=int(弯曲应力极限类型.loc[弯曲应力极限类型['极限应力类别序号']==type,nax2])
        FY1=int(弯曲应力极限类型.loc[弯曲应力极限类型['极限应力类别序号']==type,nay1])
        FY2=int(弯曲应力极限类型.loc[弯曲应力极限类型['极限应力类别序号']==type,nay2])
        HX1=int(接触应力极限类型.loc[接触应力极限类型['极限应力类别序号']==type,nax1])
        HX2=int(接触应力极限类型.loc[接触应力极限类型['极限应力类别序号']==type,nax2])
        HY1=int(接触应力极限类型.loc[接触应力极限类型['极限应力类别序号']==type,nay1])
        HY2=int(接触应力极限类型.loc[接触应力极限类型['极限应力类别序号']==type,nay2])
        FSCOP=FY2-FY1
        HSCOP=HY2-HY1
        handsc1=FX2-FX1
        handsc2=HX2-HX1
        FX=(handness-FX1)/handsc1*FSCOP+FY1
        HX=(handness-HX1)/handsc2*HSCOP+HY1
        return FX,HX
    def _小齿轮材料选择_changed(self):
        类型=int(硬齿轮材料.loc[硬齿轮材料['材料名称及热处理']==self.小齿轮材料选择,'极限应力类别'])
        硬度下 = int(硬齿轮材料.loc[硬齿轮材料['材料名称及热处理'] == self.小齿轮材料选择, '硬度下界值'])
        硬度上= int(硬齿轮材料.loc[硬齿轮材料['材料名称及热处理'] == self.小齿轮材料选择, '硬度上界值'])
        self.硬度参考值小齿轮=str(硬度下)+'--'+str(硬度上)
        print(类型)
        小齿轮应力=self.查找应力值(name=self.材料等级选择, handness=self.小齿轮硬度, type=类型)
        #self.sf_limitm2=#弯曲极限大齿轮
        self.sf_limitm1=小齿轮应力[0]# 弯曲极限小齿轮
        #self.sh_limitm2=#接触极限大齿轮#
        self.sh_limitm1=小齿轮应力[1]#接触极限小齿轮
        self.namem1 = self.大齿轮材料选择
        return
    def _大齿轮材料选择_changed(self):
        类型=int(软齿轮材料.loc[软齿轮材料['材料名称及热处理']==self.大齿轮材料选择,'极限应力类别'])
        硬度下 = int(软齿轮材料.loc[软齿轮材料['材料名称及热处理'] == self.大齿轮材料选择, '硬度下界值'])
        硬度上= int(软齿轮材料.loc[软齿轮材料['材料名称及热处理'] == self.大齿轮材料选择, '硬度上界值'])
        self.硬度参考值大齿轮=str(硬度下)+'--'+str(硬度上)
        print(类型)
        大齿轮应力=self.查找应力值(name=self.材料等级选择, handness=self.大齿轮硬度, type=类型)
        #self.sf_limitm2=#弯曲极限大齿轮
        self.sf_limitm2=大齿轮应力[0]# 弯曲极限小齿轮
        #self.sh_limitm2=#接触极限大齿轮#
        self.sh_limitm2=大齿轮应力[1]#接触极限小齿轮
        self.namem2=self.大齿轮材料选择
        return
    def _材料等级选择_changed(self):
        self._小齿轮材料选择_changed()
        self._大齿轮材料选择_changed()
        return
    def _小齿轮硬度_changed(self):
        self._小齿轮材料选择_changed()
        self._大齿轮材料选择_changed()
        return
    def _大齿轮硬度_changed(self):
        self._小齿轮材料选择_changed()
        self._大齿轮材料选择_changed()
        return
    大齿轮工作特性=Enum(['均匀平稳','轻微振动','中等振动','强烈振动'])
    小齿轮工作特性=Enum(['均匀平稳','轻微振动','中等振动','强烈振动'])
    def _大齿轮工作特性_changed(self):
        ka = 读取数据库(表名称='GEARKA')
        self.ka=ka .loc[ka['工作机工作特性'] == self.大齿轮工作特性, self.小齿轮工作特性]
        return
    def _小齿轮工作特性_changed(self):
        self._大齿轮工作特性_changed()
        return
    j查看支撑类型 = Button('查看支撑类型')

    @observe("j查看支撑类型")
    def 查看支撑类型(self, event):
        print('a')

        default_file_path = "..\数据文件\齿轮支撑.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    @observe("j计算")
    def 计算强度(self, event):
        self.bs2=self.b2
        self.bs1=self.b2
        ii=self.z2/self.z1
        rpm_in =self.rpm_in2*ii
        print('rpm_in',rpm_in)
        niujuxiao=self.niu2/ii
        p=niujuxiao*rpm_in/9550
        print('功率=',p)
        shili=gearclass()
        shili.module = self.module
        shili.helix_angle =self.helix_angle
        shili.pressure_angle = self.pressure_angle
        #shili.name = self.name
        shili.v40 = self.v40
        #shili.namem1 = self.namem1
        #shili.classificationm1 = self.classificationm1
        shili.sh_limitm1 =self.sh_limitm1
        shili.sf_limitm1 =self.sf_limitm1#不能除以2
        #shili.em1 = self.em1
        #shili.poissonm1 =  self.poissonm1
        #shili.densitym1 = self.densitym1
        shili.brinellm1 = self.小齿轮硬度
        #shili.namem2 = self.namem2
        #shili.classificationm2 = self.classificationm2
        shili.sh_limitm2 = self.sh_limitm2
        shili.sf_limitm2 = self.sf_limitm2#不能除以2
        #shili.em2 = self.em2
        #shili.poissonm2 =self.poissonm2
        #shili.densitym2 =self.densitym2
        shili.brinellm2 =self.大齿轮硬度
        shili.z1 =self.z1
        shili.x1 = self.x1  # 变位系数
        shili.b1 = self.b1  # 齿轮宽度
        shili.bs1 = self.bs1  # 见30页bs
        #shili.sr1 = self.sr1  # 见30页sr
        shili.rz1 = self.rz1  # 齿轮表面粗糙度
        shili.precision_grade1 = self.precision_grade1  # 齿轮等级
        shili.shaft_diameter1 = self.shaft_diameter1  # 轴直径
        shili.schema1 = self.schema1  # 支撑类型
        shili.l1 = self.l1  # 支撑距离
        shili.s1 =self.s1  # 支撑距离
        shili.backlash1 =self.backlash1  # 齿轮侧间隙
        shili.gear_crown1 = self.gear_crown1  # 齿轮顶
        shili.helix_modification1 = self.helix_modification1  # 螺旋修改齿轮修型
        #shili.favorable_contact1 =self.favorable_contact1  # 有利的接触
        shili.gear_condition1 = self.gear_condition1  # 齿轮条件
        shili.z2 = self.z2
        shili.x2 =self.x2  # 变位系数
        shili.b2 =self.b2  # 齿轮宽度
        shili.bs2 = self.bs2  # 见30页bs
        #shili.sr2 = self.sr2 # 见30页sr
        shili.rz2 = self.rz2  # 齿轮表面粗糙度
        shili.precision_grade2 = self.precision_grade2  # 齿轮等级
        shili.shaft_diameter2 =self.shaft_diameter2   # 轴直径
        shili.schema2 = self.schema2 # 支撑类型
        shili.l2 = self.l2  # 支撑距离
        shili.s2 = self.s2   # 支撑距离
        shili.backlash2 = self.backlash2  # 齿轮侧间隙
        shili.gear_crown2 = self.gear_crown2  # 齿轮顶
        shili.helix_modification2 = self.helix_modification2  # 螺旋修改齿轮修型
        #shili.favorable_contact2 =  self.favorable_contact2  # 有利的接触
        shili.gear_condition2 = self.gear_condition2  # 齿轮条件
        shili.rpm_in = rpm_in  # 转速
        shili.p = p  # 名义功率
        shili.l = self.l  # 使用时间小时
        #shili.gear_box_type =self.gear_box_type  # 齿轮数量
        shili.ka = self.ka   # 使用系数
        shili.sh_min = self.sh_min  # 接触应力安全系数
        shili.sf_min =self.sf_min # 许用应力安全系数
        shili.ha_p = self.ha_p
        shili.hf_p = self.hf_p  # 齿根高系数
        shili.rho_fp =self.rho_fp  # 齿根圆角半径
        shili.x = self.x
        shili.rho_ao =self.rho_ao
        shili.delta_ao = self.delta_ao
        shili.nc = self.nc
        应力 = shili.应力计算()
        shili.应力计算()
        print(应力[0])
        print('中心距',应力[2].a)
        print('重合度', 应力[2].epsilon_alpha)
        print('分度圆大齿轮',应力[4].da)
        print('分度圆小齿轮', 应力[3].da)
        self.sigmafone =应力[1]['sigmafone']
        self.sigmaftow = 应力[1]['sigmaftwo']
        self.sigmafpone = 应力[1]['sigmafpone']
        self.sigmafptow = 应力[1]['sigmafptwo']
        self.sigmahone = 应力[0]['sigmaH']
        self.sigmahtow =应力[0]['sigmaHTwo']
        self.sigmahpone =应力[0]['sigmaHPOne']
        self.sigmahptow = 应力[0]['sigmaHPTwo']
        self.fenduyuanxiao = 应力[3].d
        self.fenduyuanda = 应力[4].d
        self.zhongxinju = 应力[2].a
        self.chonghedu = 应力[2].epsilon_gama
        self.安全系数大弯曲=self.sigmafptow/self.sigmaftow
        self.安全系数小弯曲 = self.sigmafpone/self.sigmafone
        self.安全系数小接触 = self.sigmahpone/self.sigmahone
        结果字典=应力[5]
        结果字典['安全系数大弯曲']=(self.安全系数大弯曲, '')
        结果字典['安全系数小弯曲']=(self.安全系数小弯曲, '')
        结果字典['安全系数小接触'] =(self.安全系数小接触, '')
        from 测试表格生成 import create_pdf
        create_pdf(结果字典, title='齿轮计算报告', filename='..\数据文件\齿轮.pdf')
        return 结果字典

    @observe("j计算精度")
    def a计算精度(self, event):
        结果字典=self.计算强度( event)
        from 齿轮几何计算2 import 最小侧间隙计算,计算k
        self.大齿轮跨齿数=计算k(螺旋角=self.helix_angle, 压力角=self.pressure_angle, z=self.z2, xn=self.x2, 模数=self.module)[0]
        self.大齿轮跨齿距 = 计算k(螺旋角=self.helix_angle, 压力角=self.pressure_angle, z=self.z2, xn=self.x2, 模数=self.module)[1]
        结果字典['大齿轮跨齿数'] = (self.大齿轮跨齿数, '')
        结果字典['大齿轮跨齿距'] = (self.大齿轮跨齿距, '')
        self.小齿轮跨齿数=计算k(螺旋角=self.helix_angle, 压力角=self.pressure_angle, z=self.z1, xn=self.x1, 模数=self.module)[0]
        self.小齿轮跨齿距 = 计算k(螺旋角=self.helix_angle, 压力角=self.pressure_angle, z=self.z1, xn=self.x1, 模数=self.module)[1]
        结果字典['小齿轮跨齿数'] = (self.小齿轮跨齿数, '')
        结果字典['小齿轮跨齿距'] = (self.小齿轮跨齿距, '')
        a=最小侧间隙计算(中心距=float(结果字典['中心距.a'][0]) , 模数=self.module, 压力角=self.pressure_angle, 中心距偏差=self.中心距偏差, jn=self.jn, Ebns1u=self.Ebns1u, Ebns1d=self.Ebns1d, Ebns2u=self.Ebns2u, Ebns2d=self.Ebns2d)
        self.jbmin=a[0]
        self.jbn=a[1]
        self.jbnmax=a[2]
        self.tsn1=a[3]
        self.tsn2=a[4]
        结果字典['jbmin'] = (self.jbmin, '')
        结果字典['jbn'] = (self.jbnmax, '')
        结果字典['tsn1'] = (self.tsn1, '')
        结果字典['tsn2'] = (self.tsn2, '')
        结果字典['jbnmax'] = (self.jbnmax, '')
        from 测试表格生成 import create_pdf
        create_pdf(结果字典, title='齿轮计算报告', filename='..\数据文件\齿轮.pdf')
        return
    @observe("j生成大齿轮")
    def a生成三维大齿轮(self,event):
        结果=self.计算强度( event)
        from 齿轮三维 import opendoc,opendoczhichi
        #path1=r'E:/机械设计诺顿资料/mechanical-design-program-4-master/gearbox/spurgear_betanotzero_wheel_mm.SLDPRT'
        print('aa',结果['大齿轮齿根圆直径df'][0])
        print('aa',结果['大齿轮分度圆直径d'][0])
        print('aa',结果['大齿轮齿顶圆直径da'][0])
        print('s',结果['大齿轮s'][0])
        print('sa',结果['大齿轮sa'][0])
        print('sf',结果['大齿轮sf'][0])
        from math import tan,pi
        print(int(self.chsoseswbanben))
        if 结果['大齿轮螺旋角beta'][0]==0:
            opendoczhichi(D1Sketch1=float(结果['大齿轮齿根圆直径df'][0]) / 1000,
                    D1BaseExtrude=float(结果['大齿轮齿宽b'][0]) / 1000,
                    D1Sketch2=float(结果['大齿轮分度圆直径d'][0]) / 1000,
                    D2Sketch2=float(结果['大齿轮齿顶圆直径da'][0]) / 1000,
                    D3Sketch2=float(结果['大齿轮sa'][0]) / 1000 / 2,
                    D4Sketch2=float(结果['大齿轮s'][0]) / 1000 / 2,
                    D5Sketch2=float(结果['大齿轮sf'][0]) / 1000 / 2,  # 这里有问题
                    D1CirPattern1=float(结果['大齿轮齿数z'][0]),
                    D1Plane1=float(结果['中心距.a'][0]) / 1000,
                    banben=int(self.chsoseswbanben), )
        else:
            opendoc(D1Sketch1 =float(结果['大齿轮齿根圆直径df'][0])/1000,
                        D1BaseExtrude=float(结果['大齿轮齿宽b'][0])/1000,
                        D1Sketch2=float(结果['大齿轮分度圆直径d'][0])/1000,
                        D2Sketch2=float(结果['大齿轮齿顶圆直径da'][0])/1000,
                        D3Sketch2=float(结果['大齿轮sa'][0])/1000/2,
                        D4Sketch2=float(结果['大齿轮s'][0])/1000/2,
                        D5Sketch2=float(结果['大齿轮sf'][0])/1000/2,#这里有问题
                        D1CirPattern1=float(结果['大齿轮齿数z'][0]),
                        D1Plane1=float(结果['中心距.a'][0])/1000,
                        D4Helix1=float(pi*结果['大齿轮分度圆直径d'][0]/tan(结果['大齿轮螺旋角beta'][0]/180*pi))/1000,
                    banben=int(self.chsoseswbanben),)
        return

    @observe("j生成小齿轮")
    def a生成三维小齿轮(self, event):
        结果 = self.计算强度(event)
        from 齿轮三维 import opendoc, opendoczhichi
        # path1=r'E:/机械设计诺顿资料/mechanical-design-program-4-master/gearbox/spurgear_betanotzero_wheel_mm.SLDPRT'
        print('aa', 结果['小齿轮齿根圆直径df'][0])
        print('aa', 结果['小齿轮分度圆直径d'][0])
        print('aa', 结果['小齿轮齿顶圆直径da'][0])
        print('s', 结果['小齿轮s'][0])
        print('sa', 结果['小齿轮sa'][0])
        print('sf', 结果['小齿轮sf'][0])
        from math import tan, pi
        print(int(self.chsoseswbanben))
        if 结果['大齿轮螺旋角beta'][0] == 0:
            opendoczhichi(D1Sketch1=float(结果['小齿轮齿根圆直径df'][0]) / 1000,
                          D1BaseExtrude=float(结果['小齿轮齿宽b'][0]) / 1000,
                          D1Sketch2=float(结果['小齿轮分度圆直径d'][0]) / 1000,
                          D2Sketch2=float(结果['小齿轮齿顶圆直径da'][0]) / 1000,
                          D3Sketch2=float(结果['小齿轮sa'][0]) / 1000 / 2,
                          D4Sketch2=float(结果['小齿轮s'][0]) / 1000 / 2,
                          D5Sketch2=float(结果['小齿轮sf'][0]) / 1000 / 2,  # 这里有问题
                          D1CirPattern1=float(结果['小齿轮齿数z'][0]),
                          D1Plane1=float(结果['中心距.a'][0]) / 1000,
                          banben=int(self.chsoseswbanben), )
        else:
            opendoc(D1Sketch1=float(结果['小齿轮齿根圆直径df'][0]) / 1000,
                    D1BaseExtrude=float(结果['小齿轮齿宽b'][0]) / 1000,
                    D1Sketch2=float(结果['小齿轮分度圆直径d'][0]) / 1000,
                    D2Sketch2=float(结果['小齿轮齿顶圆直径da'][0]) / 1000,
                    D3Sketch2=float(结果['小齿轮sa'][0]) / 1000 / 2,
                    D4Sketch2=float(结果['小齿轮s'][0]) / 1000 / 2,
                    D5Sketch2=float(结果['小齿轮sf'][0]) / 1000 / 2,  # 这里有问题
                    D1CirPattern1=float(结果['小齿轮齿数z'][0]),
                    D1Plane1=float(结果['中心距.a'][0]) / 1000,
                    D4Helix1=float(pi * 结果['大齿轮分度圆直径d'][0] / tan(结果['大齿轮螺旋角beta'][0] / 180 * pi)) / 1000,
                    banben=int(self.chsoseswbanben), )
        return
    j打开pdf = Button('打开pdf')
    @observe("j打开pdf")
    def 打开pdf(self, event):
        self.计算强度( event)
        self.a计算精度(event)
        default_file_path = "..\数据文件\齿轮.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    #Item('bs2', label='大齿轮结合齿宽'), Item('bs1', label='小齿轮结合齿宽'),
    显示2 = Group(HGroup(
        VGroup(Item(label='-'),
               VGrid(Item('module', label='齿轮模数', style_sheet='*{font-size:30px}'), Item('pressure_angle', label='压力角', tooltip='28'),
                     Item('niu2', label='大齿轮扭矩'),Item('helix_angle', label='螺旋角'),
                     Item('z2', label='大齿轮齿数'), Item('z1', label='小齿轮齿数'),
                     Item('x2', label='大齿轮变位'), Item('x1', label='小齿轮变位'),
                     Item('b2', label='大齿轮齿宽'), Item('b1', label='小齿轮齿宽'),
                    Item('rpm_in2', label='大齿轮转速'),Item(label='-'),
                     Item('大齿轮工作特性', label='大齿轮工作特性'), Item('小齿轮工作特性', label='小齿轮工作特性'),
                     Item('ka', label='使用系数'),Item(label='-'),
               )), label='基本数据'),
        # Item('打印显示', style='custom', label='打印显示'),label='几何计算'),'
        HGroup(
            VGroup(Item(label='-'),
                   VGrid(Item('大齿轮材料选择', label='大齿轮材料选择'), Item('小齿轮材料选择', label='小齿轮材料选择'),
                         Item('材料等级选择', label='材料等级选择'), Item(label='-'),
                         Item('硬度参考值大齿轮', label='硬度参考值大'),Item('硬度参考值小齿轮', label='硬度参考值小'),
                         Item('大齿轮硬度', label='大齿轮硬度'), Item('小齿轮硬度', label='小齿轮硬度'),
                         Item('sf_limitm2', label='弯曲极限大齿轮'), Item('sf_limitm1', label='弯曲极限小齿轮'),
                         Item('sh_limitm2', label='接触极限大齿轮'), Item('sh_limitm1', label='接触极限小齿轮')),
                   ), label='材料选择'),
        HGroup(
            VGroup(Item(label='-'),
                   VGrid(Item('rz2', label='大齿轮表面粗糙度'), Item('rz1', label='小齿轮表面粗糙度'),
                         Item('helix_modification2', label='大齿轮螺旋修形'), Item('helix_modification1', label='小齿轮螺旋修形'),
                         Item('precision_grade2', label='大齿轮等级'),Item('precision_grade1', label='小齿轮等级'),
                         Item('gear_crown2', label='大齿轮齿轮顶'),Item('gear_crown1',label='小齿轮齿轮顶'),
                         Item('backlash2', label="大齿轮尺侧间隙"),Item('backlash1', label='小齿轮尺侧间隙'),
                         Item('ha_p', label="齿顶高"),Item('hf_p', label='齿根高'),
                         Item('rho_fp', label='圆角半径'),Item('x', label='总变位'),
                         Item('rho_ao', label='rho_ao'),Item('delta_ao', label='delta_ao'),
                         Item('nc', label='nc'))),
                    label='齿形'),
        HGroup(
            VGroup(Item(label='-'),
                   VGrid(Item('shaft_diameter2', label='大齿轮轴直径'), Item('shaft_diameter1', label='小齿轮轴直径'),
                         Item('j查看支撑类型', label='j查看支撑类型'),Item(label='-'),
                         Item('schema2', label='大齿轮支撑类型'), Item('schema1', label='小齿轮支撑类型' )
                         ,Item('l2', label='大齿轮支撑距离l'),Item('l1', label='小齿轮支撑距离l'),
                         Item('s2', label='大齿轮支撑距离s' ),Item('s1', label='小齿轮支撑距离s'),
                         #Item('gear_condition2', label='大齿轮齿轮条件'),Item('gear_condition1', label='小齿轮齿轮条件'),
                         Item('l', label='使用时间'),
                         Item('v40', label='油号'),
                         Item('sh_min', label='接触应力安全系数'),Item('sf_min', label='弯曲应力安全系数' ))),
                    label='系数条件'),
        HGroup(
            VGroup(Item(label='-'),
                   VGrid(Item('zhongxinju', label='中心距'), Item('chonghedu', label='重合度'),
                   Item('fenduyuanda', label='分度圆大齿轮'),Item('fenduyuanxiao', label='分度圆小齿轮'),
                         ),

                   Item('j计算', label="                                ", style_sheet='*{font-size:25px}'),

                   VGrid(
                       Item('sigmafptow', label='大齿轮许用弯曲应力',editor=TextEditor(format_str='%.2f')), Item('sigmafpone', label='小齿轮许用弯曲应力',editor=TextEditor(format_str='%.2f')),
                       Item('sigmaftow', label='大齿轮弯曲应力',editor=TextEditor(format_str='%.2f')), Item('sigmafone', label='小齿轮弯曲应力',editor=TextEditor(format_str='%.2f')),
                       Item('sigmahptow', label='大齿轮许用齿面应力',editor=TextEditor(format_str='%.2f')), Item('sigmahpone', label='小齿轮许用齿面应力',editor=TextEditor(format_str='%.2f')),
                       Item('sigmahtow', label='大齿轮齿面应力',editor=TextEditor(format_str='%.2f')), Item('sigmahone', label='小齿轮齿面应力',editor=TextEditor(format_str='%.2f')),
                       Item('安全系数大弯曲', label='弯曲sf大', editor=TextEditor(format_str='%.2f')),Item('安全系数小弯曲', label='弯曲sf小',editor=TextEditor(format_str='%.2f')),
                       Item('安全系数小接触', label='接触sf小', editor=TextEditor(format_str='%.2f')),Item('j打开pdf', label='j打开pdf'),
                       Item('j生成大齿轮'),Item('j生成小齿轮'),Item('chsoseswbanben'),Item('string_trait', style='readonly', label='判断条件')
                   ), ), label='计算结果'),
        HGroup( VGroup(VGrid(Item(
        "中心距偏差"),
    Item("jn"),
    Item("Ebns1u"),
    Item("Ebns1d"),
    Item("Ebns2u"),
    Item("Ebns2d")),
    Item('j计算精度') ,
    VGrid(Item('大齿轮跨齿数'),
    Item('小齿轮跨齿数'),
    Item('大齿轮跨齿距' ),
    Item('小齿轮跨齿距' ),
    Item('jbmin', label='推荐最小间隙',),
    Item('jbn'),
    Item('jbnmax' ),
    Item('tsn1' ),
    Item('tsn2')),
    Item('j打开pdf', label='j打开pdf'), ),label='公差计算')
        ,
    layout='tabbed',
        style_sheet='*{font-size:25px}')
    # Item('打印显示2', style='custom', label='打印显示2'),label='强度校核'),)
    traits_view = View(显示2,
                       title='齿轮强度计算',
                       resizable=True,
                       kind="live",
                       width=1000,
                       height=500,
                       handler=HouseHandler(),
                       )
if __name__ == '__main__': 
  test=test()
  demo = 齿轮强度界面()
  demo.configure_traits()