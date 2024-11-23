# -*- coding = utf-8 -*-
# @time:2024/1/26 13:45
# Author:lizhuang
# @File:pyd打包.py
# @Software:PyCharm
import os
import subprocess

# Python源文件
source_file = r'.\fn优化界面.py'

# 输出目录
output_dir = '.'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# Nuitka编译命令
# 注意：这里使用'--module'选项来创建一个共享库（.dll），而不是可执行文件
# 但是，这并不会直接创建一个.pyd文件
command = [
    'python -m nuitka '+
    ' --module '+source_file+' --include-plugin-directory='+'E:\mechanical-calculation-4\发布程序文件'+
    ' --run '
    # 如果需要，可以添加其他Nuitka选项，比如优化选项等
]
print(str(command[0]))
# 执行Nuitka编译
subprocess.run(str(command[0]))

# 在Windows上，你可能需要重命名生成的.dll文件为.pyd
# 或者使用其他工具（如Visual Studio的cl.exe编译器和.def文件）来创建.pyd文件
# 这里只是一个简化的示例，假设生成的.dll可以直接重命名为.pyd
'''if os.name == 'nt':  # 检查操作系统是否为Windows
    dll_file = os.path.join(output_dir, f'{os.path.splitext(source_file)[0]}.dll')
    pyd_file = os.path.join(output_dir, f'{os.path.splitext(source_file)[0]}.pyd')
    os.rename(dll_file, pyd_file)
    print(f"已重命名 {dll_file} 为 {pyd_file}")'''

print("编译完成。")