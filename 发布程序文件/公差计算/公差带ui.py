# -*- coding = utf-8 -*-
# @time:2024/4/15 15:54
# Author:lizhuang
# @File:公差带ui.py
# @Software:PyCharm
from traits.api import Float, HasTraits, Instance, on_trait_change,Button
from traitsui.api import Item, View, HGroup, VGroup
#from traitsui.message import message


# 定义模型类，包含所需的所有traits
class GapCalculator(HasTraits):
    basic_size = Float(160,label='基本尺寸')
    hole_upper_deviation = Float(0.12,label='孔上偏差')
    hole_lower_deviation = Float(0.08,label='孔下偏差')
    shaft_upper_deviation = Float(-0.02,label='轴上偏差')
    shaft_lower_deviation = Float(-0.04,label='轴下偏差')

    calculate = Button(label='计算间隙')
    max_gap= Float(label='最大间隙')
    min_gap= Float(label='最小间隙')
    # 定义视图
    traits_view = View(
        VGroup(
            VGroup(
                Item('basic_size'),
                Item('hole_upper_deviation'),
                Item('hole_lower_deviation'),
                Item('shaft_upper_deviation'),
                Item('shaft_lower_deviation'),
                label='输入参数',
                show_border=True
            ),
            VGroup(
                Item('calculate', show_label=False),
                Item('max_gap'),
                Item('min_gap'),
                label='操作',
                show_border=True
            ),
            # 结果显示部分可以根据需要添加
        ),
        resizable=True,
        title='间隙计算器'
    )

    # 监听按钮点击事件
    @on_trait_change('calculate')
    def calculate_gap(self):
        self.max_gap, self.min_gap = calculate_gaps(
            self.basic_size,
            self.hole_upper_deviation,
            self.hole_lower_deviation,
            self.shaft_upper_deviation,
            self.shaft_lower_deviation
        )
        self.max_gap=round(self.max_gap,3)
        self.min_gap=round(self.min_gap,3)
        #message(f"最大间隙: {max_gap:.2f}\n最小间隙: {min_gap:.2f}", title="间隙计算结果")


# 计算间隙的函数，与GUI分离以便复用和测试
def calculate_gaps(basic_size, hole_upper_deviation, hole_lower_deviation,
                   shaft_upper_deviation, shaft_lower_deviation):
    shaft_upper_limit = basic_size + shaft_upper_deviation
    shaft_lower_limit = basic_size + shaft_lower_deviation
    hole_upper_limit = basic_size + hole_upper_deviation
    hole_lower_limit = basic_size + hole_lower_deviation

    max_gap = hole_upper_limit - shaft_lower_limit
    min_gap = hole_lower_limit - shaft_upper_limit

    return max_gap, min_gap


# 创建并运行GUI
if __name__ == '__main__':
    calculator = GapCalculator()
    calculator.configure_traits()