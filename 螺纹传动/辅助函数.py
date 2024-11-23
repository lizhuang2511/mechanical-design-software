import pandas as pd
from excel公式python版本螺纹传动 import IF,INDEX
def 计算螺栓外形(螺纹类型,螺纹大小):
    文件路径 = '../螺纹传动/luowenleixing.xlsx'
    文件路径2 = '../螺纹传动/luowenchuandong.xlsx'
    数据 = pd.read_excel(open(文件路径2, 'rb'), sheet_name='T_ScrewA')
    print(螺纹类型)
    表格名称 = str(数据.loc[数据['List of threads'] == 螺纹类型, 4].values[0])
    螺纹角度1 = float(数据.loc[数据['List of threads'] == 螺纹类型, 7].values[0])
    螺纹角度2 = float(数据.loc[数据['List of threads'] == 螺纹类型, 8].values[0])
    T_ISO2940_A=pd.read_excel(open(文件路径, 'rb'), sheet_name='T_ISO2940_A')
    T_ScrewB_MetricTr=pd.read_excel(open(文件路径, 'rb'), sheet_name='T_ScrewB_MetricTr')
    print(表格名称)
    数据螺栓大小 = pd.read_excel(open(文件路径, 'rb'), sheet_name=表格名称)
    螺纹外径 =数据螺栓大小.loc[数据螺栓大小[1] == 螺纹大小, 3]#o
    螺纹外径=(螺纹外径.values)
    print('螺纹外径',螺纹外径)
    螺栓间距 = 数据螺栓大小.loc[数据螺栓大小[1] == 螺纹大小, 4]
    螺栓间距 = (螺栓间距.values)#j
    if len(螺纹外径)==0:
        螺纹外径=0
        螺栓间距=0
    if 螺纹类型=='公制螺纹-粗系列   (ISO 68 - 1)':
        Hh=(3**0.5)/2*螺栓间距#k
        aca=0
        h1b=0
        h1hs=0
        d0=螺纹外径-2*(7/8*Hh)#p
        d1=螺纹外径 - 2 * (5 / 8 *Hh )
        d2=螺纹外径-2*(3/8*Hh)
        d3=d0+2*(0.125*螺栓间距)
        d4=螺纹外径
    if 螺纹类型=='公制方螺纹精细   (IS 4694-1968)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        aca=IF(螺纹外径 < 300, 0.25, 0.5)
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '公制方螺纹正常   (IS 4694-1969)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        aca = IF(螺纹外径 < 115, 0.25, 0.5)
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '公制方螺纹粗   (IS 4694-1970)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        aca = IF(螺纹外径 < 55, 0.25, 0.5)
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '公制梯形螺纹30°   (ISO 2904: 1977)':
        螺栓间距 = 数据螺栓大小.loc[数据螺栓大小[1] == 螺纹大小, 4]
        螺栓间距 = float(螺栓间距.values)  # j
        print('螺栓间距',螺栓间距)
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        aca=T_ISO2940_A.loc[T_ISO2940_A['P']==螺栓间距,'ac']
        print('aca',aca)
        aca=aca.values
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '公制梯形螺纹30°   (DIN 103)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '支撑柱粗螺纹3°，30°   (DIN 513)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        aca=T_ScrewB_MetricTr.loc[T_ScrewB_MetricTr[1]==螺纹大小,:]
        aca = aca.values
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '统一英制螺纹-粗系列   (ASME B 1.1)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '英制方螺纹   ()':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '英制梯形螺纹29°   (ASME B 1.5)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    if 螺纹类型 == '支撑螺纹7°，45°   (ASME B 1.9)':
        Hh = (3 ** 0.5) / 2 * 螺栓间距  # k
        d0 = 螺纹外径 - 2 * (7 / 8 * Hh)  # p
        d1 = 螺纹外径 - 2 * (5 / 8 * Hh)
        d2 = 螺纹外径 - 2 * (3 / 8 * Hh)
        d3 = d0 + 2 * (0.125 * 螺栓间距)
        d4 = 螺纹外径
    data ={
            'thread_outer_diameter': float(螺纹外径),#螺纹外径（标称）
            'nut_inner_diameter': d1,#螺母螺纹的内径
            'pitch_diameter': d2,#节圆直径
            'thread_inner_diameter': d3,#螺纹内径
            'nut_thread_outer_diameter': d4,#螺母螺纹外径
            'bolt_spacing': float(螺栓间距),#螺栓间距
            'thread_angle_1': 螺纹角度1,#螺纹角度1
            'thread_angle_2': 螺纹角度2#螺纹角度2
        }
        # Add other type-size mappings here...
    值 =data
    return 值
def 读取螺纹大小(螺纹类型):
    文件路径 = '../螺纹传动/luowenleixing.xlsx'
    文件路径2 = '../螺纹传动/luowenchuandong.xlsx'
    数据 = pd.read_excel(open(文件路径2, 'rb'), sheet_name='T_ScrewA')
    print(螺纹类型)
    表格名称 = str(数据.loc[数据['List of threads'] == 螺纹类型, 4].values[0])
    print(表格名称)
    数据螺栓大小 = pd.read_excel(open(文件路径, 'rb'), sheet_name=表格名称)
    赛选数据 = 数据螺栓大小.loc[1:,1]
    值 = list(赛选数据)
    return 值
def 返回螺纹类型():
    文件路径 = '../螺纹传动/luowenchuandong.xlsx'
    数据 = pd.read_excel(open(文件路径, 'rb'), sheet_name='T_ScrewA')
    数据 = 数据.iloc[1:, :]
    赛选数据 = 数据.loc[:, 'List of threads']
    值 = list(赛选数据)
    return 值