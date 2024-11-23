import math

# 已知条件
F1 = 500
F2 = 1200
h = 60
G = 7.85e4
sigma = 1420
D1_min = 50

# 1-按照强度条件确定弹簧丝直径
# 由于弹簧丝材料强度与它的直径相关，需要采用试算法
ds = float(input('    试选弹簧丝直径(mm) ds = '))
sigma_b = float(input('    按照表16-3，选择弹簧丝强度极限(MPa) sigma_b = '))
tau_p = 0.45 * sigma_b
print(f'  许用剪切应力 tau_p = {tau_p:.4f} MPa')

Cj = D1_min / ds + 1
print(f'  计算弹簧指数 Cj = {Cj:.4f}')
C = float(input('    按照表16-5，选择弹簧指数 C = '))
Kq = (4 * C - 1) / (4 * C - 4) + 0.615 / C
print(f'  计算曲度系数 Kq = {Kq:.4f}')
dj = math.sqrt(8 * Kq * F2 * C / (math.pi * tau_p))
print(f'  计算簧丝直径 dj = {dj:.4f}')

if dj > ds:
    print('    不安全，需要重选弹簧丝直径')
else:
    print('    安全')
    d = ds  # 确定弹簧丝直径

# 2-按照刚度条件确定弹簧工作圈数
Kj = (F2 - F1) / h
print(f'  计算弹簧刚度 Kj = {Kj:.4f}')
nj = G * d / (8 * C**3 * Kj)
print(f'  计算弹簧圈数 nj = {nj:.4f}')
n = float(input('    选取弹簧工作圈数 n = '))
n2 = float(input('    选取弹簧支承圈数 n2 = '))
n1 = n + n2
print(f'  弹簧总圈数 n1 = {n1:.4f}')

# 计算弹簧的刚度和变形量
Kp = G * d / (8 * C**3 * n)
f1 = F1 / Kp
f2 = F2 / Kp
print(f'  弹簧实际刚度 Kp = {Kp:.4f} N/mm')
print(f'  弹簧最小变形量 f1 = {f1:.4f} mm')
print(f'  弹簧最大变形量 f2 = {f2:.4f} mm')
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 弹簧稳定性校核
D2 = C * d
print(f'  弹簧中径  D2 = {D2:.4f} mm')
delta = float(input('    选取相邻两圈弹簧丝间隙系数 delta = '))#0.1
t = (1 + delta) * d + f2 / n  # 圆柱螺旋压缩弹簧
print(f'  弹簧节距   t = {t:.4f} mm')
Y = int(input('    选取弹簧端部结构类型 Y = '))  # 弹簧端部结构类型:1或是2
if Y == 1:
    H0 = n * t + (n2 - 0.5) * d
elif Y == 2:
    H0 = n * t + (n2 + 1) * d
print(f'  弹簧自由高度  H0 = {H0:.4f} mm')
b = H0 / D2
print(f'  弹簧高径比     b = {b:.4f}')

# 采用3次样条插值确定圆柱螺旋弹簧不稳定系数Cb
DBZC = int(input('    选取弹簧端部支承类型 DBZC = '))  # 弹簧端部支承类型:1、2、3
bx, Cby = [], []
if DBZC == 1:  # 弹簧两端固定支承
    bx = [5.3, 5.4, 5.5, 5.75, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10]
    Cby = [0.80, 0.65, 0.60, 0.45, 0.40, 0.325, 0.265, 0.225, 0.19, 0.165, 0.145, 0.125]
elif DBZC == 2:  # 弹簧一端固定、一端自由支承
    bx = [3.7, 3.85, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]
    Cby = [0.80, 0.60, 0.50, 0.31, 0.24, 0.20, 0.17, 0.15, 0.13, 0.105, 0.08, 0.075]
elif DBZC == 3:  # 弹簧两端自由支承
    bx = [2.6, 2.8, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10]
    Cby = [0.8, 0.5, 0.4, 0.27, 0.21, 0.15, 0.12, 0.09, 0.075, 0.05, 0.04, 0.03, 0.025]

Cb_interpolator = interp1d(bx, Cby, kind='cubic', fill_value='extrapolate')
Cb = Cb_interpolator(b)
print(f'  弹簧不稳定系数    Cb = {Cb:.4f}')

# 绘制圆柱螺旋弹簧不稳定系数Cb线图
plt.plot(bx, Cby, 'ro', label='原始数据')
plt.plot(b, Cb, label='插值结果')
plt.grid(True)
plt.xlabel('b')
plt.ylabel('Cb')
plt.title('弹簧不稳定系数线图')
plt.legend()
plt.show()

Fc = Cb * Kp * H0
print(f'  弹簧稳定临界载荷  Fc = {Fc:.4f} N')

if Fc < F2:
    print('    弹簧工作不稳定，需要改变参数或是加装导向装置')
else:
    print('    弹簧工作稳定')
