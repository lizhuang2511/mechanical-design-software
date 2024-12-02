# -*- coding = utf-8 -*-

# @time:2024/11/23 13:56
# Author:lizhuang
# @File:pdf处理.py
# @Software:PyCharm
import os
import pyautogui
import time
import subprocess

# 设置要处理的文件夹路径
folder_path = './'

# 获取文件夹下的所有 PDF 文件
pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

# 循环处理每个 PDF 文件
for pdf_file in pdf_files:
    # 构建完整的文件路径
    full_file_path = os.path.join(folder_path, pdf_file)

    # 使用系统默认程序打开 PDF 文件
    subprocess.run(['start', full_file_path], shell=True)

    # 等待几秒钟，确保 PDF 文件已打开
    time.sleep(3)

    # 执行 Ctrl+Shift+S（另存为）命令
    pyautogui.hotkey('ctrl', 'shift', 's')

    # 等待另存为对话框出现
    time.sleep(1)

    # 执行 Enter 命令（这里假设另存为对话框已经聚焦并且默认路径是可接受的）
    pyautogui.press('enter')

    # 执行左移命令（这里假设你需要移动到某个特定的位置，比如文件名输入框）
    # 注意：左移的次数和速度可能需要根据你的具体情况进行调整
    pyautogui.press(['left'])
    time.sleep(1)
    # 再次执行 Enter 命令（这里假设你已经完成了所有必要的输入）
    pyautogui.press('enter')

    # 等待几秒钟，确保文件已保存并关闭
    time.sleep(1)

# 注意：这个脚本有很多假设和硬编码的延迟，它可能不会在你的环境中按预期工作。
# 你可能需要根据你使用的 PDF 阅读器、操作系统和屏幕分辨率进行调整。