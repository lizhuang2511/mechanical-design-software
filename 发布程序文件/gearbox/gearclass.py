import sys
sys.path.append("../gearbox/transmission")
from gears import *
sys.path.append("../gearbox/standards")
from iso import Pitting as isoPitting
from iso import Bending as isoBending
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password
from traitsui.api import Item, Group, View,CheckListEditor,Handler,VGrid,HGroup,VGroup,Font,TextEditor
import pandas as pd
import re
#from traitsui.menu import ModalButtons
import sys
from pyface.api import ArrayImage, Image, ImageResource
from traitsui.api import View, VGroup, Item, ImageEditor
#from gearbox.standards.agma import Pitting as agmaPitting
#from gearbox.standards.agma import Bending as agmaBending
#from gearbox.export.export import *
#from gearbox.optimization.addendum import *
from 测试表格生成 import create_pdf
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
from datetime import datetime
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
class gearclass():
    def __init__(self):
        self.module=2.5
        self.helix_angle=0
        self.pressure_angle=20
        self.name='Kiruna'
        self.v40=160
        self.namem1='AISI 2010'
        self.classificationm1='NV(nitrocar)'
        self.sh_limitm1=1500
        self.sf_limitm1=460
        self.em1=206000.
        self.poissonm1=0.3
        self.densitym1=7.83e-6
        self.brinellm1=286.6667
        self.namem2 = 'AISI 2010'
        self.classificationm2 = 'NV(nitrocar)'
        self.sh_limitm2 = 1500
        self.sf_limitm2 = 460
        self.em2 = 206000.
        self.poissonm2 = 0.3
        self.densitym2 = 7.83e-6
        self.brinellm2 = 286.6667
        self.z1=22.
        self.x1=0.525  # 变位系数
        self.b1=34.0  # 齿轮宽度
        self.bs1=34.0 # 见30页bs
        self.sr1 = None # 见30页sr
        self.rz1 = 3.67 # 齿轮表面粗糙度
        self.precision_grade1 = 6.0  # 齿轮等级
        self.shaft_diameter1 = 35.0  # 轴直径
        self.schema1 = 3.0 # 支撑类型
        self.l1 = 60.0  # 支撑距离
        self.s1 = 15.0  # 支撑距离
        self.backlash1 = 0.017 # 齿轮侧间隙
        self.gear_crown1 = 1 # 齿轮顶
        self.helix_modification1 = 1  # 螺旋修改齿轮修型
        self.favorable_contact1 = True # 有利的接触
        self.gear_condition1 = 1  # 齿轮条件
        self.z2 = 40
        self.x2 = -0.275 # 变位系数
        self.b2 = 34.0 # 齿轮宽度
        self.bs2 = 34.0 # 见30页bs
        self.sr2 = None # 见30页sr
        self.rz2 = 3.67 # 齿轮表面粗糙度
        self.precision_grade2 = 6.0  # 齿轮等级
        self.shaft_diameter2 = 50.0  # 轴直径
        self.schema2 = 3.0  # 支撑类型
        self.l2 = 60.0 # 支撑距离
        self.s2 = 35.0 # 支撑距离
        self.backlash2 = 0.017  # 齿轮侧间隙
        self.gear_crown2 = 1  # 齿轮顶
        self.helix_modification2 = 1  # 螺旋修改齿轮修型
        self.favorable_contact2 = True # 有利的接触
        self.gear_condition2 = 1  # 齿轮条件
        self.rpm_in = 1450.0  # 转速
        self.p = 40.0  # 名义功率
        self.l = 10000.0 # 使用时间小时
        self.gear_box_type = 2  # 齿轮数量
        self.ka = 1.3  # 使用系数
        self.sh_min = 1 # 接触应力安全系数
        self.sf_min = 1  # 许用应力安全系数
        self.ha_p=1
        self.hf_p = 1.25  # 齿根高系数
        self.rho_fp = 0.38 # 齿根圆角半径
        self.x = 0
        self.rho_ao = 0
        self.delta_ao = 0
        self.nc = 10
    def 应力计算(self):
        module = self.module  # m
        helix_angle = self.helix_angle  # beta
        pressure_angle = self.pressure_angle  # alpha

        lubricant = Lubricant(
            name=self.name,
            v40=self.v40
        )

        materialm1 = Material(
            name=self.namem1,
            classification=self.classificationm1,
            sh_limit=self.sh_limitm1,#许用接触应力极限
            sf_limit=self.sf_limitm1,#许用弯曲应力
            e=self.em1,#弹性模量
            poisson=self.poissonm1,#泊松比
            density=self.densitym1,#密度
            brinell=self.brinellm1#硬度
        )
        materialm2 = Material(
            name=self.namem2,
            classification=self.classificationm2,
            sh_limit=self.sh_limitm2,  # 许用接触应力极限
            sf_limit=self.sf_limitm2,  # 许用弯曲应力
            e=self.em2,  # 弹性模量
            poisson=self.poissonm2,  # 泊松比
            density=self.densitym2,  # 密度
            brinell=self.brinellm2  # 硬度
        )
        tool = Tool(
            ha_p=self.ha_p,#齿顶高系数
            hf_p=self.hf_p,#齿根高系数
            rho_fp=self.rho_fp,#齿根圆角半径
            x=self.x,
            rho_ao=self.rho_ao,
            delta_ao=self.delta_ao,
            nc=self.nc
            )#配置文件#基本齿廓

        pinion = Gear(
            profile=tool,
            material=materialm1,
            z=self.z1,#齿数
            beta=self.helix_angle,#螺旋角
            alpha=self.pressure_angle,#压力角
            m=self.module,#模数
            x=self.x1,#变位系数
            b=self.b1,#齿轮宽度
            bs=self.bs1,#见30页bs
            sr=self.sr1,#见30页sr
            rz=self.rz1,#齿轮表面粗糙度
            precision_grade=self.precision_grade1,#齿轮等级
            shaft_diameter=self.shaft_diameter1,#轴直径
            schema=self.schema1,#支撑类型
            l=self.l1,#支撑距离
            s=self.s1,#支撑距离
            backlash=self.backlash1,#齿轮侧间隙
            gear_crown=self.gear_crown1,#齿轮顶
            helix_modification=self.helix_modification1,#螺旋修改齿轮修型
            favorable_contact=self.favorable_contact1,#有利的接触
            gear_condition=self.gear_condition1#齿轮条件agma才使用
        )

        gear = Gear(
            profile=tool,
            material=materialm2,
            z=self.z2,
            m=module,
            beta=helix_angle,
            alpha=pressure_angle,
            x=self.x2,
            b=self.b2,
            bs=self.bs2,
            sr=self.sr2,
            rz=self.rz2,
            precision_grade=self.precision_grade2,
            shaft_diameter=self.shaft_diameter2,
            schema=self.schema2,
            l=self.l2,#支撑距离
            s=self.s2,#支撑距离
            backlash=self.backlash2,
            gear_crown=self.gear_crown2,
            helix_modification=self.helix_modification2,
            favorable_contact=self.favorable_contact2,
            gear_condition=self.gear_condition2#agma才使用
        )

        pair = [pinion, gear]

        transmission = Transmission(
            gears=pair,
            lubricant=lubricant,
            rpm_in=self.rpm_in,#转速
            p=self.p,#名义功率
            l=self.l,#使用时间小时
            gear_box_type=self.gear_box_type,#齿轮数量
            ka=self.ka,#使用系数
            sh_min=self.sh_min,#接触应力安全系数
            sf_min=self.sf_min#许用应力安全系数
        )
        接触应力=isoPitting(transmission=transmission).calculate()
        弯曲应力=isoBending(transmission=transmission).calculate
        transmission.计算齿厚(pinion, gear)
        transmission.计算齿厚小齿轮(pinion, gear)
        '''转换列表=[pinion,gear,tool,transmission,lubricant,materialm1,materialm2]

        obj=转换列表[5]
        print(转换列表[5])
        # 获取对象的所有属性名称及对应的属性值
        attributes = obj.__dict__.items()
        # 创建包含对象名和每个属性与其完整的对象名和原始属性名称的字典
        result_dict = {f"{obj.__class__.__name__}.{key}": (f"{obj.__class__.__name__}.{key}", '') for key, value in
                           attributes}
        print(result_dict)'''
        结果字典={'pinion.profile': (pinion.profile, ''),
        '小齿轮材料': (self.namem2, ''),
        '小齿轮齿数z': (pinion.z, ''),
        '小齿轮螺旋角beat': (pinion.beta, ''),
        '小齿轮压力角alph': (pinion.alpha, ''),
        '小齿轮模数m': (pinion.m, ''),
        '小齿轮变位系数x': (pinion.x, ''),
        '小齿轮齿宽b': (pinion.b, ''),
        '小齿轮实际齿宽bs': (pinion.bs, ''),
        'pinion.sr': (pinion.sr, ''),
        'pinion.rz': (pinion.rz, ''),
        '小齿轮精度等级grade': (pinion.precision_grade, ''),
        'pinion.shaft_diameter': (pinion.shaft_diameter, ''),
        'pinion.schema': (pinion.schema, ''),
        '小齿轮支撑长度l': (pinion.l, ''),
        '小齿轮支撑长度.s': (pinion.s, ''),
        'pinion.backlash': (pinion.backlash, ''),
        #'pinion.pinion_crown': (pinion.pinion_crown, ''),
        'pinion.helix_modification': (pinion.helix_modification, ''),
        'pinion.favorable_contact': (pinion.favorable_contact, ''),
        #'pinion.pinion_condition': (pinion.pinion_condition, ''),
        'pinion.xmin': (pinion.xmin, ''),
        '小齿轮横向压力角.alpha_t': (pinion.alpha_t, ''),
        '小齿轮分度圆直径d': (pinion.d, ''),
        '小齿轮齿顶圆直径da': (pinion.da, ''),
        '小齿轮齿根圆直径df': (pinion.df, ''),
        '小齿轮基圆直径db': (pinion.db, ''),
        'pinion.addendum': (pinion.addendum, ''),
        'pinion.dedendum': (pinion.dedendum, ''),
        'pinion.h': (pinion.h, ''),
        'pinion.rho_f': (pinion.rho_f, ''),
        'pinion.mt': (pinion.mt, ''),
        'pinion.p_b': (pinion.p_b, ''),
        'pinion.p_n': (pinion.p_n, ''),
        'pinion.beta_b': (pinion.beta_b, ''),
        'pinion.zn': (pinion.zn, ''),
        'pinion.f_pt': (pinion.f_pt, ''),
        'pinion.f_p': (pinion.f_p, ''),
        'pinion.f_alpha': (pinion.f_alpha, ''),
        'pinion.f_beta': (pinion.f_beta, ''),
        'pinion.f_f_alpha': (pinion.f_f_alpha, ''),
        'pinion.f_h_alpha': (pinion.f_h_alpha, ''),
        'pinion.f_h_beta': (pinion.f_h_beta, ''),
        'pinion.f_f_beta': (pinion.f_f_beta, ''),
        'pinion.f_h_beta5': (pinion.f_h_beta5, ''),
        'gear.profile': (gear.profile, ''),
        '大齿轮材料material': (self.namem1, ''),
        '大齿轮齿数z': (gear.z, ''),
        '大齿轮螺旋角beta': (gear.beta, ''),
        '大齿轮压力角alpha': (gear.alpha, ''),
        '大齿轮模数m': (gear.m, ''),
        '大齿轮变位系数x': (gear.x, ''),
        '大齿轮齿宽b': (gear.b, ''),
        '大齿轮有效齿宽bs': (gear.bs, ''),
        'gear.sr': (gear.sr, ''),
        'gear.rz': (gear.rz, ''),
        '大齿轮精度等级grade': (gear.precision_grade, ''),
        'gear.shaft_diameter': (gear.shaft_diameter, ''),
        'gear.schema': (gear.schema, ''),
        '大齿轮支撑长度l': (gear.l, ''),
        '大齿轮支撑长度s': (gear.s, ''),
        'gear.backlash': (gear.backlash, ''),
        'gear.gear_crown': (gear.gear_crown, ''),
        'gear.helix_modification': (gear.helix_modification, ''),
        'gear.favorable_contact': (gear.favorable_contact, ''),
        'gear.gear_condition': (gear.gear_condition, ''),
        'gear.xmin': (gear.xmin, ''),
        'gear.alpha_t': (gear.alpha_t, ''),
        '大齿轮分度圆直径d': (gear.d, ''),
        '大齿轮齿顶圆直径da': (gear.da, ''),
        '大齿轮齿根圆直径df': (gear.df, ''),
        '大齿轮基圆直径db': (gear.db, ''),
        '大齿轮s': (transmission.s, ''),
        '大齿轮sn': (transmission.sn22, ''),
        '大齿轮sa': (transmission.sa, ''),
        '大齿轮sf': (transmission.sf, ''),
        '小齿轮s': (transmission.s1, ''),
        '小齿轮sn': (transmission.sn11, ''),
        '小齿轮sa': (transmission.sa1, ''),
        '小齿轮sf': (transmission.sf1, ''),
        'gear.addendum': (gear.addendum, ''),
        'gear.dedendum': (gear.dedendum, ''),
        'gear.h': (gear.h, ''),
        'gear.rho_f': (gear.rho_f, ''),
        'gear.mt': (gear.mt, ''),
        'gear.p_b': (gear.p_b, ''),
        'gear.p_n': (gear.p_n, ''),
        'gear.beta_b': (gear.beta_b, ''),
        'gear.zn': (gear.zn, ''),
        'gear.f_pt': (gear.f_pt, ''),
        'gear.f_p': (gear.f_p, ''),
        'gear.f_alpha': (gear.f_alpha, ''),
        'gear.f_beta': (gear.f_beta, ''),
        'gear.f_f_alpha': (gear.f_f_alpha, ''),
        'gear.f_h_alpha': (gear.f_h_alpha, ''),
        'gear.f_h_beta': (gear.f_h_beta, ''),
        'gear.f_f_beta': (gear.f_f_beta, ''),
        'gear.f_h_beta5': (gear.f_h_beta5, ''),
        '齿顶高系数.ha_p': (tool.ha_p, ''),
        '齿根高系数.hf_p': (tool.hf_p, ''),
        '齿根半径系数.rho_fp': (tool.rho_fp, ''),
        'tool.c': (tool.c, ''),
        'tool.nc': (tool.nc, ''),
        'tool.x': (tool.x, ''),
        'tool.rho_ao': (tool.rho_ao, ''),
        'tool.delta_ao': (tool.delta_ao, ''),
        '输入转速rpm_in': (transmission.rpm_in, ''),
        '输出转速rpm_out': (transmission.rpm_out, ''),
        '使用系数ka': (transmission.ka, ''),
        'transmission.sh_min': (transmission.sh_min, ''),
        'transmission.sf_min': (transmission.sf_min, ''),
        'transmission.v40': (transmission.v40, ''),
        'transmission.gear_box_type': (transmission.gear_box_type, ''),
        'transmission.u': (transmission.u, ''),
        'transmission.p': (transmission.p, ''),
        'transmission.l': (transmission.l, ''),
        'transmission.m': (transmission.m, ''),
        'transmission.alpha': (transmission.alpha, ''),
        'transmission.alpha_t': (transmission.alpha_t, ''),
        'transmission.u_real': (transmission.u_real, ''),
        'transmission.u_error': (transmission.u_error, ''),
        'transmission.alpha_wt': (transmission.alpha_wt, ''),
        '中心距.a': (transmission.a, ''),
        'transmission.aw': (transmission.aw, ''),
        '端面重合度epsilon_alpha': (transmission.epsilon_alpha, ''),
        '纵向重合度.epsilon_beta': (transmission.epsilon_beta, ''),
        '总重合度.epsilon_gama': (transmission.epsilon_gama, ''),
        '分度圆圆周速度 .v': (transmission.v, ''),
        '切向力.ft': (transmission.ft, ''),
        'transmission.fmt': (transmission.fmt, ''),
        'transmission.xsum': (transmission.xsum, ''),
        'transmission.gear_one': (transmission.gear_one, ''),
        'transmission.gear_two': (transmission.gear_two, ''),
        'transmission.pair': (transmission.pair, ''),
        'lubricant.name': (lubricant.name, ''),
        'lubricant.v40': (lubricant.v40, ''),
        '小齿轮接触应力极限.sh_limit': (materialm1.sh_limit, ''),
        '小齿轮弯曲应力极限.sf_limit': (materialm1.sf_limit, ''),
        'materialm1.classification': (materialm1.classification, ''),
        '小齿轮材料名称name': (materialm1.name, ''),
        '小齿轮材料弹性模量.e': (materialm1.e, ''),
        '小齿轮材料泊松比.poisson': (materialm1.poisson, ''),
        '小齿轮材料密度.density': (materialm1.density, ''),
        'materialm1.brinell': (materialm1.brinell, ''),
        '大齿轮接触应力极限.sh_limit': (materialm2.sh_limit, ''),
        '大齿轮弯曲应力极限.sf_limit': (materialm2.sf_limit, ''),
        'materialm2.classification': (materialm2.classification, ''),
        '大齿轮材料名称.name': (materialm2.name, ''),
        '大齿轮材料弹性模量.e': (materialm2.e, ''),
        '大齿轮材料泊松比.poisson': (materialm2.poisson, ''),
        '大齿轮材料密度.density': (materialm2.density, ''),
        'materialm2.brinell': (materialm2.brinell, ''),
        'sigmafoone': (弯曲应力['sigmafoone'], ''),
        'sigmafotwo': (弯曲应力['sigmafotwo'], ''),
        'sigmafone': (弯曲应力['sigmafone'], ''),
        'sigmaftwo': (弯曲应力['sigmaftwo'], ''),
        'sigmafpone': (弯曲应力['sigmafpone'], ''),
        'sigmafptwo': (弯曲应力['sigmafptwo'], ''),
        'yst': (弯曲应力['yst'], ''),
        'yxone': (弯曲应力['yxone'], ''),
        'yxtwo': (弯曲应力['yxtwo'], ''),
        'yfone': (弯曲应力['yfone'], ''),
        'yftwo': (弯曲应力['yftwo'], ''),
        'ysone': (弯曲应力['ysone'], ''),
        'ystwo': (弯曲应力['ystwo'], ''),
        'ybeta': (弯曲应力['ybeta'], ''),
        'ybone': (弯曲应力['ybone'], ''),
        'ybtwo': (弯曲应力['ybtwo'], ''),
        'ydeltaone': (弯曲应力['ydeltaone'], ''),
        'ydeltatwo': (弯曲应力['ydeltatwo'], ''),
        'ydt': (弯曲应力['ydt'], ''),
        'yntone': (弯曲应力['yntone'], ''),
        'ynttwo': (弯曲应力['ynttwo'], ''),
        'yrelone': (弯曲应力['yrelone'], ''),
        'yreltwo': (弯曲应力['yreltwo'], ''),
        'kv': (接触应力['kv'], ''),
        'kfa': (弯曲应力['kfa'], ''),
        'kfb': (弯曲应力['kfb'], ''),
        'sigmaH': (接触应力['sigmaH'], ''),
        'sigmaHTwo': (接触应力['sigmaHTwo'], ''),
        'sigmaHPOne': (接触应力['sigmaHPOne'], ''),
        'sigmaHPTwo': (接触应力['sigmaHPTwo'], ''),
        'zh': (接触应力['zh'], ''),
        'zb': (接触应力['zb'], ''),
        'zd': (接触应力['zd'], ''),
        'ze': (接触应力['ze'], ''),
        'z_epsilon': (接触应力['z_epsilon'], ''),
        'z_beta': (接触应力['z_beta'], ''),
        'znt_one': (接触应力['znt_one'], ''),
        'znt_two': (接触应力['znt_two'], ''),
        'zl': (接触应力['zl'], ''),
        'zv': (接触应力['zv'], ''),
        'zr': (接触应力['zr'], ''),
        'zw_one': (接触应力['zw_one'], ''),
        'zw_two': (接触应力['zw_two'], ''),
        'zx': (接触应力['zx'], ''),
        'khb': (接触应力['khb'], ''),
        'kha': (接触应力['kha'], '')}
        #create_pdf(结果字典, title='涡轮蜗杆计算报告', filename='output_with_page_number.pdf')

        return 接触应力,弯曲应力,transmission,pinion,gear,结果字典
if __name__=="__main__":
    测试=gearclass()
    弯曲应力=测试.应力计算()[1]
    接触应力=测试.应力计算()[0]
    print(弯曲应力)
    print(接触应力)
'''print ('========================================')
print ('ISO Pitting')
print (isoPitting(transmission=transmission).calculate())
print ('========================================')

print ('========================================')
print ('ISO Bending')
print (isoBending(transmission=transmission).calculate)
print ('========================================')'''

'''print ('========================================')
print ('AGMA Pitting')
print (agmaPitting(transmission=transmission).calculate())
print ('========================================')

print ('========================================')
print ('AGMA Bending')
print (agmaBending(transmission=transmission).calculate())
print ('========================================')

print ('========================================')
xoptim_bending = Optmization(transmission).bending()
xoptim_pitting_iso = Optmization(transmission).pitting(standard='ISO')
# xoptim_pitting_agma = Optmization(transmission).pitting(standard='AGMA')
print ('Profile shift optimization')
print ('x1=%s, x2=%s for minimum bending stress' % (xoptim_bending[0], xoptim_bending[1]))
print ('x1=%s, x2=%s for minimum contact stress using ISO standard' % (xoptim_pitting_iso[0], xoptim_pitting_iso[1]))
print ('========================================')




output_folder = os.path.join(os.path.dirname(__file__), 'output')
try:
    os.mkdir(output_folder)
except:
    pass

# ===============================================
# EXPORT TO MATLAB/COMSOL SCRIPT 
# ===============================================
# 2D model matlab-comsol export
# for 2D export type='2D' is optional because '2D' is the default output
comsol_transmission_model_name2d = 'transmission2d'
comsol_pinion_model_name2d = 'pinion2d'
comsol_wheel_model_name2d = 'wheel2d'
ExportGear(pinion).matlab_comsol(model_name=comsol_pinion_model_name2d, output_folder=output_folder, type='2D')
ExportGear(gear).matlab_comsol(model_name=comsol_wheel_model_name2d, output_folder=output_folder, type='2D')
ExportPair(pair).matlab_comsol(model_name=comsol_transmission_model_name2d, output_folder=output_folder, type='2D')

# 3D model matlab-comsol export
comsol_transmission_model_name3d = 'transmission3d'
comsol_pinion_model_name3d = 'pinion3d'
comsol_wheel_model_name3d = 'wheel3d'
ExportGear(pinion).matlab_comsol(model_name=comsol_pinion_model_name3d, output_folder=output_folder, type='3D')
ExportGear(gear).matlab_comsol(model_name=comsol_wheel_model_name3d, output_folder=output_folder, type='3D')
ExportPair(pair).matlab_comsol(model_name=comsol_transmission_model_name3d, output_folder=output_folder, type='3D')

# ===============================================
# EXPORT TO ABAQUS PYTHON 
# ===============================================
# 2D model abaqus export
# for 2D export type='2D' is optional because '2D' is the default output
abaqus_transmission_model_name2d = 'transmission2d'
abaqus_pinion_model_name2d = 'pinion2d'
abaqus_wheel_model_name2d = 'wheel2d'
ExportGear(pinion).abaqus(model_name=abaqus_pinion_model_name2d, output_folder=output_folder, type='2D')
ExportGear(gear).abaqus(model_name=abaqus_wheel_model_name2d, output_folder=output_folder, type='2D')
ExportPair(pair).abaqus(model_name=abaqus_transmission_model_name2d, output_folder=output_folder, type='2D')

# 3D model abaqus export
abaqus_transmission_model_name3d = 'transmission3d'
abaqus_pinion_model_name3d = 'pinion3d'
abaqus_wheel_model_name3d = 'wheel3d'
ExportGear(pinion).abaqus(model_name=abaqus_pinion_model_name3d, output_folder=output_folder, type='3D')
ExportGear(gear).abaqus(model_name=abaqus_wheel_model_name3d, output_folder=output_folder, type='3D')
ExportPair(pair).abaqus(model_name=abaqus_transmission_model_name3d, output_folder=output_folder, type='3D')

# ===============================================
# EXPORT TO ANSYS/WOKRBENCH Script
# ===============================================
# 2D model abaqus export
# for 2D export type='2D' is optional because '2D' is the default output
ansys_transmission_model_name2d = 'transmission2d'
ansys_pinion_model_name2d = 'pinion2d'
ansys_wheel_model_name2d = 'wheel2d'
ExportGear(pinion).ansys(model_name=ansys_pinion_model_name2d, output_folder=output_folder, type='2D')
ExportGear(gear).ansys(model_name=ansys_wheel_model_name2d, output_folder=output_folder, type='2D')
ExportPair(pair).ansys(model_name=ansys_transmission_model_name2d, output_folder=output_folder, type='2D')
#
# 3D model ansys export
ansys_transmission_model_name3d = 'transmission3d'
ansys_pinion_model_name3d = 'pinion3d'
ansys_wheel_model_name3d = 'wheel3d'
ExportGear(pinion).ansys(model_name=ansys_pinion_model_name3d, output_folder=output_folder, type='3D')
ExportGear(gear).ansys(model_name=ansys_wheel_model_name3d, output_folder=output_folder, type='3D')
ExportPair(pair).ansys(model_name=ansys_transmission_model_name3d, output_folder=output_folder, type='3D')'''
