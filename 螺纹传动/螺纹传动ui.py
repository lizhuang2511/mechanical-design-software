from traits.api import List, Str, observe
from traitsui.api import View, Item, VGrid
from traits.api import HasTraits, Float, Int, Enum, observe,Button
from traitsui.api import View, Item, VGrid, Handler
from traitsui.api import View, VGroup, Item, ImageEditor,EnumEditor,HGroup,Group,TextEditor
from 辅助函数 import 读取螺纹大小,返回螺纹类型,计算螺栓外形
from 螺纹传动计算 import 传动螺栓计算
import pandas as pd
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
from datetime import datetime
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('SimSun', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
from pdf阅读3 import PdfViewer
luomaocaizhi=list(['钢（结构） - (Rm = 380;  Rp(0.2) = 220 [MPa])',
'钢（结构） - (Rm = 420;  Rp(0.2) = 245 [MPa])',
'钢（结构） - (Rm = 510;  Rp(0.2) = 280 [MPa])',
'硬化钢 - (Rm = 580;  Rp(0.2) = 320 [MPa])',
'硬化钢 - (Rm = 640;  Rp(0.2) = 350 [MPa])',
'铸铁 - (Rm = 200;  Rp(0.2) = 100 [MPa])',
'铸铁 - (Rm = 275;  Rp(0.2) = 140 [MPa])',
'青铜 - (Rm = 200;  Rp(0.2) = 110 [MPa])',
'青铜 - (Rm = 250;  Rp(0.2) = 138 [MPa])',])
def INDEX(表名,行,列):
    文件路径='../螺纹传动/luowenchuandong.xlsx'
    数据=pd.read_excel(open(文件路径,'rb'),sheet_name=表名)
    #数据 = read_table_to_dataframe('../涡轮蜗杆计算/wilumwogan.db', 表名)
    #列=str(列)
    print(列)
    #行=str(str(行)+'.0')
    #行 = str(str(行))
    print(行)
    赛选数据=数据.loc[数据.行号 == 行, 列]
    print(赛选数据)
    #赛选数据.reset_index()
    #print(type(赛选数据))
    #列=str(列)
    数 = 赛选数据.values[0]
    if type(数)==str:
        值 = 赛选数据.values[0]
    else:
        值=float(赛选数据.values[0])
    #值 = 赛选数据.values[0]
    return 值
class ThreadInfoHandler(Handler):
    cities = List(Str)

    def object_thread_type_changed(self, info):
        self.cities = 读取螺纹大小(info.object.thread_type)
        print('a')
        # As default value, use the first city in the list:
        info.object.thread_size = self.cities[0]

class ThreadInfo(HasTraits):
    thread_type =Enum(返回螺纹类型())
    thread_size = Str()

    thread_outer_diameter = Float
    nut_inner_diameter = Float
    pitch_diameter = Float
    thread_inner_diameter = Float
    nut_thread_outer_diameter = Float
    bolt_spacing = Float
    thread_number = Int(1)
    thread_angle_1 = Float
    thread_angle_2 = Float
    螺丝材质=Enum(luomaocaizhi)
    螺帽材质=Enum(luomaocaizhi)
    负载力=Float(10000)
    #进给速度=Float
    螺纹摩擦系数=Float(0.08)
    _n_req=Float(100)
    j计算值 = Button('计算值')
    螺栓长度=Float(1000)
    螺母高度=Float(10)
    最大活动螺纹数=Float(8)
    等效应力=Float(0)
    下降力=Float(0)
    起重力=Float(0)
    效率=Float(0)
    驱动功率=Float(0)
    _ro_input = Float(0)
    _E_input =Float(0)
    _Rp02_input =Float(0)
    _pD_input = Float(0)
    _SRcs = Float(0)
    _SRc = Float(0)  # 自定义材料参数输入
    _ecc=Float(0.1)
    _Lef_coef=Float(2)
    螺纹压力=Float(0)
    def _螺丝材质_changed(self):
        a=luomaocaizhi.index(self.螺丝材质) + 1
        b = luomaocaizhi.index(self.螺帽材质) + 2
        self._ro_input = INDEX('T_MaterialA',a,4)
        self._E_input =INDEX('T_MaterialA',a,5)
        self._Rp02_input =INDEX('T_MaterialA',a,7)
        self._pD_input =INDEX('T_Pressure3',a,b)
        self._SRcs = INDEX('T_MaterialA',a,12)
        self._SRc = INDEX('T_MaterialA',a,13)#
        self.螺纹摩擦系数=INDEX('T_Friction2',a,b)
    def _螺帽材质_changed(self):
        self._螺丝材质_changed()

    @observe('thread_type')
    def _update_values_from_thread_type(self, change):
        print('选择大小后继续')
        '''data = self._read_thread_data(self.thread_type, self.thread_size)
        if data:
            self._update_values(data)'''

    @observe('thread_size')
    def _update_values_from_thread_size(self, change):
        data = self._read_thread_data(self.thread_type, self.thread_size)
        print(luomaocaizhi.index(self.螺帽材质)+1)
        if data:
            self._update_values(data)

    def _update_values(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def _read_thread_data(self, thread_type, thread_size):
        return 计算螺栓外形(thread_type, thread_size)

    @observe("j计算值")
    def 计算值(self, event):
        值=传动螺栓计算(_Q_input=self.负载力,
               _n_req=self._n_req,
               _f=self.螺纹摩擦系数,
               _d_input=self.thread_outer_diameter,
               _d1_input=self.nut_inner_diameter,
               _d2_input=self.pitch_diameter,
               _d3_input=self.thread_inner_diameter,
               _d4_input=self.nut_thread_outer_diameter,
               _P_input=self.bolt_spacing,
               _ns=self.thread_number,
               _alfa1_input=self.thread_angle_1,
               _alfa2_input=self.thread_angle_2, _MatID_Screw=int(luomaocaizhi.index(self.螺丝材质)+1),
               _MatID_Nut=int(luomaocaizhi.index(self.螺帽材质)+1),
               _JournalBT=0, #是否考虑摩擦扭矩
               _KFactor=6,#螺栓安装类型
               _EccRatioID=3,#偏心率id
               _fj=0.1,#摩擦系数
               _dj_input=32,#销钉直径
               _dx_input=250,#螺母螺钉位移
               _rev_input=83.3333333333333,#旋转圈速输入
               _Ls_input=self.螺栓长度,#螺栓长度
               _ro_input=self._ro_input,
               _E_input=self._E_input,
               _Rp02_input=self._Rp02_input,
               _pD_input=self._pD_input,
               _SRcs=self._SRcs,
               _SRc=self._SRc,#自定义材料参数输入
               _Lef_coef=self._Lef_coef,#有效长度系数默认会给
               _ecc=self._ecc,#偏心率输入
               _h_nut_input=self.螺母高度,#螺母高度
               _nzmax=self.最大活动螺纹数,#最大活动螺纹数
               _nts=333,#画图输入
               _ntn=8,
               _DN=52,#画图输入
               _SFA=2,#安全系数默认值
               _SFC_prop=1.5,
               _SFB_1=1.75,
               _nzmax_prop=8,
               _SFC=1.25,
               S_ExtraCopy_FlagIN=1,#无用
               )
        self.等效应力 = 值[0]
        self.下降力 = 值[1]
        self.起重力 = 值[2]
        self.效率 = 值[3]
        self.驱动功率 = 值[4]
        self.螺纹压力=值[6]
        结果字典=值[5]
        from 测试表格生成 import create_pdf
        create_pdf(结果字典, title='螺纹传动计算报告', filename=r'..\数据文件\螺纹传动.pdf')
        print(1)
        return

    j打开pdf = Button('打开pdf')

    @observe("j打开pdf")
    def 打开pdf(self, event):
        self.计算值(event)
        default_file_path = "..\数据文件\螺纹传动.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    traits_view = View(Group( HGroup(VGroup(
        Item('thread_type', label='螺纹类型'),
        Item('thread_size', label='螺纹尺寸',editor=EnumEditor(name='handler.cities')),
        VGrid(
            Item('thread_outer_diameter', label='螺纹外径（标称）',editor=TextEditor(format_str='%.2f')),
            Item('nut_inner_diameter', label='螺母螺纹的内径',editor=TextEditor(format_str='%.2f')),
            Item('pitch_diameter', label='节圆直径',editor=TextEditor(format_str='%.2f')),
            Item('thread_inner_diameter', label='螺纹内径',editor=TextEditor(format_str='%.2f')),
            Item('nut_thread_outer_diameter', label='螺母螺纹外径',editor=TextEditor(format_str='%.2f')),
            Item('bolt_spacing', label='螺栓间距',editor=TextEditor(format_str='%.2f')),
            Item('thread_number', label='螺纹头数'),
            Item('thread_angle_1', label='螺纹角度1',editor=TextEditor(format_str='%.2f')),
            Item('thread_angle_2', label='螺纹角度2',editor=TextEditor(format_str='%.2f')),
            columns=2,
            show_border=True,
        )),label='初始条件'),
        HGroup(VGroup(
            Item('螺丝材质', label='螺丝材质'),
            Item('螺帽材质', label='螺帽材质'),
            VGrid(Item('_ro_input', label='密度'),
                  Item('_E_input', label='拉伸弹性模量'),
                  Item('_Rp02_input', label='屈服强度'),
                  Item('_pD_input', label='允许平均螺纹压力'),
                  Item('_SRcs', label='极限纤度比（短/中）'),
                  Item('_SRc', label='极限纤度比（中/长）'),
        )),label='材料和受力'),
        HGroup(VGroup(
            VGrid(Item('负载力', label='负载力'),
            Item('螺纹摩擦系数', label='螺纹摩擦系数'),
            Item('_n_req', label='螺纹转速'),
            Item('螺栓长度', label='螺栓长度'),
            Item('螺母高度', label='螺母高度'),
            Item('最大活动螺纹数', label='最大活动螺纹数'),
            Item('_ecc', label='偏心率'),
            Item('_Lef_coef', label='有效长度系数')),

            Item('j计算值', label='计算值1'),
            VGrid(Item('等效应力', label='等效应力'),
            Item('下降力', label='下降力'),
            Item('起重力', label='起重力'),
            Item('效率', label='效率'),
            Item('驱动功率', label='驱动功率'),
                  Item('螺纹压力', label='螺纹压力')    ),
            Item('j打开pdf', label='打开pdf'),

        ), label='计算结果')
        ,layout='tabbed',style_sheet='*{font-size:25px}'),
        title='螺纹信息',
        resizable=True,
        handler=ThreadInfoHandler()
    )

if __name__ == "__main__":
    # 创建对象并显示界面
    thread_info = ThreadInfo()
    thread_info.configure_traits()
