# -*- coding = utf-8 -*-
# @time:2023/10/30 21:40
# Author:lizhuang
# @File:涡轮蜗杆输入界面.py
# @Software:PyCharm
#from traits.etsconfig.api import ETSConfig
#ETSConfig.toolkit = 'qt'
#from pyface.ui.qt4.init import toolkit_object
#toolkit = toolkit_object
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password,Bool
from traitsui.api import Item, Group, View,CheckListEditor,Handler,VGrid,HGroup,VGroup,Font,TextEditor
import pandas as pd
import re
#from traitsui.menu import ModalButtons
import sys
from pyface.api import ArrayImage, Image, ImageResource
from traitsui.api import View, VGroup, Item, ImageEditor,EnumEditor
from traits.api import HasTraits, Directory
from decimal import Decimal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollArea, QWidget, QLabel, QFileDialog, QAction, QScrollBar, QSizePolicy
from math import *
# Dictionary of defined states and cities.
from reportlab.pdfgen import canvas
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
from datetime import datetime
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
import os
from 涡轮蜗杆计算新 import 计算涡轮
import re
from pdf阅读3 import PdfViewer
from 涡轮蜗杆计算新 import INDEX
from excel公式python版本涡轮蜗杆 import IF
from excel公式python版本涡轮蜗杆 import INDEX,CHOOSE,OR,LOG,LN,ROUND,AND,CellTransmitVal,T_Lubrication,convert_to_dms
import sqlite3
def read_table_to_dataframe(database_file, table_name):
    # 连接到数据库
    conn = sqlite3.connect(database_file)

    # 读取数据库中的数据表到 DataFrame
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)

    # 关闭数据库连接
    conn.close()

    return df
def 返回材料值(表名,列):
    列=str(列)
    #文件路径='../涡轮蜗杆计算/数据库拆分表3.xlsx'
    #数据=pd.read_excel(open(文件路径,'rb'),sheet_name=表名)
    数据 = read_table_to_dataframe('../涡轮蜗杆计算/wilumwogan.db', 表名)
    赛选数据=数据.loc[:,列]
    #赛选数据.reset_index()
    #print(type(赛选数据))
    #列=str(列)
    值=赛选数据.to_list()
    return 值
def 返回数据(表名,列,行):
    #文件路径='../涡轮蜗杆计算/数据库拆分表3.xlsx'
    #数据=pd.read_excel(open(文件路径,'rb'),sheet_name=表名)
    数据=read_table_to_dataframe('../涡轮蜗杆计算/wilumwogan.db',表名)
    值 = 数据.iloc[行, 列]
    值 = float(值)
    #赛选数据.reset_index()
    #print(type(赛选数据))
    #列=str(列)
    return 值
涡轮类型值=['ZA (A)蜗轮','ZN (N) 蜗轮','ZI (I) 蜗轮','ZK (K) 蜗轮','ZH (C) 蜗轮']
负载类型值=['A…连续的','B…轻的震动','C…中等的震动','D….重的震动']
齿轮箱的加强肋值=['无加强筋接合','晶格结构无加强筋','部分加强筋','最佳加强筋']
蜗杆材料值=返回材料值('T_MatTblWorm','材料名称(GB)')
蜗轮材料值=返回材料值('T_MatTblWheel','材料名称(GB)')
print(蜗杆材料值)
润滑油类型值=['矿物油','聚 α 稀烴油润滑 (PAO)','聚乙二醇油润滑 (PEG)']
润滑方式值=['蜗杆油浸没润滑','蜗轮油浸没润滑','油喷润滑']
润滑油值=返回材料值('T_Lubricant',1)
传动比选择=返回材料值('T_i',1)
涡轮传动选择数据=返回材料值('T_Results',1)
class 涡轮蜗杆输入界面(HasTraits):
    传动功率=Float(2.224)
    蜗杆速度=Float(900)
    传动比=Float(50)
    数值F122 = 1
    F122=Enum(传动比选择)
    数值涡轮类型 = 1
    涡轮类型=Enum(涡轮类型值)
    def _涡轮类型_changed(self):
        self.数值涡轮类型=涡轮类型值.index(self.涡轮类型)+1
        print(self.数值涡轮类型)
        return
    def _F122_changed(self):
        self.数值F122=传动比选择.index(self.F122)
        self.传动比=float(re.sub('[*]','',str(self.F122)))
        print(self.数值F122)
        return
    数值负载类型输入=1
    数值负载类型输出=1
    负载类型输入=Enum(负载类型值)
    负载类型输出=Enum(负载类型值)
    运用因素 = Float(1)
    def _负载类型输入_changed(self):
        self.数值负载类型输入=负载类型值.index(self.负载类型输入)+1
        self.运用因素=INDEX('T_KAcoef',self.数值负载类型输入,self.数值负载类型输出)
        print(self.数值负载类型输入)
        return
    def _负载类型输出_changed(self):
        self.数值负载类型输出=负载类型值.index(self.负载类型输出)+1
        print(self.数值负载类型输出)
        self.运用因素 = INDEX('T_KAcoef', self.数值负载类型输入, self.数值负载类型输出)
        return
    数值蜗杆材料 = 1
    数值蜗轮材料 = 1
    蜗杆材料 = Enum(蜗杆材料值)
    蜗轮材料 = Enum(蜗轮材料值)
    def _蜗杆材料_changed(self):
        self.数值蜗杆材料=蜗杆材料值.index(self.蜗杆材料)-2
        print(self.数值蜗杆材料)
        return
    def _蜗轮材料_changed(self):
        self.数值蜗轮材料=蜗轮材料值.index(self.蜗轮材料)
        print(self.数值蜗轮材料)
        return
    数值润滑油类型=1
    数值润滑方式=1
    数值润滑油=1
    润滑油类型=Enum(润滑油类型值)
    润滑方式=Enum(润滑方式值)
    润滑油=Enum(润滑油值)
    _ny100 = 9;_ny40 = 46;_rooil15_Input = 1.035
    def _润滑油类型_changed(self):
        self.数值润滑油类型=润滑油类型值.index(self.润滑油类型)+1
        print(self.数值润滑油类型)
        return
    def _润滑方式_changed(self):
        self.数值润滑方式=润滑方式值.index(self.润滑方式)+1
        print(self.数值润滑方式)
        return
    def _润滑油_changed(self):
        self.数值润滑油=润滑油值.index(self.润滑油)
        print(self.数值润滑油)
        self._ny100=返回数据('T_Lubricant',4,self.数值润滑油)
        self._ny40=返回数据('T_Lubricant',3,self.数值润滑油)
        self._rooil15_Input=返回数据('T_Lubricant',2,self.数值润滑油)
        print(self._rooil15_Input)
        return
    蜗杆的平均粗糙度=Float(0.5)
    期望安全时间=Float(1000)
    磨损安全=Float(1)
    蚀损安全=Float(1)
    蜗杆挠度安全=Float(1.1)
    齿强度安全=Float(1.1)
    military_service = Bool()
    齿根高系数=Float(1)
    动力头间隙=Float(0.25)
    被推荐齿根半径系数=Float(0.379950841145184)
    齿根半径系数=Float(0.379950841145184)
    蜗杆齿数=Float(1)
    轴向压力角=Float(20)
    直径率=Float(10)
    直径率选择 = Bool(True)
    蜗杆中心直径=Float(50)
    蜗杆中心直径选择= Bool(False)
    螺旋角=Float(5.7106)
    螺旋角选择=Bool(False)
    螺旋角显示 = Bool(False)
    螺旋角转换=Str()
    倾斜角选择=Enum(['右','左'])
    倾斜角=Float(1)
    _YNL=Float(1)
    def _倾斜角选择_changed(self):
        if self.倾斜角选择=='右':
           self.倾斜角=1
        else:
           self.倾斜角 = 2
        return
    模数额定值=Float(5)
    圆周齿距径节=Float()
    左轴承距离百分比=Float(50)
    右轴承距离百分比 = Float(50)
    左右轴承距离左=Float(105)
    左右轴承距离右 = Float(105)
    蜗杆表面宽度=Float(45)
    蜗轮表面宽度=Float(45)
    蜗轮齿顶修正系数=Float(0)
    参考直径=Float()
    所需圆心距当前的=Float(150)
    j计算 = Button('计算')
    安全系数磨损=Float()
    安全系数蚀损=Float()
    安全系数变形=Float()
    安全系数疲劳衰坏=Float()
    j打开pdf = Button('打开pdf')
    def _直径率选择_changed(self):
        if self.直径率选择==True:
           self.蜗杆中心直径选择=False
           self.螺旋角选择=False
        return
    def _蜗杆中心直径选择_changed(self):
        if self.蜗杆中心直径选择==True:
           self.直径率选择=False
           self.螺旋角选择=False
        return
    def _螺旋角选择_changed(self):
        if self.螺旋角选择==True:
           self.直径率选择=False
           self.蜗杆中心直径选择=False
        return
    name=Str()
    #涡轮传动选择值=1
    j涡轮传动选择=Button('参考标准')
    @observe("j涡轮传动选择")
    def 打开参考文件(self,event):
        #self.涡轮传动选择值=涡轮传动选择数据.index(self.涡轮传动选择)
        #self.模数额定值 = 返回数据('T_Results', 7, self.涡轮传动选择值)
        default_file_path = "..\数据文件\涡轮尺寸参考.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    齿侧允许磨损=Float()
    判断齿侧允许磨损=Bool(False)
    涡轮外径 = Float(265)
    涡轮外径判断值 = Bool(False)
    轮缘厚度输入=Float(10)
    轮缘厚度输入判断值 = Bool(False)
    环境温度=Float(20)
    齿轮箱的极端温度油=Float(90)
    齿轮箱的极端温度油判断值=Bool(False)
    目标最大齿轮箱温度油=Float(81.82)
    目标最大齿轮箱温度油判断值=Bool(False)
    齿轮箱表面=Float(0.3119)
    齿轮箱表面判断值=Bool(False)
    热传导效率=Float(22.39)
    热传导效率判断值=Bool(False)
    油冷却能量如果使用=Float(1.424)
    油冷却能量如果使用判断值=Bool(False)
    齿轮箱的加强肋=Enum(齿轮箱的加强肋值)
    数值齿轮箱的加强肋=Int(1)
    def _直径率_changed(self):
        #_q_calc = _d1 / _mx
        #_gama_calc = IF(_ToothType == 1, atan(_z1 / _q) * 180 / pi, asin(_z1 / _q) * 180 / pi)
        #_d1_calc = IF(_ToothType == 1, _mx * _z1 / tan(_gama * pi / 180), _mn * _z1 / sin(_gama * pi / 180)) / IF(S_Units, 1, 25.4)
        if self.直径率选择 == True:
            self.螺旋角=IF(self.数值涡轮类型 == 1, atan(self.蜗杆齿数 / self.直径率) * 180 / pi, asin(self.蜗杆齿数 /self.直径率) * 180 / pi)
            _m_temp = IF(True, self.模数额定值, 25.4 /self.模数额定值)
            if self.数值涡轮类型 == 1:
                    mx =_m_temp
                    _mn =mx*cos(self.螺旋角*pi/180)
            else:
                    _mn =_m_temp
                    mx=_mn/cos(self.螺旋角*pi/180)
            self.蜗杆中心直径=IF(self.数值涡轮类型 == 1, mx * self.蜗杆齿数 / tan(self.螺旋角 * pi / 180), _mn * self.蜗杆齿数 / sin(self.螺旋角 * pi / 180)) / IF(True, 1, 25.4)
            self.螺旋角转换 = convert_to_dms(self.螺旋角)
        return
    def _蜗杆中心直径_changed(self):
        #_q_calc = _d1 / _mx
        #_gama_calc = IF(_ToothType == 1, atan(_z1 / _q) * 180 / pi, asin(_z1 / _q) * 180 / pi)
        #_d1_calc = IF(_ToothType == 1, _mx * _z1 / tan(_gama * pi / 180), _mn * _z1 / sin(_gama * pi / 180)) / IF(S_Units, 1, 25.4)
        if self.蜗杆中心直径选择==True:
            self.螺旋角=IF(self.数值涡轮类型 == 1, atan(self.蜗杆齿数 / self.直径率) * 180 / pi, asin(self.蜗杆齿数 /self.直径率) * 180 / pi)
            _m_temp = IF(True, self.模数额定值, 25.4 /self.模数额定值)
            if self.数值涡轮类型 == 1:
                    mx =_m_temp
                    _mn =self.模数额定值*cos(self.螺旋角*pi/180)
            else:
                    _mn =_m_temp
                    mx=_mn/cos(self.螺旋角选择*pi/180)
            self.直径率=self.蜗杆中心直径/mx
            self.螺旋角转换 = convert_to_dms(self.螺旋角)
            #self.蜗杆中心直径=IF(self.数值涡轮类型 == 1, mx * self.蜗杆齿数 / tan(self.螺旋角选择 * pi / 180), _mn * self.蜗杆齿数 / sin(self.螺旋角选择 * pi / 180)) / IF(True, 1, 25.4)
        return
    def _螺旋角_changed(self):
        #_q_calc = _d1 / _mx
        #_gama_calc = IF(_ToothType == 1, atan(_z1 / _q) * 180 / pi, asin(_z1 / _q) * 180 / pi)
        #_d1_calc = IF(_ToothType == 1, _mx * _z1 / tan(_gama * pi / 180), _mn * _z1 / sin(_gama * pi / 180)) / IF(S_Units, 1, 25.4)
        if self.螺旋角选择 == True:
            #self.螺旋角=IF(self.数值涡轮类型 == 1, atan(self.蜗杆齿数 / self.直径率) * 180 / pi, asin(self.蜗杆齿数 /self.直径率) * 180 / pi)
            _m_temp = IF(True, self.模数额定值, 25.4 /self.模数额定值)
            if self.数值涡轮类型 == 1:
                    mx =_m_temp
                    _mn =mx*cos(self.螺旋角*pi/180)
            else:
                    _mn =_m_temp
                    mx=_mn/cos(self.螺旋角*pi/180)
            self.蜗杆中心直径=IF(self.数值涡轮类型 == 1, mx * self.蜗杆齿数 / tan(self.螺旋角 * pi / 180), _mn * self.蜗杆齿数 / sin(self.螺旋角 * pi / 180)) / IF(True, 1, 25.4)
            self.直径率 = self.蜗杆中心直径 / mx
            self.螺旋角转换 = convert_to_dms(self.螺旋角)
        return

    def _齿轮箱的加强肋_changed(self):
        self.数值齿轮箱的加强肋=齿轮箱的加强肋值.index(self.齿轮箱的加强肋)+1
        print(self.数值齿轮箱的加强肋)
        return
    @observe("j打开pdf")
    def 打开pdf(self, event):
        default_file_path = "..\数据文件\涡轮蜗杆.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    @observe("j计算")
    def 计算(self, event):
        返回值=计算涡轮(_PoweredWoWh=1, _Pw2_Input=self.传动功率, _n1=self.蜗杆速度, _iin=self.传动比, F122=self.数值F122, _MatP=self.数值蜗杆材料, _MatW=self.数值蜗轮材料,
             _ToothType=self.数值涡轮类型, _LoadTypeA=self.数值负载类型输入, _LoadTypeB=self.数值负载类型输出, _DesignCooling=self.数值润滑油类型, _OilType=self.数值润滑方式,
             _Lubricant=self.数值润滑油, _ny100=self._ny100, _ny40=self._ny40, _rooil15_Input=self._rooil15_Input, _Ra_Input=self.蜗杆的平均粗糙度, _KA=self.运用因素,
             _Lh=self.期望安全时间,_Sd_Proposal=self.磨损安全, _SH_proposal=self.蚀损安全, _SF_Proposal=self.蜗杆挠度安全, _SW_proposal=self.齿强度安全,
             _haXP=self.齿根高系数, _caXP=self.动力头间隙, _rf1=self.齿根半径系数, _z1_from=1, _z1_to=3,
             _SortTbl=13, _z1=self.蜗杆齿数, _d1_Input=self.蜗杆中心直径, _alfa_temp=self.轴向压力角,
             _gama=self.螺旋角, _gamaProp=3, _q=self.直径率, P163=45102, _calc_q=1,
             _TeethOrientation=self.倾斜角, _m_Input=self.模数额定值, _Module=5, _l1_proc=self.左轴承距离百分比, _l2_proc=self.右轴承距离百分比,
             _x2=self.蜗轮齿顶修正系数, _a_req1_Input=self.所需圆心距当前的, _FitAxis=3, _l1_input=self.左右轴承距离左, _l2_input=self.左右轴承距离右,
             _L_Input=self.蜗杆表面宽度, _b2H_Input=self.蜗轮表面宽度, _de2Input=self.涡轮外径,涡轮外径判断值=self.涡轮外径判断值, _BearingType=2, _deltaWlimn_Input=self.齿侧允许磨损,判断齿侧允许磨损=self.判断齿侧允许磨损,
             _SKInput=self.轮缘厚度输入,轮缘厚度输入判断值=self.轮缘厚度输入判断值, _YNL=self._YNL, _AG=1, _theta0_Input=self.环境温度, _thetaSlimInput=self.齿轮箱的极端温度油,齿轮箱的极端温度油判断=self.齿轮箱的极端温度油判断值,
             _Cooling1=1, _thetaReqInput=self.目标最大齿轮箱温度油,目标最大齿轮箱温度油判断值=self.目标最大齿轮箱温度油判断值, _GboxAreaType=self.数值齿轮箱的加强肋, _AgesInput=self.齿轮箱表面,齿轮箱表面判断值=self.齿轮箱表面判断值,
             _k_Input=self.热传导效率,热传导效率判断值=self.热传导效率判断值, _PK1_Input=self.油冷却能量如果使用,油冷却能量如果使用判断值=self.油冷却能量如果使用判断值, _Cooling2=2, _dthetaS_Input=3, _coil_Input=1900,
             _Qoil=0.028188110386212, _CastType=3, S_Units=True, _Diam_q_from=1, _Diam_q_to=18)
        self.安全系数磨损=返回值['安全系数磨损'][0]
        self.安全系数蚀损=返回值['安全系数蚀损'][0]
        self.安全系数变形=返回值['安全系数变形'][0]
        self.安全系数疲劳衰坏=返回值['安全系数疲劳'][0]
        from 测试表格生成 import create_pdf
        create_pdf(返回值, title='涡轮蜗杆计算报告', filename='../数据文件/涡轮蜗杆.pdf')
        self.齿侧允许磨损=self.设置调整参数(判断=self.判断齿侧允许磨损,计算值=返回值['齿侧允许磨损'][0],输入值=self.齿侧允许磨损)
        self.涡轮外径 = self.设置调整参数(判断=self.涡轮外径判断值, 计算值=返回值['蜗轮外径'][0], 输入值=self.涡轮外径)
        return
    def 设置调整参数(self,判断=False,计算值=1,输入值=1):
        if 判断==False:
            输出=计算值
        else:
            输出 = 输入值
        return 输出

    显示2 = Group(HGroup(VGroup(Item('传动功率', label='传动功率'),
                Item('蜗杆速度', label='蜗杆速度'),
                Item('传动比', label='传动比'),
                Item('F122', label='传动比选择'),
                Item('涡轮类型', label='涡轮类型'),
                Item('负载类型输入', label='负载类型输入'),
                Item('负载类型输出', label='负载类型输出'),
                              Item('_YNL', label='寿命精度系数'),),label='初始条件'),

                HGroup(VGroup(Item('蜗杆材料', label='蜗杆材料'),
                              Item('蜗轮材料', label='蜗轮材料'),
                              Item('润滑油类型', label='润滑油类型'),
                              Item('润滑方式', label='润滑方式'),
                              Item('润滑油', label='润滑油'),
                              Item('蜗杆的平均粗糙度', label='蜗杆的平均粗糙度'),
                              VGroup(Item('运用因素', label='运用因素'),show_border=True,enabled_when='military_service == True'),
                              Item('期望安全时间', label='期望安全时间'),
                              Item('磨损安全', label='目标磨损安全'),
                              Item('蚀损安全', label='蚀损安全'),
                              Item('蜗杆挠度安全', label='目标蜗杆挠度安全'),
                              Item('齿强度安全', label='目标齿强度安全'),
                              Item('military_service', label=''),
                              ),label='材料和加载条件'),
                HGroup(VGroup( Item('j涡轮传动选择', label='j涡轮传动选择',style_sheet='*{font-size:11px}'),
                    Item('蜗杆齿数', label='蜗杆齿数'),
                                    Item('轴向压力角', label='轴向压力角'),
                              Item('倾斜角选择', label='倾斜角'),
                              Item('模数额定值', label='模数额定值'),
                          HGroup(Group(Item('直径率', label='直径率'), show_border=False, enabled_when='直径率选择 == True'),
                                 Group(Item('直径率选择', label='直径率选择'))),
                           HGroup(Group(Item('蜗杆中心直径', label='蜗杆中心直径'), show_border=False,
                                        enabled_when='蜗杆中心直径选择 == True'), Group(Item('蜗杆中心直径选择', label='蜗杆中心直径选择'), )),
                           HGroup(Group(Item('螺旋角', label='螺旋角'), show_border=False, enabled_when='螺旋角选择 == True'),
                                  Group(Item('螺旋角选择', label='螺旋角选择'), )),Group(Item('螺旋角转换', label='螺旋角转换',enabled_when='螺旋角显示==True'))),
                              label='传动主参数'),
                HGroup(
                    VGrid(VGroup(Item('齿根高系数', label='齿根高系数'),
                              Item('动力头间隙', label='动力头间隙'),
                              Item('被推荐齿根半径系数', label='被推荐齿根半径系数'),
                              Item('齿根半径系数', label='齿根半径系数'),
                              Item('左右轴承距离左', label='左右轴承距离左'),
                              Item('左右轴承距离右', label='左右轴承距离右'),
                              Item('蜗杆表面宽度', label='蜗杆表面宽度'),
                              Item('蜗轮表面宽度', label='蜗轮表面宽度'),
                              Item('蜗轮齿顶修正系数', label='蜗轮齿顶修正系数'),
                              Item('所需圆心距当前的', label='所需圆心距当前的'),
                              )), label='齿形,安装参数'),
                HGroup(VGroup(Item('j计算', label='计算'),
                              Item('安全系数磨损', label='安全系数磨损',editor=TextEditor(format_str='%.2f')),
                              Item('安全系数蚀损', label='安全系数蚀损',editor=TextEditor(format_str='%.2f')),
                              Item('安全系数变形', label='安全系数变形',editor=TextEditor(format_str='%.2f')),
                              Item('安全系数疲劳衰坏', label='安全系数疲劳衰坏',editor=TextEditor(format_str='%.2f')),
                              Item('j打开pdf', label='j打开pdf'),
                              ), label='计算结果'),
                HGroup(VGroup(HGroup(Group(Item('齿侧允许磨损', label='齿侧允许磨损'), show_border=False, enabled_when='判断齿侧允许磨损 == True'),
                                 Group(Item('判断齿侧允许磨损', label='判断齿侧允许磨损'))),
                              HGroup(Group(Item('涡轮外径', label='涡轮外径'), show_border=False,
                                           enabled_when='涡轮外径判断值 == True'),
                                     Group(Item('涡轮外径判断值', label='涡轮外径判断值'))),
                              HGroup(Group(Item('轮缘厚度输入', label='轮缘厚度输入'), show_border=False,
                                           enabled_when='轮缘厚度输入判断值 == True'),
                                     Group(Item('轮缘厚度输入判断值', label='轮缘厚度输入判断值'))),
                              ), label='默认参数调整'),
                HGroup(VGroup(Item('环境温度', label='环境温度'),
                    HGroup(Group(Item('齿轮箱的极端温度油', label='齿轮箱的极端温度油'), show_border=False, enabled_when='齿轮箱的极端温度油判断值 == True'),
                           Group(Item('齿轮箱的极端温度油判断值', label='齿轮箱的极端温度油判断值'))),
                              Item('齿轮箱的加强肋', label='齿轮箱的加强肋'),
                    HGroup(Group(Item('齿轮箱表面', label='齿轮箱表面'), show_border=False,
                                 enabled_when='齿轮箱表面判断值 == True'),
                           Group(Item('齿轮箱表面判断值', label='齿轮箱表面判断值'))),
                    HGroup(Group(Item('热传导效率', label='热传导效率'), show_border=False,
                                 enabled_when='热传导效率判断值 == True'),
                           Group(Item('热传导效率判断值', label='热传导效率判断值'))),
                    HGroup(Group(Item('油冷却能量如果使用', label='油冷却能量如果使用'), show_border=False,
                                 enabled_when='油冷却能量如果使用判断值 == True'),
                                 Group(Item('油冷却能量如果使用判断值', label='油冷却能量如果使用判断值'))),
                    ), label='热量安全'),
                layout='tabbed',style_sheet='*{font-size:25px}')
    traits_view = View(显示2,
                       title='涡轮蜗杆计算                         制作：lizhuang',
                       resizable=True,
                       width=1200,
                       height=600,
                       kind="live",
                       )
if __name__ == '__main__':
    demo = 涡轮蜗杆输入界面()
    demo.configure_traits()
