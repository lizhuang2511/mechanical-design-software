# -*- coding = utf-8 -*-
# @time:2024/3/29 10:41
# Author:lizhuang
# @File:meshzhejie.py
# @Software:PyCharm
import gmsh

# 初始化 GMSH
gmsh.initialize()

# 设置模型参数
gmsh.model.add("my_model")

# 定义长方体的几何参数
x_min, x_max = 0.0, 10.0
y_min, y_max = 0.0, 5.0
z_min, z_max = 0.0, 2.0

# 使用Gmsh的内置函数来创建长方体
gmsh.model.geo.add(x_min, x_max, y_min, y_max, z_min, z_max, meshSize=1.0)

# 设置网格划分算法为六面体（对于简单形状，Gmsh 可以生成六面体网格）
gmsh.option.setNumber("Mesh.Algorithm3D", 9)  # 使用 HXT (Hybrid eXtra-fast Tetrahedralization) 算法
gmsh.option.setNumber("Mesh.RecombineAll", 1)  # 尝试将所有四面体单元重新组合为六面体单元

# 设置网格划分的其他参数
gmsh.option.setNumber("Mesh.ElementOrder", 1)  # 线性元素

# 生成网格
gmsh.model.mesh.generate(3)  # 生成 3D 网格

# 导出网格到文件
gmsh.write("my_model.vtk")  # 导出为 VTK 格式的网格文件

# 如果需要查看网格信息，可以使用以下命令
# gmsh.fltk.run()  # 这将打开一个窗口显示网格，需要安装FLTK库

# 清理并退出 GMSH
gmsh.finalize()