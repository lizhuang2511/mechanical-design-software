# -*- coding = utf-8 -*-
# @time:2024/4/3 13:37
# Author:lizhuang
# @File:ceshi1.py
# @Software:PyCharm
from OCC.Core.Geom2d import Handle_Geom2d_BSplineCurve
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge2d

# 假设geom2d_object是Geom2d_OffsetCurve类型的对象
basis_curve2d = geom2d_object.BasisCurve()

# 尝试转换并获取2D B样条曲线的实际对象
try:
    basis_bspline2d = basis_curve2d.GetObject()
except AttributeError:
    # 如果BasisCurve不是一个BSplineCurve，此处可能会抛出异常
    print("Basis curve is not a BSplineCurve.")
else:
    # 确保它是B-spline类型，并转换成Handle_Geom2d_BSplineCurve
    if isinstance(basis_bspline2d, Geom2d_BSplineCurve):
        basis_bspline_handle = Handle_Geom2d_BSplineCurve(basis_bspline2d)
    else:
        raise TypeError("Expected a Geom2d_BSplineCurve but got another type.")

    # 进行其他操作...
    # ...
    # 在新版本中，可能不再需要直接处理Handle，而是直接使用对象
    # ...

    # 示例：将2D B样条曲线转换为3D曲线（此处仅为示例逻辑）
    # （具体转换逻辑取决于您的_make3dGeomFrom2dGeom方法实现）
basis_bspline3d = self._make3dGeomFrom2dGeom(basis_bspline2d)
offset = geom2d_object.Offset()
reference_dir = gp_Dir(0.0, 0.0, 1.0)
geom3d_object = Geom_OffsetCurve(basis_bspline3d.Curve(), offset, reference_dir)
