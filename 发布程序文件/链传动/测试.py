


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')  # 或者尝试其他后端，如 'Agg', 'GTK3Agg' 等
import matplotlib.pyplot as plt
# 输入数据（行名和列名的值）
'''x_data = np.array([11, 13, 15, 17, 19, 21, 23, 25, 100])
y_data = np.array([0, 0.1, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2])
z_data = np.array([
    [31.29, 31.29, 31.29, 31.78, 31.98, 32.47, 32.47, 32.86, 32.86],
    [31.29, 31.29, 31.29, 31.78, 31.98, 32.47, 32.47, 32.86, 32.86],
    [27.96, 30.02, 30.21, 30.41, 30.41, 31, 31.49, 31.89, 31.89],
    [25.9, 27.57, 28.45, 28.94, 29.33, 29.63, 29.92, 30.51, 30.51],
    [24.13, 26.09, 27.08, 27.76, 28.15, 28.45, 29.04, 29.72, 29.72],
    [22.46, 24.53, 25.7, 26.59, 27.08, 27.57, 27.96, 28.55, 28.55],
    [21.29, 23.35, 24.72, 25.6, 26.39, 26.78, 27.46, 27.96, 27.96],
    [18.64, 21.19, 22.76, 24.03, 24.62, 25.21, 25.8, 26.19, 26.19],
    [16.68, 19.33, 21.09, 22.17, 23.35, 23.94, 24.53, 25.11, 25.11]
])
# 将输入数据转换成适合curve_fit的形式（需要是一维数组）
x_flat = x_data.repeat(len(y_data))
y_flat = np.tile(y_data, len(x_data))
z_flat = z_data.flatten()


# 定义要拟合的二元函数形式（这里以二次多项式为例）
def func(variables, a, b, c, d, e, f):
    x, y = variables
    return a + b * x + c * y + d * x ** 2 + e * y ** 2 + f * x * y
def func1(variables, a, b, c):
    x, y = variables
    return a + b * x + c * y

# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, np.vstack((x_flat, y_flat)), z_flat)

# 输出拟合参数
print("拟合参数:", popt)


# 使用拟合函数预测新的数据点
def predict(x_new, y_new, popt):
    return func((x_new, y_new), *popt)


# 创建一个网格来评估拟合函数
x_min, x_max = x_data.min(), x_data.max()
y_min, y_max = y_data.min(), y_data.max()
x_vals = np.linspace(x_min, x_max, 50)
y_vals = np.linspace(y_min, y_max, 50)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)

# 预测网格上的z值
z_grid = predict(x_grid, y_grid, popt)

# 可视化拟合结果
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis')
ax.scatter(x_flat, y_flat, z_flat, c='red', marker='.')  # 绘制原始数据点
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Visualization of the Fitted Function')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit


# 假设的拟合函数（这只是一个例子，实际上你需要根据你的数据来定义这个函数）
def fitted_func(variables, a, b, c):
    x, y = variables
    return a * x + b * y + c  # 这是一个线性函数，仅作为示例


# 输入数据（这里只是示例数据，你应该使用你自己的数据）
row_values = np.array([1, 2, 3, 4])
column_values = np.array([20, 40, 60, 80])
table_values = np.array([
    [0.69, 0.8, 0.9, 1.0],
    [0.83, 0.95, 1.07, 1.19],
    [1.00, 1.14, 1.28, 1.42],
    [1.20, 1.36, 1.52, 1.68]
])

# 将二维数据展平为一维，以便与curve_fit一起使用
x_flat = row_values.repeat(column_values.size)
y_flat = np.tile(column_values, row_values.size)
z_flat = table_values.flatten()

# 使用curve_fit进行拟合（注意：这里的拟合函数和参数只是示例，并不适用于上述数据）
# 你需要根据你的数据调整拟合函数和初始参数猜测
popt, pcov = curve_fit(fitted_func, np.vstack((x_flat, y_flat)), z_flat, p0=[0, 0, 0])

# 创建一个网格来可视化拟合的函数
x_grid = np.linspace(row_values.min(), row_values.max(), 10)
y_grid = np.linspace(column_values.min(), column_values.max(), 10)
x_grid, y_grid = np.meshgrid(x_grid, y_grid)
z_grid = fitted_func((x_grid, y_grid), *popt)  # 使用拟合的参数计算z值

# 可视化结果
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis')  # 绘制拟合函数的表面
ax.scatter(x_flat, y_flat, z_flat, c='red', marker='.')  # 绘制原始数据点
ax.set_xlabel('Row Values (X)')
ax.set_ylabel('Column Values (Y)')
ax.set_zlabel('Table Values (Z)')
plt.title('3D Visualization of the Fitted Function')
plt.show()'''
'''import numpy as np
from scipy.interpolate import interp2d
x_values = np.array([9.52, 15.87, 25.4, 38.1, 50.8, 63.5, 88.9])
y_values= np.array([1,
                   4,
                   10,
                   50,
                   100,
                   400,
                   1000,
                   2000,
                   3000,
                   4000,
                   ])
z_values= np.array(
    [[7.61, 7.69, 7.87, 8.19, 8.7, 9.24, 10.71],
     [8.73, 8.83, 9.04, 9.4, 9.99, 10.61, 12.3],
     [9.58, 9.68, 9.91, 10.31, 10.95, 11.64, 13.49],
     [11.25, 11.37, 11.64, 12.11, 12.86, 13.67, 15.84],
     [12.05, 12.18, 12.47, 12.98, 13.79, 14.65, 16.98],
     [13.84, 13.99, 14.32, 14.91, 15.83, 16.82, 18],  # 注意这里的18值可能需要处理
     [15.18, 15.34, 15.7, 16.35, 18, 18, 18],  # 同上
     [16.26, 16.44, 16.83, 18, 18, 18, 18],  # 同上
     [16.94, 17.12, 18, 18, 18, 18, 18],  # 同上
     [17.43, 17.62, 18, 18, 18, 18, 18]]
)
print(z_values)
# 创建插值函数
interp_func = interp2d(x_values, y_values, z_values, kind='cubic')

# 现在你可以使用这个函数来插值任意的(x, y)点
# 例如，插值点(0.5, 0.5)
x_new = 12.7
y_new = 720
z_new = interp_func(x_new, y_new)
print(f"The interpolated value at ({x_new}, {y_new}) is {z_new}")
x_fine = np.linspace(x_values.min(), x_values.max(), 100)
y_fine = np.linspace(y_values.min(), y_values.max(), 100)
x_fine_grid, y_fine_grid = np.meshgrid(x_fine, y_fine)

# 使用插值函数计算细网格上的z值
z_fine_grid = interp_func(x_fine, y_fine)

# 创建一个3D图
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
x_grid, y_grid = np.meshgrid(x_values, y_values)

# 将网格展平以用于scatter函数
x_flat = x_grid.flatten()
y_flat = y_grid.flatten()
z_flat = z_values.flatten()
# 绘制原始数据点
#ax.scatter(x_values.flatten(), y_values.flatten(), z_values, color='red', marker='o', label='Original Data')
ax.scatter(x_flat, y_flat, z_flat, color='red', marker='o', label='Original Data')
# 绘制插值后的曲面
ax.plot_surface(x_fine_grid, y_fine_grid, z_fine_grid, cmap='viridis', alpha=0.8, label='Interpolated Surface')

# 设置图例
#ax.legend()

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
import numpy as np
from scipy.interpolate import interp2d

x_values = np.array([6,	25.4,	50	,1000
])
y_values = np.array([0,
5,
10,
30,
])
z_values = np.array([
        [12	,10,	9,	8

],
        [20,	15,	10	,10

],
        [30	,20	,20,	20
],
        [40	,30,	30	,30
],

    ])
# 将输入数据转换成适合curve_fit的形式（需要是一维数组）
interp_func = interp2d(x_values, y_values, z_values, kind='linear')

# 现在你可以使用这个函数来插值任意的(x, y)点
# 例如，插值点(0.5, 0.5)
x_new = 12.7
y_new = 720
z_new = interp_func(x_new, y_new)
print(f"The interpolated value at ({x_new}, {y_new}) is {z_new}")
x_fine = np.linspace(x_values.min(), x_values.max(), 100)
y_fine = np.linspace(y_values.min(), y_values.max(), 100)
x_fine_grid, y_fine_grid = np.meshgrid(x_fine, y_fine)

# 使用插值函数计算细网格上的z值
z_fine_grid = interp_func(x_fine, y_fine)

# 创建一个3D图
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
x_grid, y_grid = np.meshgrid(x_values, y_values)

# 将网格展平以用于scatter函数
x_flat = x_grid.flatten()
y_flat = y_grid.flatten()
z_flat = z_values.flatten()
# 绘制原始数据点
#ax.scatter(x_values.flatten(), y_values.flatten(), z_values, color='red', marker='o', label='Original Data')
ax.scatter(x_flat, y_flat, z_flat, color='red', marker='o', label='Original Data')
# 绘制插值后的曲面
ax.plot_surface(x_fine_grid, y_fine_grid, z_fine_grid, cmap='viridis', alpha=0.8, label='Interpolated Surface')

# 设置图例
#ax.legend()

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
import numpy as np
from scipy.interpolate import interp2d

x_values = np.array([1,2,3	,5,7
])
y_values = np.array([20,
40,
80,
160,
])
z_values = np.array([
        [0.69	,0.8	,0.87	,0.98,	1.04


],
        [0.83,	0.93,	1	,1.09	,1.15


],
        [1	,1.12,	1.19	,1.27,	1.32

],
        [1.24,	1.38,	1.45,	1.53,	1.57

],

    ])
    # 将输入数据转换成适合curve_fit的形式（需要是一维数组）
interp_func = interp2d(x_values,y_values, z_values,kind='cubic')


# 现在你可以使用这个函数来插值任意的(x, y)点
# 例如，插值点(0.5, 0.5)
x_new = 12.7
y_new = 720
z_new = interp_func(x_new, y_new)
print(f"The interpolated value at ({x_new}, {y_new}) is {z_new}")
x_fine = np.linspace(x_values.min(), x_values.max(), 100)
y_fine = np.linspace(y_values.min(), y_values.max(), 100)
x_fine_grid, y_fine_grid = np.meshgrid(x_fine, y_fine)

# 使用插值函数计算细网格上的z值
z_fine_grid = interp_func(x_fine, y_fine)

# 创建一个3D图
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
x_grid, y_grid = np.meshgrid(x_values, y_values)

# 将网格展平以用于scatter函数
x_flat = x_grid.flatten()
y_flat = y_grid.flatten()
z_flat = z_values.flatten()
# 绘制原始数据点
#ax.scatter(x_values.flatten(), y_values.flatten(), z_values, color='red', marker='o', label='Original Data')
ax.scatter(x_flat, y_flat, z_flat, color='red', marker='o', label='Original Data')
# 绘制插值后的曲面
ax.plot_surface(x_fine_grid, y_fine_grid, z_fine_grid, cmap='viridis', alpha=0.8, label='Interpolated Surface')

# 设置图例
#ax.legend()

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()'''
from traits.api import Enum, HasTraits, List, Str, observe
from traitsui.api import Handler,EnumEditor,View,Item

# 假设这是一个用于获取螺纹数据的函数，返回螺纹类型列表
def 返回螺纹类型():
    return ['欧标', '美标']

# 假设这是一个根据螺纹类型获取螺纹大小的函数
def 读取螺纹大小(螺纹类型):
    if 螺纹类型 == '欧标':
        return ['M1', 'M2', 'M3']  # 示例数据，请替换为实际数据
    elif 螺纹类型 == '美标':
        return ['1', '1', '34']  # 示例数据，请替换为实际数据

class ThreadInfoHandler(Handler):
    cities = List(Str)

    def object_thread_type_changed(self, info):
        self.cities = 读取螺纹大小(info.object.thread_type)
        # As default value, use the first city in the list:
        info.object.thread_size = self.cities[0]

class ThreadInfo(HasTraits):
    thread_type = Enum(返回螺纹类型())
    thread_size = Str()



    traits_view =View(
    Item('thread_type', label='螺纹类型'),
    Item('thread_size', label='螺纹尺寸', editor=EnumEditor(name='handler.cities')))
# 创建一个示例对象并运行
if __name__ == "__main__":
    thread_info = ThreadInfo()
    thread_info.configure_traits(handler=ThreadInfoHandler())
