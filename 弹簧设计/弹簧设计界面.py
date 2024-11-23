from traits.api import HasTraits, Instance, Str, Button, Float, Int, Bool, Enum
from traitsui.api import View, Item, HGroup, VGroup, Spring, UItem, Handler, Tabbed,Group
from traitsui.editors.instance_editor import InstanceEditor
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from 弹簧设计类 import HelicalSpringDesign
from traits.api import HasTraits, Range ,Int,List,Button,observe,Enum,Str,Float,Password
from traitsui.api import Item, Group, View,CheckListEditor,Handler,VGrid,HGroup,VGroup,Font,TextEditor
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('SimSun', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
from pdf阅读3 import PdfViewer
class HelicalSpringDesignUI(HasTraits):
    # 绑定HelicalSpringDesign实例
    spring_design = Instance(HelicalSpringDesign)

    # 定义界面上的输入参数
    F1 = Float(121, label='最小工作载荷')
    F2 = Float(260, label='最大工作载荷')
    h = Float(36, label='载荷变化量')
    G = Float(7.85e4, label='材料的剪切模量')
    sigma = Float(1420, label='弹簧丝强度极限')
    D1_min = Float(53, label='弹簧直径')

    # 其他可能需要显示的参数
    tau_p = Float(label='许用应力')
    Cj = Float(label='计算旋绕比')
    Kq = Float(label='曲度系数')
    dj = Float(label='最小直径')
    ds = Float(5,label='钢丝直径')
    c = Float(8,label='旋绕比')
    Kj = Float(label='刚度')
    nj = Float(label='计算弹簧圈数')
    n1= Float(11,label='输入弹簧圈数')
    n2=Float(2,label='输入弹簧支撑圈数')
    Cb = Float(label='Cb值')
    Fc = Float(label='临界载荷')
    b = Float(label='高径比')
    f1 = Float(label='最小变形量')
    f2=Float(label='最大变形量')
    Kp = Float(label='弹簧计算刚度')
    H0 = Float(label='弹簧高度')
    stable = Bool(label='是否稳定')
    delta = Float(0.1,label='弹簧相邻间隙系数')
    应力许用系数 = Float(0.45, label='应力许用系数')
    # 枚举类型用于下拉选择
    Y_options = Enum(1, 2, label='Y值')
    DBZC_options = Enum(1, 2, 3, label='DBZC值')
    c显示材料 = Button('材料参考')
    c显示推荐直径 = Button('显示推荐直径')
    c显示圈数计算方法 = Button('显示圈数计算方法')
    c类型选择 = Button('显示类型选择参考')
    # 按钮用于触发计算
    calculate_wire_diameter = Button('计算钢丝直径')
    calculate_coil_number = Button('计算圈数')
    check_stability_btn = Button('检查稳定性')
    共振= Float(0)
    最大应力=Float(0)
    最小应力=Float(0)
    疲劳应力系数=Float(0.3)
    疲劳许用应力=Float(0)
    安全系数=Float(0)
    btnpilao = Button('检查疲劳')
    #figure = Instance(FigureCanvas)
    @observe("c显示材料")
    def 显示材料(self, event):
        print('a')
        default_file_path = "..\数据文件\弹簧材料.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    @observe("c显示推荐直径")
    def 显示推荐直径(self, event):
        print('a')
        default_file_path = "..\数据文件\钢丝选择.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    # 图形显示
    @observe("c显示圈数计算方法")
    def 显示圈数计算方法(self, event):
        print('a')
        default_file_path = "..\数据文件\圈数和疲劳.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return

    @observe("c类型选择")
    def 类型选择(self, event):
        print('a')
        default_file_path = "..\数据文件\类型选择.pdf"
        self.viewer = PdfViewer(default_file_path)
        self.viewer.show()
        return
    # 图形显示


    # TraitsUI视图定义
    viewid = Group(HGroup(
            VGroup(
                    VGrid(Item('F1'),Item('F2'),
                    Item('h'),Item('G'),
                    Item('sigma'),Item('c显示材料'),
                    Item('D1_min'),Item('c'),
                    #springy=True,
                    Item('ds'),Item('c显示推荐直径')),
                    Item('应力许用系数'),
                    Item('calculate_wire_diameter'),
                    Item('tau_p', style='readonly'),
                    Item('Cj', style='readonly'),
                    Item('Kq', style='readonly'),
                    Item('dj', style='readonly'),
                    springy=True,
                ),label='计算直径'),
                HGroup(VGroup(VGrid(
                    Item('calculate_coil_number'),Item('c显示圈数计算方法'),
                    Item('Kj', style='readonly'),Item('nj', style='readonly'),
                    Item('n2'),Item('n1'), ),
                    #springy=True,
                    VGrid(Item('delta'),
                        Item('Y_options', label='Y'),
                    Item('DBZC_options', label='DBZC'),
                    Item('c类型选择'),Item('check_stability_btn'),),
                    VGrid(Item('Cb', style='readonly'),Item('Fc', style='readonly'),
                    Item('b', style='readonly'),Item('H0', style='readonly'),
                    Item('f1', style='readonly'), Item('f2', style='readonly'),
                    Item('Kp', style='readonly'), Item('stable', style='readonly'),),

                    #springy=True,
                    #UItem('figure', editor=InstanceEditor(view='figure_view')),
                    springy=True
                    ),label='计算圈数'),
        HGroup(VGroup(VGrid(
            Item('共振'), Item('疲劳应力系数'),
            Item('最大应力'),Item('最小应力')
            , Item('疲劳许用应力'),Item('安全系数'),),
            Item('btnpilao'),
            # springy=True,
            # UItem('figure', editor=InstanceEditor(view='figure_view')),
            springy=True
        ), label='计算疲劳')
        ,layout='tabbed',style_sheet='*{font-size:25px}')

    traits_view = View(viewid,
                       title='压缩弹簧计算',
                       resizable=True,
                       kind="live",
                       width = 1000,
                       height = 500,

        )

    ''''# 图形视图定义
    figure_view = View(
        Item(
            'figure',
            editor=InstanceEditor(),
            show_label=False,
            width=600,
            height=400
        ),
        resizable=True
    )'''
    def _ds_changed(self):
        self.c=self.D1_min/self.ds
        return
    def _D1_min_changed(self):
        self.c=self.D1_min/self.ds
        return
    def _c_changed(self):
        self.ds=self.D1_min/self.c
        return
    def _btnpilao_fired(self):
        值=self.spring_design.pilao(self.疲劳应力系数)
        self.最小应力=值[0]
        self.最大应力 = 值[1]
        self.疲劳许用应力 = 值[2]
        self.安全系数= 值[3]
        return
    # 按钮点击事件处理
    def _calculate_wire_diameter_fired(self):
        # 假设C已经给定或者可以在其他地方设置
        self.a动态修正类()
        sigma_b = self.sigma  # 假设扭转应力等于许用应力
        tau_p, Cj, Kq, ds, success,dj = self.spring_design.determine_wire_diameter(ds=self.ds, sigma_b=sigma_b, C=self.c)

        if success:
            self.tau_p = tau_p
            self.Cj = Cj
            self.Kq = Kq
            self.ds = ds
            self.dj=dj
        else:
            self.tau_p = None
            self.Cj = None
            self.Kq = None
            self.ds = None

    def _calculate_coil_number_fired(self):
        Kj, nj = self.spring_design.determine_coil_number()
        self.Kj = Kj
        self.nj = nj

    def _check_stability_btn_fired(self):
        n = self.n1 # 假设等于之前计算的nj
        n2 = self.n2  # 示例值，需要根据实际情况调整
        delta = self.delta  # 示例值0.1
        Cb, Fc, stable, b, bx, Cby = self.spring_design.check_stability(n=n, n2=n2, delta=delta, Y=self.Y_options,
                                                                        DBZC=self.DBZC_options)
        self.Cb = Cb
        self.Fc = Fc
        self.stable = stable
        self.b = b
        self.Kp = self.spring_design.Kp
        self.f1 = self.spring_design.f1
        self.f2 = self.spring_design.f2
        self.H0=self.spring_design.H0
        # 更新图形显示
        self.update_plot(bx, Cby, b, Cb)

    def update_plot(self, bx, Cby, b, Cb):
        #plt.clf()
        plt.plot(bx, Cby, 'ro', label='Original Data')
        plt.plot(b, Cb, 'bo', label='Interpolated Result')
        plt.grid(True)
        plt.xlabel('b')
        plt.ylabel('Cb')
        plt.title('Spring Instability Coefficient Diagram')
        plt.legend()
        plt.show()
    def a动态修正类(self):
        # Traits初始化函数
        self.spring_design.F1=self.F1; self.spring_design.F2 = self.F2; self.spring_design.h = self.h; \
        self.spring_design.G = self.G; self.spring_design.sigma = self.sigma; self.spring_design.D1_min = self.D1_min;
        self.spring_design.应力许用系数=self.应力许用系数
        return
    def _spring_design_default(self):
        return HelicalSpringDesign(F1=self.F1, F2=self.F2, h=self.h, G=self.G, sigma=self.sigma, D1_min=self.D1_min)

    '''def _figure_default(self):
        fig = plt.figure(figsize=(8, 6))
        canvas = FigureCanvas(fig)
        return canvas'''

    # 使用示例


if __name__ == "__main__":
    spring_design_ui = HelicalSpringDesignUI()
    spring_design_ui.configure_traits()
    print('a')