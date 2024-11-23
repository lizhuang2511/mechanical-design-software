import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


class HelicalSpringDesign:
    def __init__(self, F1, F2, h, G, sigma, D1_min):
        self.F1 = F1  # 最小工作载荷
        self.F2 = F2  # 最大工作载荷
        self.h = h  # 载荷变化量
        self.G = G  # 材料的剪切模量
        self.sigma = sigma  # 材料的许用应力
        self.D1_min = D1_min  # 弹簧直径
        self.应力许用系数=0.45
        # 以下是计算过程中会用到的变量，但可能不需要在构造函数中初始化
        # 可以在需要时再在相应的方法中定义
        # 比如：self.tau_p, self.Cj, self.Kq, self.ds, self.Kj, self.nj 等

    def determine_wire_diameter(self, ds, sigma_b, C):
        self.ds=ds#钢丝直径
        self.C=C#旋绕比
        self.tau_p = self.应力许用系数 * sigma_b  # 许用应力
        self.sigma_b=sigma_b
        self.Kq = (4 * self.C - 1) / (4 * self.C - 4) + 0.615 / self.C  # 圈间接触应力修正系数
        self.dj = math.sqrt(8 * self.Kq * self.F2 * self.C / (math.pi * self.tau_p))  # 计算直径
        self.Cjj = self.D1_min / self.ds  # 计算旋绕比
        #if self.dj > self.ds:
            #return None, None, None, None, False,None
        #else:
        return self.tau_p, self.Cjj, self.Kq, self.ds, True,self.dj

    def determine_coil_number(self):
        self.Kj = (self.F2 - self.F1) / self.h  # 刚度
        self.nj = self.G * self.ds / (8 * self.Cjj ** 3 * self.Kj)  # 计算弹簧圈数
        return self.Kj, self.nj

    def pilao(self,xishu):
        最小应力=8*self.Kq*self.F1*self.D2/(math.pi*self.ds**3)
        最大应力 = 8 * self.Kq * self.F2 * self.D2 / (math.pi * self.ds ** 3)
        疲劳许用应力=xishu*self.sigma_b
        安全系数=(疲劳许用应力+0.75*最小应力)/最大应力
        return 最小应力,最大应力,疲劳许用应力,安全系数
    def check_stability(self,  n, n2, delta, Y, DBZC):
        self.n = n
        self.n2 = n2
        self.delta = delta
        self.Y = Y
        self.DBZC = DBZC
        # 计算弹簧的刚度和变形量
        self.Kp = self.G * self.ds / (8 * self.C ** 3 * self.n)
        self.f1 = self.F1 / self.Kp
        self.f2 = self.F2 / self.Kp
        self.D2 = self.Cjj * self.ds  # 外径
        self.t = (1 + delta) * self.ds + (self.f2 / n)  # 节距
        # 根据条件计算H0
        if Y == 1:
            self.H0 = self.n * self.t + (n2 - 0.5) * self.ds
        elif Y == 2:
            self.H0 = self.n * self.t + (n2 + 1) * self.ds
        self.b = self.H0 / self.D2  # 高径比

        bx, Cby = [], []
        if DBZC == 3:
            bx = [5.3, 5.4, 5.5, 5.75, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10]
            Cby = [0.80, 0.65, 0.60, 0.45, 0.40, 0.325, 0.265, 0.225, 0.19, 0.165, 0.145, 0.125]
        elif DBZC == 2:
            bx = [3.7, 3.85, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]
            Cby = [0.80, 0.60, 0.50, 0.31, 0.24, 0.20, 0.17, 0.15, 0.13, 0.105, 0.08, 0.075]
        elif DBZC == 1:
            bx = [1,2.0,2.6, 2.8, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10]
            Cby = [0.9,0.9,0.8, 0.5, 0.4, 0.27, 0.21, 0.15, 0.12, 0.09, 0.075, 0.05, 0.04, 0.03, 0.025]

        Cb_interpolator = interp1d(bx, Cby, kind='cubic', fill_value='extrapolate')
        self.Cb = Cb_interpolator(self.b)  # 插值得到的Cb

        self.Fc = self.Cb * (self.G * self.ds / (8 * self.C ** 3 * n)) * self.H0  # 临界载荷
        stable = self.Fc >= self.F2

        return self.Cb, self.Fc, stable, self.b, bx, Cby

    def plot_stability_diagram(self, save_path=None):
        # 这里假设check_stability方法已经被调用过，因此self.Cb, self.b等值已经存在
        plt.plot(self.bx, self.Cby, 'ro', label='Original Data')
        plt.plot(self.b, self.Cb, label='Interpolated Result')
        plt.grid(True)
        plt.xlabel('b')
        plt.ylabel('Cb')
        plt.title('Spring Instability Coefficient Diagram')
        plt.legend()

        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

        # 使用示例

if __name__ == "__main__":
  spring_design = HelicalSpringDesign(F1=500, F2=1200, h=60, G=7.85e4, sigma=1420, D1_min=50)
# ...（后续调用方法计算相关属性）