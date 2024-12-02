import sys
sys.path.append("../transmission")
from gears import *
sys.path.append("../standards")
from iso import Pitting as isoPitting
from iso import Bending as isoBending
#from gearbox.standards.agma import Pitting as agmaPitting
#from gearbox.standards.agma import Bending as agmaBending
#from gearbox.export.export import *
#from gearbox.optimization.addendum import *

module = 2.5  # m
helix_angle = 0.0  # beta
pressure_angle = 20.0  # alpha

lubricant = Lubricant(
    name='Kiruna',
    v40=160
)

material = Material(
    name='AISI 2010',
    classification='NV(nitrocar)',
    sh_limit=1500.,#许用接触应力极限
    sf_limit=460.,#许用弯曲应力
    e=206000.,#弹性模量
    poisson=0.3,#泊松比
    density=7.83e-6,#密度
    brinell=286.6667#硬度
)

tool = Tool(
    ha_p=1,#齿顶高系数
    hf_p=1.25,#齿根高系数
    rho_fp=0.38,#齿根圆角半径
    x=0,
    rho_ao=0,
    delta_ao=0,
    nc=10.
)#配置文件#基本齿廓

pinion = Gear(
    profile=tool,
    material=material,
    z=22.,#齿数
    beta=helix_angle,#螺旋角
    alpha=pressure_angle,#压力角
    m=module,#模数
    x=0.525,#变位系数
    b=34.0,#齿轮宽度
    bs=34.0,#见30页bs
    sr=None,#见30页sr
    rz=3.67,#齿轮表面粗糙度
    precision_grade=6.0,#齿轮等级
    shaft_diameter=35.0,#轴直径
    schema=3.0,#支撑类型
    l=60.0,#支撑距离
    s=15.0,#支撑距离
    backlash=0.017,#齿轮侧间隙
    gear_crown=1,#齿轮顶
    helix_modification=1,#螺旋修改齿轮修型
    favorable_contact=True,#有利的接触
    gear_condition=1#齿轮条件
)

gear = Gear(
    profile=tool,
    material=material,
    z=40.,
    m=module,
    beta=helix_angle,
    alpha=pressure_angle,
    x=-0.275,
    b=34.0,
    bs=34.0,
    sr=None,
    rz=3.67,
    precision_grade=6.0,
    shaft_diameter=50.0,
    schema=3.0,
    l=60.0,#支撑距离
    s=35.0,#支撑距离
    backlash=-0.017,
    gear_crown=1,
    helix_modification=1,
    favorable_contact=True,
    gear_condition=1
)

pair = [pinion, gear]

transmission = Transmission(
    gears=pair,
    lubricant=lubricant,
    rpm_in=1450.0,#转速
    p=40.0,#名义功率
    l=10000.0,#使用时间小时
    gear_box_type=2,#齿轮数量
    ka=1.3,#使用系数
    sh_min=1,#接触应力安全系数
    sf_min=1#许用应力安全系数
)

print ('========================================')
print ('ISO Pitting')
print (isoPitting(transmission=transmission).calculate())
print ('========================================')

print ('========================================')
print ('ISO Bending')
print (isoBending(transmission=transmission).calculate)
print ('========================================')

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
