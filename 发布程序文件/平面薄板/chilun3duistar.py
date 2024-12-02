# -*- coding = utf-8 -*-
# @time:2024/4/12 12:53
# Author:lizhuang
# @File:chilun3dui.py
# @Software:PyCharm
from traits.api import Float, Int, Button, HasTraits, Instance, on_trait_change
from traitsui.api import View, Item, HGroup, VGroup,Group
#import pygear  # 假设这个库存在或已被替换为相应的库
#from __future__ import print_function
import pygear
from OCC.Display.SimpleGui import init_display

class GearCreator(HasTraits):
    m_n = Float(10.0, label='模数')
    z = Int(11, label='齿数')
    beta = Float(0.0, label='螺旋角')
    x = Float(0.35, label='变位系数')
    alpha_n = Float(20.0, label='法向压力角')
    b = Float(180.0, label='齿宽')
    d_s = Float(20.0, label='轴孔直径')
    create_gear = Button('创建齿轮')
    #display, start_display, add_menu, add_function_to_menu = init_display()[0]
    #display = init_display()[0]

    # 齿轮对象的实例
    #gear_instance = Instance(pygear.displayOCCShape)

    # 当点击创建齿轮按钮时触发的函数
    def _create_gear_fired(self):
        gear_data = {
            'm_n': self.m_n,
            'z': self.z,
            'beta': self.beta,
            'x': self.x,
            'alpha_n': self.alpha_n,
            'b': self.b,
            'd_s': self.d_s,
        }



        import example_data
        #extgear_2 = {'m_n': 10.0, 'z': 11, 'beta': 0, 'x': 0.35, 'alpha_n': 20.0, 'b': 180, 'd_s': 20.0}
        geardata = gear_data  # select gear data here
        mygear = pygear.CylindricalGearWheel(geardata)  # create cylindrical gear wheel instance
        print(mygear)  # print gear data
        mygear_solid = mygear.makeOCCSolid()  # create OCC-3d-solid of gear wheel
        #start_display, add_menu, add_function_to_menu = init_display()
        # write 3d-solid of gear to STEP-file (in working directory)
        pygear.writeOCCShape(mygear_solid, 'extgear_1.stp', 'step')
        #a=self.gear_instance(mygear_solid)
        self.display, self.start_display, self.add_menu, self.add_function_to_menu = init_display()
        self.display.DisplayShape(mygear_solid, update=False)
        self.start_display()
    # UI布局定义
    traits_view = View(Group(
        VGroup(
            VGroup(
                Item('m_n'),
                Item('z'),
                Item('beta'),
                Item('x'),
                Item('alpha_n'),
                Item('b'),
                Item('d_s'),
                show_border=True,
                label='齿轮参数'
            ),
            HGroup(
                Item('create_gear', show_label=False),
                show_border=True,
                label='操作'
            ),
            # 可以根据需要添加更多UI元素，如显示齿轮的3D视图等。
        ),style_sheet='*{font-size:25px}'),
        resizable=True,
        title='齿轮生成器',
    )

# 运行UI界面
if __name__ == "__main__":
    gc = GearCreator()
    gc.configure_traits()
