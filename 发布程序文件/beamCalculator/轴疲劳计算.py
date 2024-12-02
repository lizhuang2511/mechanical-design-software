def calculate_effective_stress_concentration_factor(k_sigma, beta, epsilon_sigma):
    """
    计算修正后的有效应力集中系数 (k_sigma)_D。

    参数:
    k_sigma -- 理论应力集中系数
    beta -- 表面状态系数
    epsilon_sigma -- 尺寸系数

    返回:
    (k_sigma)_D -- 修正后的有效应力集中系数
    """
    # 使用公式 (1-8) 来计算 (k_sigma)_D
    _D = k_sigma / (beta * epsilon_sigma)
    return _D
# 示例性的函数实现
# 计算ψ值的函数
def calculate_psi(sigma_minus_1, sigma_0):
    psi_sigma = (2 * sigma_minus_1 - sigma_0) / (sigma_0)
    return psi_sigma

# 计算安全系数的函数
def calculate_safety_factor(sigma_min, sigma_max, sigma_minus_1, sigma_0, comprehensive_influence_coefficient,
                            allowable_safety_factor):
    sigma_a=(sigma_max-sigma_min)/2
    sigma_m = (sigma_max + sigma_min) / 2
    comprehensive_influence_coefficient = comprehensive_influence_coefficient
    psi_sigma = calculate_psi(sigma_minus_1, sigma_0)
    S_ca = sigma_minus_1 / (comprehensive_influence_coefficient * sigma_a + psi_sigma * sigma_m)
    yingli=(comprehensive_influence_coefficient * sigma_a + psi_sigma * sigma_m)
    return S_ca / allowable_safety_factor, sigma_m,yingli # 返回实际安全系数与许用安全系数的比值


from traits.api import Float, Instance, Button, HasTraits, Str, on_trait_change,observe,Enum
from traitsui.api import View, Item, HGroup, VGroup, Label,VGrid,TextEditor,Group
from traitsui.message import message
from traitsui.handler import Handler
from pdf阅读3 import PdfViewer

# Your original functions remain the same
# ... [Your calculate_effective_stress_concentration_factor, calculate_psi, and calculate_safety_factor functions] ...

class StressAnalysisHandler(Handler):
    def object_calculate_clicked(self, info):
        info.object.calculate()


class StressAnalysis(HasTraits):
    # Define traits for input fields
    k_sigma_theoretical = Float(1.6, label='应力集中系数 (k_sigma)')
    beta_coefficient = Float(0.8, label='表面影响系数(beta)')
    epsilon_sigma_coefficient = Float(0.8, label='尺寸影响系数 (epsilon_sigma)')
    sigma_min = Float(0, label='名义最小应力 (sigma_min)')
    sigma_max = Float(180, label='名义最大应力(sigma_max)')
    sigma_minus_1 = Float(370, label='对称循环疲劳极限(sigma_minus_1)')
    sigma_0 = Float(360, label='脉动循环疲劳极限 (sigma_0)')
    allowable_safety_factor = Float(1.5, label='允许安全系数')

    # Output fields
    k_sigma_effective = Float(0.0, label='((k_sigma)_D)')
    psi_sigma = Float(0.0, label='系数平均应力(ψ)')
    safety_factor = Float(0.0, label='安全系数')
    计算应力=Float(0.0, label='计算应力')
    calculate = Button('Calculate')
    大直径=Float(100,)
    小直径=Float(90,)
    圆角=Float(2,)
    系数1 = Float(0.0,label='(D-d)/r' )
    系数2= Float(0.0, label='r/d')
    xianshi = Button('集中系数')
    jisuanfuzhu = Button('计算辅助')
    材料选择 = Enum(['结构钢', '铸铁', '铝合金', '青铜'])
    xianshi2=Button('材料应力查询')
    # Button to trigger calculations
    xgms=Float(785,)
    xgmb=Float(570,)
    jianhaujisuan = Button('简化计算极限应力')

    # Define the view for the GUI
    traits_view = View(
        Group(VGroup(
            HGroup(
                VGroup(
                    Item('k_sigma_theoretical'),
                    Item('beta_coefficient'),
                    Item('epsilon_sigma_coefficient'),
                    Item('sigma_min'),
                    Item('sigma_max'),
                    Item('sigma_minus_1'),
                    Item('sigma_0'),
                    Item('allowable_safety_factor'),
                    Item('calculate', ),
                    label='Input Parameters',
                    show_border=True
                ),
                VGroup(
                VGrid(
                    Item('大直径', ),
                    Item('小直径'),
                    Item('圆角', ),
                    Item('jisuanfuzhu', ),
                    Item('系数1', ),
                    Item('系数2', ),
                    Item('xianshi',),
                    Item('xianshi2', ),
                    Item('xgms'),
                    Item('xgmb', ),
                    Item('材料选择', ),
                    Item('jianhaujisuan', ),
                    label='辅助系数计算',
                    show_border=True,
                ),
                VGrid(
                    Item('计算应力', style='readonly',editor=TextEditor(format_str='%.2f')),
                    Item('k_sigma_effective', style='readonly',editor=TextEditor(format_str='%.2f')),
                    Item('psi_sigma', style='readonly',editor=TextEditor(format_str='%.2f')),
                    Item('safety_factor', style='readonly',editor=TextEditor(format_str='%.2f')),
                    label='output Parameters',
                    show_border=True,
                ),),
            ),
        ),style_sheet='*{font-size:18px}'),
        handler=StressAnalysisHandler(),
        #resizable=True,
        title='Stress Analysis Calculator'
    )

    @observe('jisuanfuzhu')
    def calculate2(self, event):
        self.系数1=round((self.大直径-self.小直径)/self.圆角,3)
        self.系数2 = round(self.圆角/self.小直径,3)
        return

    @observe('xianshi')
    def xianshi1(self, event):
        default_file_path = r"..\数据文件\常用应力集中系数.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    @observe('xianshi2')
    def xianshi3(self, event):
        default_file_path = r"..\数据文件\轴材料.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return

    @observe('jianhaujisuan')
    def jianhaujisuan1(self, event):
        if self.材料选择=='结构钢':
            self.sigma_minus_1=0.27*(self.xgms+self.xgmb)
            self.sigma_0=self.sigma_minus_1
        if self.材料选择=='铸铁':
            self.sigma_minus_1=0.4*(self.xgmb)
            self.sigma_0=self.sigma_minus_1
        if self.材料选择=='铝合金':
            self.sigma_minus_1=1/6*(self.xgmb)-7.5
            self.sigma_0=self.sigma_minus_1
        if self.材料选择=='青铜':
            self.sigma_minus_1=0.21*(self.xgmb)
            self.sigma_0=self.sigma_minus_1
        self.sigma_minus_1=round(self.sigma_minus_1,2)
        self.sigma_0 = self.sigma_minus_1
        return
    # Event handler for the calculate button
    @observe('calculate')
    def calculate1(self, event):
        # Calculate effective stress concentration factor
        self.k_sigma_effective = calculate_effective_stress_concentration_factor(
            self.k_sigma_theoretical,
            self.beta_coefficient,
            self.epsilon_sigma_coefficient
        )
        # Calculate psi
        self.psi_sigma = calculate_psi(self.sigma_minus_1, self.sigma_0)
        a=calculate_safety_factor(
            self.sigma_min,
            self.sigma_max,
            self.sigma_minus_1,
            self.sigma_0,
            self.k_sigma_effective,
            self.allowable_safety_factor
        )
        # Calculate safety factor
        self.safety_factor = a[0]
        self.计算应力=a[2]
        # Optionally, display a message indicating calculations are done
        #message("Calculations completed!")

    # Create and run the GUI

if __name__ == "__main__":
   analysis = StressAnalysis()
   analysis.configure_traits()
