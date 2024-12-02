# -*- coding = utf-8 -*-
# @time:2024/3/29 9:23
# Author:lizhuang
# @File:测试.py
# @Software:PyCharm
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Extend.DataExchange import write_step_file
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Ax2,gp_Dir

from OCC.Core.STEPControl import STEPControl_Writer
from sfepy.discrete.fem import Mesh, FEDomain, Field
# 定义圆柱的底部中心点、半径和高
center_point = gp_Pnt(0.0, 0.0, 0.0)
radius = 10.0
height = 50.0

# 定义圆柱的方向（使用向量），并将其转换为方向（gp_Dir）
axis_vec = gp_Vec(-1.0, 0.0, 0.0)  # Z轴方向的向量
z_dir = gp_Dir(axis_vec)  # 转换为方向

# 默认X轴方向（可选，如果不提供，则OCCT会自动计算一个垂直于Z轴的X轴）
x_dir = gp_Dir(0.0, 0.0, 1.0)  # 例如，这里我们选择X轴方向为(1,0,0)

# 使用gp_Ax2定义圆柱的位置和方向（原点，Z轴和X轴）
location = gp_Ax2(center_point, z_dir, x_dir)  # 注意这里添加了X轴方向

# 使用BRepPrimAPI_MakeCylinder类创建圆柱体
cylinder = BRepPrimAPI_MakeCylinder(location, radius, height).Shape()

# 保存为STEP文件，以便在其他CAD软件中查看
step_writer = STEPControl_Writer()
write_step_file(cylinder,'cylinder.step')
# 创建一个长方体，其左下角位于原点(0, 0, 0)，并且各边长度为100, 200, 300
box = BRepPrimAPI_MakeBox(100, 100, 100).Shape()

# 将长方体保存为STEP格式的文件
write_step_file(box, "output_box.step")

print("长方体已保存为output_box.step")
import gmsh

# 初始化 GMSH
gmsh.initialize()

# 设置模型参数
gmsh.model.add("my_model")

# 加载 STL 文件作为几何体的一部分
#
# 假设 STL 文件名为 "my_model.stl"
gmsh.merge("cylinder.step")  # 这会将 STL 文件合并到当前模型中

# 设置网格参数
gmsh.option.setNumber("Mesh.MeshSizeMin", 1)
gmsh.option.setNumber("Mesh.MeshSizeMax", 5)
#gmsh.option.setNumber("Mesh.ElementOrder", 1)  # 线性元素
#gmsh.option.setNumber("Mesh.Algorithm3D", 9)  # 使用 3D 算法，例如 Frontal-Delaunay
#gmsh.option.setNumber("Mesh.RecombineAll", 1)

#gmsh.option.setNumber("Mesh.CharacteristicLengthFromCurvature", 0)  # 不从曲率计算特征长度
#gmsh.option.setNumber("Mesh.CharacteristicLengthExtendFromBoundary", 0)  # 不从边界扩展特征长度
#gmsh.option.setNumber("Mesh.CharacteristicLengthMax", 1.0)  # 设置最大特征长度

# 生成网格
gmsh.model.mesh.generate(3)  # 生成 3D 网格

# 导出网格到文件
gmsh.write("my_model.vtk")  # 导出为 GMSH 格式的网格文件

# 清理并退出 GMSH
gmsh.finalize()
import pyvista as pv

# 读取VTK文件
filename = "my_model.vtk"
mesh = pv.read(filename)

# 创建一个视窗并添加网格数据
plotter = pv.Plotter()

# 添加网格到场景中
plotter.add_mesh(mesh, color='w', show_edges=True)  # 颜色设置为白色，同时显示边框
plotter.show_axes()
# 设置相机位置和视角
#plotter.set_camera_position((0, 0, 10), (0, 0, 0))

# 显示窗口
plotter.show()
import numpy as nm
from sfepy.discrete.fem import Mesh, FEDomain, Field
mesh = Mesh.from_file('my_model.vtk')
#domain = FEDomain('domain', mesh)''
import gmsh
gmsh.initialize() # 初始化
gmsh.model.add("model1") # 创建模型
lc = 1e-1 # 设置网格尺寸值 # 创建点
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 1, 0, lc, 4) #创建线
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(3, 2, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4) # 创建边
gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1) # 创建面
gmsh.model.geo.addPlaneSurface([1])
gmsh.model.geo.synchronize() # 同步到模型
# 设置网格单元类型为四边形单元
gmsh.option.setNumber("Mesh.MeshSizeMax", lc)
gmsh.option.setNumber("Mesh.ElementOrder", 1)  # 对于线性单元
gmsh.model.mesh.generate(2) # 生成网格
gmsh.write("model1.msh") # 生成.msh文件
gmsh.fltk.run() # 图形界面显示
gmsh.finalize() # 关闭gmsh
from sfepy.discrete.fem import Mesh, FEDomain, Field
from sfepy.base.base import IndexedStruct
from sfepy.discrete import (FieldVariable, Material, Integral, Function,
                            Equation, Equations, Problem)
from sfepy.discrete.fem import Mesh, FEDomain, Field
from sfepy.terms import Term
from sfepy.discrete.conditions import Conditions, EssentialBC
from sfepy.solvers.ls import ScipyDirect
from sfepy.solvers.nls import Newton
from sfepy.mechanics.matcoefs import stiffness_from_lame

from argparse import ArgumentParser
import numpy as nm

import sys
sys.path.append('.')
def shift_u_fun(ts, coors, bc=None, problem=None, shift=0.0):
    """
    Define a displacement depending on the y coordinate.
    """
    val = shift * coors[:,1]**2

    return val
mesh = Mesh.from_file('model1.msh')
#subdomains = {name: ('all', tag) for name, tag in mesh.dim_tags['surfaces'].items()}  # 示例假设所有的物理组都是子域
domain = FEDomain('domain', mesh)
min_x, max_x = domain.get_mesh_bounding_box()[:,0]
eps = 1e-8 * (max_x - min_x)
omega = domain.create_region('Omega', 'all')
gamma1 = domain.create_region('Gamma1',
                              'vertices in x < %.10f' % (min_x + eps),
                              'facet')
gamma2 = domain.create_region('Gamma2',
                              'vertices in x > %.10f' % (max_x - eps),
                              'facet')

field = Field.from_args('fu', nm.float64, 'vector', omega,
                        approx_order=2)

u = FieldVariable('u', 'unknown', field)
v = FieldVariable('v', 'test', field, primary_var_name='u')

m = Material('m', D=stiffness_from_lame(dim=2, lam=1.0, mu=1.0))
f = Material('f', val=[[0.02], [0.01]])

integral = Integral('i', order=3)

t1 = Term.new('dw_lin_elastic(m.D, v, u)',
              integral, omega, m=m, v=v, u=u)
t2 = Term.new('dw_volume_lvf(f.val, v)', integral, omega, f=f, v=v)
eq = Equation('balance', t1 + t2)
eqs = Equations([eq])

fix_u = EssentialBC('fix_u', gamma1, {'u.all' : 0.0})

bc_fun = Function('shift_u_fun', shift_u_fun,
                  extra_args={'shift' : 0.01})
shift_u = EssentialBC('shift_u', gamma2, {'u.0' : bc_fun})

ls = ScipyDirect({})

nls_status = IndexedStruct()
nls = Newton({}, lin_solver=ls, status=nls_status)

pb = Problem('elasticity', equations=eqs)
pb.save_regions_as_groups('regions')

pb.set_bcs(ebcs=Conditions([fix_u, shift_u]))

pb.set_solver(nls)

status = IndexedStruct()
variables = pb.solve(status=status)

print('Nonlinear solver status:\n', nls_status)
print('Stationary solver status:\n', status)

pb.save_state('linear_elasticity.vtk', variables)
import pyvista as pv

# 读取VTK文件
filename = "linear_elasticity.vtk"
mesh = pv.read(filename)

# 创建一个视窗并添加网格数据
plotter = pv.Plotter()

# 添加网格到场景中
plotter.add_mesh(mesh, color='w', show_edges=True)  # 颜色设置为白色，同时显示边框

# 设置相机位置和视角
#plotter.set_camera_position((0, 0, 10), (0, 0, 0))

# 显示窗口
plotter.show()
import sys
sys.path.append('.')
import subprocess

# 定义要运行的命令
command = "start sfepy-view.exe linear_elasticity.vtk"

# 使用subprocess运行命令
subprocess.run(command, shell=True, check=True)
'''
A linear elastic beam loaded with a continuous force. The FE meshes consisting
of hexehedral, tetrahedral, and wedge elements are used in the simulation and
the results are compared.

The displacement at the beam end is compared to the reference
solution calculated on the homogeneous hexahedral mesh.

Running the simulation::

    sfepy-run sfepy/examples/linear_elasticity/wedge_mesh.py

Viewing the results::

    sfepy-view beam_h7.vtk beam_t42.vtk beam_w14.vtk -f u:s0:wu:e:p0 u:s1:wu:e:p0 u:s2:wu:e:p0 --camera-position="1.2,-0.6,0.1,0.4,0.1,-0.1,-0.2,0.1,1"'''

import sys
sys.path.append('.')
import subprocess

# 定义要运行的命令
command = "start sfepy-run.exe cswenjian.py"

# 使用subprocess运行命令
subprocess.run(command, shell=True, check=True)
import sys
sys.path.append('.')
import subprocess

# 定义要运行的命令
command = "start sfepy-view.exe cylinder.vtk"

# 使用subprocess运行命令
subprocess.run(command, shell=True, check=True)