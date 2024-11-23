from traits.api import HasTraits, Float, Int, Bool, Str, Enum, Instance,Button,observe
from traitsui.api import View, Item, Group, HGroup, VGroup, Label, Spring, ButtonEditor
from traitsui.key_bindings import KeyBinding, KeyBindings
from traitsui.menu import OKButton, CancelButton


# 花键参数类
class SplineParameters(HasTraits):
    # 输入参数
    T = Float(7300000.0,label='传递的转矩 (N·mm)' )
    psi = Float(0.75,label='各齿间载荷不均匀系数', )
    Z = Int(27,label='花键的齿数', )
    l = Float(140.0,label='齿的工作长度 (mm)', )
    d_m = Float(129.0,label='平均直径 (mm)', )
    C = Float(1.0,label='倒角尺寸 (mm)', )
    m = Float(5,label='模数 (mm)', )
    alpha_D = Enum(30,45,label='压力角 (°)', )
    spline_type = Enum( 'Involute','Rectangular', label='花键类型')
    connection_type = Enum( 'Dynamic','Static', label='连接类型', value='Static')

    # 计算属性
    h = Float(label='工作高度 (mm)')
    sigma_p = Float(label='σp (MPa)')
    p = Float(label='p (MPa)')
    result_message = Str(label='结果信息')
    calculate=Button('计算')
    静态许用应力设定=Float(100,label='静态许用应力Mpa',)
    动态许用应力设定 = Float(15,label='动态许用应力Mpa',)
    # UI视图定义
    view = View(
        VGroup(
            HGroup(
                Item('spline_type', label='选择花键类型'),
                Spring(),
                Item('calculate'),
                Item('connection_type', label='连接类型'),
            ),
            Group(
                Item('T'),
                Item('psi'),
                Item('Z'),
                Item('l'),
                Item('d_m'),
                Item('C'),
                Item('静态许用应力设定'),
                Item('动态许用应力设定'),
                visible_when='spline_type=="Rectangular"',
                label='矩形花键参数',
                #show_border=True,
            ),
            Group(
                Item('T'),
                Item('psi'),
                Item('Z'),
                Item('l'),
                Item('d_m'),
                Item('m'),
                Item('alpha_D'),
                Item('静态许用应力设定'),
                Item('动态许用应力设定'),
                visible_when='spline_type=="Involute"',
                label='渐开线花键参数',
                #show_border=True,
            ),
            Group(
                Item('sigma_p', style='readonly'),
                Item('p', style='readonly'),
                Item('result_message', style='readonly'),  # Adjust height as needed
                label='计算结果',
                #show_border=True,
            ),
        ),
        title='花键连接强度计算',
        buttons=[OKButton, CancelButton],
        kind='live',
        resizable=True,
        width=500,  # Adjust width as needed for better layout
        height=400  # Adjust height as needed for better layout
    )

    # 初始化工作高度和其他属性（基于花键类型）
    def _spline_type_changed(self):
        if self.spline_type == 'Rectangular':
            self.h = ( self.d_m - 2 * self.C) / 2  # This is a placeholder calculation, it should be based on actual dimensions
        elif self.spline_type == 'Involute':
            if self.alpha_D == 30:
                self.h = self.m
            elif self.alpha_D == 45:
                self.h = 0.8 * self.m

                # 计算按钮的点击事件

    @observe("calculate")
    def calculate1(self,event):
        self._spline_type_changed()
        # 这里需要基于连接类型来决定使用哪个公式进行计算
        if self.connection_type == 'Static':
            print(self.T,self.psi,self.Z,self.l,self.h ,self.d_m)
            self.sigma_p =int( (2 * self.T) / (self.psi * self.Z * self.l * self.h * self.d_m))
            self.p = 0  # For simplicity, let's assume p is the same as sigma_p for static connections
            self.result_message = '静连接安全系数:'+str(round(self.静态许用应力设定/self.sigma_p,2))
        elif self.connection_type == 'Dynamic':
            # Here you would have a different formula for dynamic connections
            self.sigma_p =int((2 * self.T) / (self.psi * self.Z * self.l * self.h * self.d_m))
            self.p =  int((2 * self.T) / (self.psi * self.Z * self.l * self.h * self.d_m) )# For simplicity, let's assume p is the same as sigma_p for static connections
            self.result_message = '静连接安全系数:'+str(round(self.静态许用应力设定/self.sigma_p,2))+'-----动连接安全系数:'+str(round(self.动态许用应力设定/self.p,2))

            # 这里可以添加对结果的进一步处理，比如与许用值进行比较并给出合格与否的判断等。

    # Default values and trait initialization
    def __init__(self, **traits):
        super().__init__(**traits)
        self._spline_type_changed()  # Initialize h based on spline_type default value


# 运行UI
if __name__ == '__main__':


    spline_parameters = SplineParameters()
    spline_parameters.configure_traits()