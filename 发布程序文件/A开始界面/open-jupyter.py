# -*- coding = utf-8 -*-
# @time:2024/10/16 8:15
# Author:lizhuang
# @File:ceshi.py.py
# @Software:PyCharm
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class JupyterLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jupyter Notebook Launcher")

        # 设定窗口大小
        self.root.geometry("400x250")

        # 创建一个变量以存储所选目录的路径
        self.directory_path = tk.StringVar()

        # 构建并放置选择目录的按钮
        self.select_dir_button = ttk.Button(root, text="选择工作目录", command=self.select_directory)
        self.select_dir_button.pack(pady=10)

        # 构建并放置显示所选目录路径的输入框
        self.directory_entry = ttk.Entry(root, textvariable=self.directory_path, state="readonly", width=50)
        self.directory_entry.pack(pady=10)

        # 构建并放置运行Jupyter的按钮
        self.run_button = ttk.Button(root, text="在选择目录下启动Jupyter Notebook", command=self.run_jupyter)
        self.run_button.pack(pady=10)
        # 构建并放置运行Jupyter的按钮
        self.run_button1 = ttk.Button(root, text="启动spyder", command=self.run_spyder)
        self.run_button1.pack(pady=10)
        self.run_button2 = ttk.Button(root, text="启动awespykit", command=self.run_awespykit)
        self.run_button2.pack(pady=10)
                # 构建并放置选择目录的按钮
        #self.select_dir_button0 = ttk.Button(root, text="第一次安装环境", command=self.anzhuanghuanjing)
        #self.select_dir_button0.pack(pady=10)

        # 为窗口添加一些额外的空间以提升视觉效果
        self.root.pack_propagate(False)
        self.root.resizable(False, False)

    def select_directory(self):
        """弹出目录选择对话框并存储用户选择的目录。"""
        directory = filedialog.askdirectory()
        if directory:
            self.directory_path.set(directory)

    def run_jupyter(self):
        """在所选目录中运行Jupyter Notebook。"""
        directory = self.directory_path.get()
        if directory:
            try:
                # 通过subprocess模块在所选目录下启动Jupyter Notebook
                subprocess.Popen(['jupyter', 'notebook', '--notebook-dir', directory])
                messagebox.showinfo("操作成功", f"Jupyter Notebook已在以下位置启动: {directory}")
            except Exception as e:
                messagebox.showerror("发生错误", f"无法启动Jupyter Notebook: {e}")
        else:
            messagebox.showwarning("警告", "未选择任何目录！")

    def run_spyder(self):
        try:
            # 通过subprocess模块在所选目录下启动Jupyter Notebook
            subprocess.Popen(['spyder'])
            messagebox.showinfo("操作成功",f"spyder已在以下位置启动")
        except Exception as e:
            messagebox.showerror("发生错误", f"无法启动spyder,需要安装: {e}")
    def run_awespykit(self):
        try:
            # 通过subprocess模块在所选目录下启动Jupyter Notebook
            subprocess.Popen(['rpk'])
            messagebox.showinfo("操作成功",f"awespykit已在以下位置启动")
        except Exception as e:
            messagebox.showerror("发生错误", f"无法启动awespykit,需要安装: {e}")
    def anzhuanghuanjing(self):
        try:
            # 通过subprocess模块在所选目录下启动Jupyter Notebook
            subprocess.Popen(['./miniconda安装包共享路径38.bat'])
            messagebox.showinfo("操作成功",f"awespykit已在以下位置启动")
        except Exception as e:
            messagebox.showerror("发生错误", f"无法启动awespykit,需要安装: {e}")
# 创建Tkinter主窗口并传递至应用类
root = tk.Tk()
app = JupyterLauncherApp(root)

# 启动Tkinter事件循环
root.mainloop()
