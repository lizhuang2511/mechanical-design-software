import pandas as pd
from traits.api import HasTraits, Str, Int, Float, Enum, Bool, Instance,Button,observe,Bool,List
from traitsui.api import View, Item, HGroup, VGroup, Spring, Label, Handler,Group,EnumEditor
from 链传动修改 import 链轮计算
from pdf阅读3 import PdfViewer
import matplotlib
#matplotlib.use('TkAgg')  # 或者尝试其他后端，如 'Agg', 'GTK3Agg' 等
import matplotlib.pyplot as plt

链轮奇数偶数={'奇数':1,
      '奇偶数':2}
链奇数偶数={'偶数':1,
      '奇偶数':2}
润滑={'A…无失效':1,
'B…无污染':2,
'C…严重污染':3,
'D…无润滑':4,}
k3列表={'A平稳':[1.00,1.00,1.20],

'B轻载':[1.20,	1.30,	1.40],

'C中载':[1.40,	1.50,	1.70],
'D重载':[1.60,	1.70,	1.90],}

主动机列表={'A…均布载荷或轻度冲击':0,
'B…中等冲击':1,
'C…重度冲击':2}
链数据=pd.read_excel(r'..\链传动\链型.xlsx',sheet_name='链型iso')
链数据美标=pd.read_excel(r'..\链传动\链型.xlsx',sheet_name='链型美标')
def 读取螺纹大小(螺纹类型):
    if 螺纹类型 == '欧标':
        return list(链数据.loc[:, 'Displayed list'])  # 示例数据，请替换为实际数据
    elif 螺纹类型 == '美标':
        return list(链数据美标.loc[:, 'Displayed list'])  # 示例数据，请替换为实际数据
class ThreadInfoHandler(Handler):
    cities = List(Str)
    def object_链型_changed(self, info):
        self.cities = 读取螺纹大小(info.object.链型)
        # As default value, use the first city in the list:
        info.object.链选择 = self.cities[0]
class ChainParameters(HasTraits):
    # 定义变量，变量名保持不变，注释为输入框的标签
    _TeethOdd_1 = Enum(链轮奇数偶数.keys())  # 链轮1齿数奇数偶数
    _TeethOdd_2 = Enum(链轮奇数偶数.keys())  # 链轮2齿数奇数偶数
    _Lubrication = Enum(润滑.keys())  # 润滑类型
    _LinksEven = Enum(链奇数偶数.keys())  # 链节奇数偶数
    主动机类型=Enum(主动机列表.keys()
)
    从动机类型=Enum(k3列表.keys())
    _P1 = Float(5.5)  # 传递功率
    _n1 = Int(720)  # 小链轮速度
    _z1 = Int(21)  # 链齿轮齿数
    _C_req = Float(40.18)  # 需求轴向距离
    _ChLinks = Float(118)  # 链节数
    _K1 = Float(1)  # 齿数系数，这里假设为整数，但可能需要是Float
    _K2 = Float(1.04761910438538)  # 传动比系数
    _K3 = Float(1)  # 冲击系数 (保险系数)
    _K4 = Float(0.999113976955414)  # 轴距系数
    _K5 = Float(1)  # 润滑系数
    _K6 = Float(1)  # 温度系数
    _K7 = Enum(1,1.1,1.2)  # 寿命系数
    _n2_req = Int(276)  # 链轮转速2
    S_Units = Bool(True)  # 单位，这里使用Bool表示是否为公制单位
    _Temperature = Float(20)  # 温度
    _Density = Float(7800)  # 密度
    _Life = Int(15000)  # 工作时间
    _K9 = Float(1)  # 摩擦条件系数
    X155 = Int(1)  # 最大转速条件，这里假设为整数
    _Efficiency = Float(0.98)  # 链效率
    链型 = Enum('欧标','美标')
    链选择=Str()
    链数据欧标=链数据
    链数据美标=链数据美标
    W165 = Float(0.0117)  # W165，这里修正了原始值以符合Float类型
    _Chain_ex = Float(1)  # 链的某种系数或特征值
    _Chain_e = Float(1)  # 链的某种系数或特征值
    _Chain_s2 = Float(1)  # 链的某种系数或特征值
    _Chain_s1 = Float(1)  # 链的某种系数或特征值
    _Chain_g = Float(1)  # 链的某种系数或特征值
    _Chain_L = Float(1)  # 链的某种长度或特征值
    _Chain_d3 = Float(1)  # 滚子直径
    _Chain_d1 = Float(1)  # 销轴直径
    _Chain_b2 = Float(1)  # 链的某种宽度或特征值
    _Chain_b1 = Float(1)  # 链的某种宽度或特征值
    _RA = 2  # 这里IF不是Python内置函数，需要定义或使用其他逻辑
    _Pitch = Float(1)  # 链距
    _rows = Int(4)  # 链数
    _PiMPa = Float(1)  # 轴承压力=TblAprox("T_BPressure",_SS_Z,_v_m,"LILI")
    _OddChLinksCoeff = Float(0.8)  # 奇数链节系数
    W208 = Float(1)  # W208，这里假设为浮点数bf
    _K8 = Float(0.74)  # 链类型/摩擦系数
    _BArrea = Float(1)  # 链承载面积
    _Massm = Float(1)  # 链轮质量
    j计算 = Button('计算')
    _Sigma= Float(0)#计算压力
    _Pp= Float(0)#设计功率
    _Fu= Float(0)#张力有效圆周力
    _Fc= Float(0)#惯性力
    G9= Float(0)
    I9= Float(0)
    _PpTable=Float()
    FB=Float(0)
    需求距离判断=Bool(False)
    链节数判断=Bool(False)
    j打开pdf = Button('打开pdf')
    j计算系数 = Button('计算系数')

    @observe("j打开pdf")
    def 打开pdf(self, event):
        self.计算强度(event)
        default_file_path = "..\链传动\output_with_page_number.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    def _从动机类型_changed(self):
        self._K3 = k3列表[str(self.从动机类型)][主动机列表[str(self.主动机类型)]]
        return
    def _主动机类型_changed(self):
        self._K3 = k3列表[str(self.从动机类型)][主动机列表[str(self.主动机类型)]]
        return
    '''def _链型_changed(self):
        if str(self.链型)=='欧标':
           self.链数据11=list(链数据.loc[:, 'Displayed list'])
        else:
           self.链数据11= list(链数据美标.loc[:, 'Displayed list'])
        #self.链选择.set_value(Enum(list(self.链数据.loc[:,'Displayed list'])))
        #self.trait_set(self.链选择==Enum(list(self.链数据.loc[:,'Displayed list'])))
        return'''
    def 刷新值(self):
        结果 = 链轮计算(TeethOdd_1_value=链轮奇数偶数[str(self._TeethOdd_1)],
                  TeethOdd_2_value=链轮奇数偶数[str(self._TeethOdd_2)],
                  Lubrication_value=润滑[str(self._Lubrication)],
                  LinksEven_value=链奇数偶数[str(self._LinksEven)],
                  P1_value=self._P1,
                  n1_value=self._n1,
                  z1_value=self._z1,
                  C_req_value=self._C_req,
                  ChLinks_value=self._ChLinks,
                  K1_value=self._K1,
                  K2_value=self._K2,
                  K3_value=self._K3,
                  K4_value=self._K4,
                  K5_value=self._K5,
                  K6_value=self._K6,
                  K7_value=self._K7,
                  n2_req_value=self._n2_req,
                  S_Units_value=self.S_Units,
                  Temperature_value=self._Temperature,
                  Density_value=self._Density,
                  Life_value=self._Life,
                  K9_value=self._K9,
                  #X155_value=self.X155,
                  Efficiency_value=self._Efficiency,
                  W165_value=self.W165,
                  Chain_ex_value=self._Chain_ex,
                  Chain_e_value=self._Chain_e,
                  Chain_s2_value=self._Chain_s2,
                  Chain_s1_value=self._Chain_s1,
                  Chain_g_value=self._Chain_g,
                  Chain_L_value=self._Chain_L,
                  Chain_d3_value=self._Chain_d3,
                  Chain_d3_mm_value=self._Chain_d3,
                  Chain_d1_value=self._Chain_d1,
                  Chain_d1_mm_value=self._Chain_d1,
                  Chain_b2_value=self._Chain_b2,
                  Chain_b1_value=self._Chain_b1,
                  RA_value=self._RA,
                  Pitch_value=self._Pitch,
                  rows_value=self._rows,
                  PiMPa_value=self._PiMPa,
                  OddChLinksCoeff_value=self._OddChLinksCoeff,
                  W208_value=self.W208,  # 计算后返回
                  K8_value=self._K8,
                  BArrea_value=self._BArrea,
                  Massm_value=self._Massm,
                  G9=self.G9,
                  I9=self.I9,
                  _FB=self.FB,
                  )
        return 结果

    @observe("j计算系数")
    def 计算系数(self, event):
        结果=self.刷新值()
        self._K1=结果[9]
        self._K2= 结果[10]
        self._K4 = 结果[11]
        self._K5 = 结果[12]
        self._K6 = 结果[13]
        if self.链节数判断==False:
            self._ChLinks=结果[15]
        if self.需求距离判断 == False:
            self._C_req = round(结果[16], 4)
        结果 = self.刷新值()
        self._K1=round(结果[9],4)
        self._K2= round(结果[10],4)
        self._K4 = round(结果[11],4)
        self._K5 = round(结果[12],4)
        self._K6 = round(结果[13],4)
        if self.链节数判断==False:
            self._ChLinks=结果[15]
        if self.需求距离判断 == False:
            self._C_req = round(结果[16], 4)
        结果 = self.刷新值()
        self._K1 = round(结果[9], 4)
        self._K2 = round(结果[10], 4)
        self._K4 = round(结果[11], 2)
        self._K5 = round(结果[12], 4)
        self._K6 = round(结果[13], 4)
        if self.链节数判断 == False:
            self._ChLinks = 结果[15]
        if self.需求距离判断 == False:
            self._C_req = round(结果[16], 4)
        return
    def _链选择_changed(self):
        if self.链型=='美标':
          链数据 =self.链数据美标
        if self.链型=='欧标':
          链数据 =self.链数据欧标
        self._Chain_ex=float(链数据.loc[链数据['Displayed list']==self.链选择,'ex'].values)
        self._Chain_e=float(链数据.loc[链数据['Displayed list']==self.链选择,'e'])
        self._Chain_s2=float(链数据.loc[链数据['Displayed list']==self.链选择,'s2'])
        self._Chain_s1=float(链数据.loc[链数据['Displayed list']==self.链选择,'s1'])
        self._Chain_g=float(链数据.loc[链数据['Displayed list']==self.链选择,'g'])
        self._Chain_L=float(链数据.loc[链数据['Displayed list']==self.链选择,'l1'])
        self._Chain_d3=float(链数据.loc[链数据['Displayed list']==self.链选择,'d3'])
        self._Chain_d1=float(链数据.loc[链数据['Displayed list']==self.链选择,'d1'])
        self._Chain_b2=float(链数据.loc[链数据['Displayed list']==self.链选择,'b2'])
        self._Chain_b1=float(链数据.loc[链数据['Displayed list']==self.链选择,'b1'])
        self.w156=float(链数据.loc[链数据['Displayed list']==self.链选择,'l2'])/1000
        self._Pitch=float(链数据.loc[链数据['Displayed list']==self.链选择,'Pitch'])
        self._rows=int(链数据.loc[链数据['Displayed list']==self.链选择,'Number of rows'])
        self._BArrea = float(链数据.loc[链数据['Displayed list'] == self.链选择, 'f '])
        self.G9=float(链数据.loc[链数据['Displayed list'] == self.链选择, 'Coeficient K1'])
        self.I9 = float(链数据.loc[链数据['Displayed list'] == self.链选择, 'Coeficient K2'])
        self.FB = float(链数据.loc[链数据['Displayed list'] == self.链选择, 'FB'])
        #self.x155=float(链数据.loc[链数据['Displayed list'] == self.链选择, 'FB'])
        from excel公式python版本链传动 import CAprox
        结果=self.刷新值()
        self._Sigma = 结果[0]  # 计算压力
        self._Pp = 结果[1]  # 设计功率
        self._Fu = 结果[2]  # 张力有效圆周力
        self._Fc = 结果[3]  # 惯性力
        结果字典 = 结果[4]
        self._PiMPa=round(结果[5],2)
        self.W208=round(结果[6],2)
        self._OddChLinksCoeff=round(结果[7],2)
        self._k8 = round(结果[8], 2)
        self._Massm=float(链数据.loc[链数据['Displayed list']==self.链选择,'Q'])
        return
    @observe("j计算")
    def 计算强度(self, event):
        结果=self.刷新值()
        self._Sigma =round( 结果[0]  ,2)# 计算压力
        self._Pp = round(结果[1] ,2)  # 设计功率
        self._Fu = round(结果[2] ,2) # 张力有效圆周力
        self._Fc = round(结果[3] ,2)  # 惯性力
        结果字典={}
        结果字典['链型'] = (self.链选择, '')
        结果字典['润滑条件'] = (self._Lubrication, '')
        结果字典['主动机类型'] = (self.主动机类型, '')
        结果字典['从动机类型'] = (self.从动机类型, '')
        结果字典['_TeethOdd_1'] = (self._TeethOdd_1, '')
        结果字典['_TeethOdd_2'] = (self._TeethOdd_2, '')
        结果字典.update(结果[4])
        from 测试表格生成 import create_pdf
        create_pdf(结果字典, title='链轮计算报告', filename='..\链传动\output_with_page_number.pdf')
        return
    # 创建视图
    view = View(Group(HGroup(
        VGroup(
            HGroup(
                 Item('_TeethOdd_1', label='链轮1齿数奇数偶数'),
                 Item('_TeethOdd_2', label='链轮2齿数奇数偶数'),
            ),
            HGroup(
                Item('_Lubrication', label='润滑类型'),
               Item('_LinksEven', label='链节奇数偶数'),
            ),
            HGroup(
                Item('主动机类型', label='主动机类型'),
                Item('从动机类型', label='从动机类型'),
            ),
            HGroup(
                 Item('_P1', label='传递功率'),
                 Item('_n1', label='小链轮速度'),
            ),
            HGroup(
                Item('_z1', label='链齿轮齿数'),
                Item('_n2_req', label='链轮转速2'),
            )

            # ... 继续添加其他HGroup或VGroup ...
        ,),label='系数条件'),
        HGroup(
            VGroup(
                HGroup(Item('链型', label='链类别'), ),
                HGroup(Item('链选择', label='链选择',editor=EnumEditor(name='handler.cities'))),
            # ... 链的特定参数 ...
            HGroup(

                Item('_Chain_ex', label='Chain_ex_value'),
                Item('_Chain_e', label='Chain_e_value'),
                Item('_Chain_s2', label='Chain_s2_value'),
                Item('_Chain_s1', label='Chain_s1_value'),
            ),
            # ... 继续其他链的参数 ...
            HGroup(
                Item('_Chain_g', label='Chain_g_value'),
                Item('_Chain_L', label=' Chain_L_value'),
                Item('_Chain_d3', label='滚子直径'),
                Item('_Chain_d1', label='Chain_d1_value'),

            ),
            HGroup(
                Item('_Chain_b2', label='Chain_b2_value'),
                Item('_Chain_b1', label='链宽度或特征值'),
                Item('_Pitch', label='链距'),
            Item('_rows', label='链数'),

            ),
            HGroup(
                Item('_PiMPa', label='轴承压力'),
              Item('_OddChLinksCoeff', label='奇数链节系数'),
               Item('W208', label=' bf_链轮系数'),
                Item('W165', label='l2/1000'),
            ),
            HGroup(
              Item('_K8', label='链类型/摩擦系数'),
           Item('_BArrea', label='链承载面积'),
            ),
                HGroup(
                    Item('G9', label='系数1'),
                    Item('I9', label='系数2'),
                    Item('FB', label='FB'),

                ),
            HGroup(
          Item('_Massm', label='链轮质量'),
            ),),label = '选择链'),
            HGroup(VGroup(HGroup(
                Item('_C_req', label='需求轴向距离'),
                Item('需求距离判断',label=' '),
                 Item('_ChLinks', label='链节数'),
                Item('链节数判断',label=' '),

            ),

            HGroup(
                Item('_K1', label='齿数系数'),
                Item('_K2', label='传动比系数'),
                Item('_K3', label='冲击系数',style='readonly'),
                Item('_K7', label='寿命系数'),
            ),
    HGroup(
                Item('_Density', label='密度'),
        Item('_K4', label='轴距系数'),
        Item('_Temperature', label='温度'),
                HGroup(
                    Item('_K9', label='摩擦条件系数', style='readonly'),
                    Item('X155', label='最大转速条件', style='readonly'),
                ),

                HGroup(
                    Item('_Efficiency', label='链效率', style='readonly'),

                ),
            ),
            # ... 其他系数和参数的视图组 ...
            HGroup(
                 Item('S_Units', label='单位（公制为True）'),
                Item('_Life', label='工作时间'),
                Item('j计算系数', label='计算系数和链节数'),
            ),),label = '计算系数'),
        HGroup(
            VGroup(

        HGroup(
            Item('_Sigma', label='计算压力'),
             Item('_Pp', label='设计功率'),
        ),
        HGroup(
             Item('_Fu', label='张力有效圆周力'),
            Item('_Fc', label='惯性力'),
        ),
            HGroup(
                   Item('j计算', ),
    Item('j打开pdf', ),
                ),
            ), label = '计算')
        ,layout='tabbed',style_sheet='*{font-size:20px}'),
            # 可以添加更多的视图项或组
        title='链传动参数设置界面',  # 可选的标题
        #buttons=['OK', 'Cancel'],  # 添加确定和取消按钮
        kind="live",
        width=750,
        height=300,
        handler=ThreadInfoHandler())# 可以添加处理程序来响应按钮点击等事件（如果需要的话）

if __name__ == '__main__':
  demo = ChainParameters()
  demo.configure_traits()