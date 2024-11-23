# -*- coding = utf-8 -*-
# @time:2024/3/15 12:49
# Author:lizhuang
# @File:过盈计算.py
# @Software:PyCharm
from traits.api import HasTraits, Float, Instance, Str, Button,Enum,cached_property,Property
from traitsui.api import View, Item, Group, HGroup, VGroup, Spring, Handler
from traitsui.table_column import ObjectColumn
from traitsui.table_filter import TableFilter
import re
# 定义摩擦系数的枚举值
friction_coefficients = [
    "钢-钢 无润滑 (0.07 ~ 0.16)",
    "钢-钢 有润滑 (0.05 ~ 0.13)",
    "钢-青铜 无润滑 (0.15 ~ 0.20)",
    "钢-青铜 有润滑 (0.03 ~ 0.06)",
    # ... 其他组合
    "铸铁-铸铁 无润滑 (0.15 ~ 0.25)",
    "铸铁-铸铁 有润滑 (0.05 ~ 0.10)",
]
# 定义材料列表和对应的弹性模量、泊松系数
materials = [
    ("碳钢、低合金钢、合金结构钢", 215000, 0.305),  # 选择范围内的中间值作为代表值
    ("灰铸铁 HT 150HT 200", 75000, 0.245),
    ("灰铸铁 HT 250HT 300", 115000, 0.25),
    ("可钤铸铁", 95000, 0.25),
    ("非合金球墨铸铁", 170000, 0.285),
    ("青铜", 85000, 0.35),
    ("黄铜", 80000, 0.365),
    ("铝合金", 69000, 0.34),  # 选择范围内的中间值作为代表值
    ("镁铝合金", 40000, 0.275),
]
material_names = [material[0] for material in materials]
representative_elastic_moduli = [material[1] for material in materials]
representative_poisson_ratios = [material[2] for material in materials]
class PressureCalculation(HasTraits):
    material_combination = Enum(friction_coefficients[0], friction_coefficients)
    d_f = Float(100,label='结合直径 (mm)')
    L_f = Float(40,label='结合长度 (mm)')
    mu = Float(0.1,label='摩擦系数')
    delta_max = Float(0.02,label='最大过盈量 (mm)')
    d_a = Float(150,label='包容件外径 (mm)')
    d_i = Float(80,label='被包容件内径 (mm)', desc="若为实心轴则为0")

    calculate_button = Button(label='计算压入力')

    p_fmax = Float(label='最大单位压力 (N/mm^2)')
    P = Float(label='压入力 (N)')
    selected_materialin = Enum(material_names[0], material_names)
    selected_materialout = Enum(material_names[0], material_names)
    elastic_modulusin = Property(Float, depends_on='selected_materialin')
    poisson_ratioin = Property(Float, depends_on='selected_materialin')
    elastic_modulusout = Property(Float, depends_on='selected_materialout')
    poisson_ratioout = Property(Float, depends_on='selected_materialout')

    # 其他属性和方法...

    @cached_property
    def _get_elastic_modulusin(self):
        return representative_elastic_moduli[material_names.index(self.selected_materialin)]

    @cached_property
    def _get_poisson_ratioin(self):
        return representative_poisson_ratios[material_names.index(self.selected_materialin)]
    @cached_property
    def _get_elastic_modulusout(self):
        return representative_elastic_moduli[material_names.index(self.selected_materialout)]

    @cached_property
    def _get_poisson_ratioout(self):
        return representative_poisson_ratios[material_names.index(self.selected_materialout)]
    def _extract_friction_range(self, friction_str):
        # 使用正则表达式提取摩擦系数范围的两个浮点数
        match = re.search(r'\((\d+\.\d+ ~ \d+\.\d+)\)', friction_str)
        if match:
            range_str = match.group(1)
            low, high = map(float, range_str.split(' ~ '))
            return low, high
        else:
            raise ValueError("无法从字符串中提取摩擦系数范围")

    def _calculate_median(self, low, high):
        # 计算范围的中位数（这里简单地取平均值作为中位数）
        return (low + high) / 2
    # 当材料组合改变时更新摩擦系数显示
    def _material_combination_changed(self):
        low, high = self._extract_friction_range(self.material_combination)
        median_mu = self._calculate_median(low, high)
        self.mu = round(median_mu,2)
    def _calculate_button_fired(self):
        # 提取摩擦系数范围并计算中位数
        try:
            low, high = self._extract_friction_range(self.material_combination)
            median_mu = self._calculate_median(low, high)
            self.mu=round(median_mu,2)
            # 使用中位数进行计算（这里需要添加实际的计算逻辑）
            # 例如: self.p_fmax = ... (使用median_mu进行计算)
            #      self.P = ... (使用median_mu和其他参数进行计算)

            # 占位符，表示计算已经完成（实际应用中需要替换为真实的计算逻辑）
            C_a= (self.d_a ** 2 + self.d_f ** 2) / (self.d_a ** 2 - self.d_f ** 2) + self.poisson_ratioout
            C_i= (self.d_f ** 2 + self.d_i ** 2) / (self.d_f ** 2 - self.d_i ** 2) - self.poisson_ratioin
            self.p_fmax =round( self.delta_max / (self.d_f * ((C_a / self.elastic_modulusout) + (C_i / self.elastic_modulusin))),2)
            self.P = round(self.p_fmax * math.pi * self.d_f * self.L_f * self.mu,2)

        except ValueError as e:
            # 处理无法提取摩擦系数范围的情况（例如用户输入了无效的字符串）
            print(f"错误: {e}")
            self.p_fmax = 0.0
            self.P = 0.0
    view = View(
        VGroup(
            HGroup(
                Item('d_f'),
                Item('L_f'),
            ),
            HGroup(
                Item('delta_max'),
                Item('d_a'),
                Item('d_i'),
            ),
            HGroup(Item('material_combination', label='选择材料组合和润滑情况'),
                Item('mu'),),

            HGroup(
                Item('selected_materialin', label='选择材料被包容件'),
                Item('elastic_modulusin', label='被包容件弹性模量 (N/mm^2)', ),
                Item('poisson_ratioin', label='被包容件泊松系数', ),
            ),
            HGroup(     Item('selected_materialout', label='选择材料包容件'),
                Item('elastic_modulusout', label='包容件弹性模量 (N/mm^2)', ),
                Item('poisson_ratioout', label='包容件泊松系数', ),

            ),
            Item('calculate_button', show_label=False),
            HGroup(

                Item('p_fmax', style='readonly'),
            ),
            HGroup(

                Item('P', style='readonly'),
            ),
        ),
        title='压入力计算器',
        buttons=[],
        resizable=True,
        width=400,
        height=300
    )



    # 主程序入口


if __name__ == '__main__':
    # 修正代码：需要导入math模块
    import math

    # 创建计算对象
    calc = PressureCalculation()

    # 配置用户界面
    calc.configure_traits()
