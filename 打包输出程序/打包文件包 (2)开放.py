# -*- coding = utf-8 -*-
# @time:2023/6/15 10:53
# Author:lizhuang
# @File:打包文件包.py
# @Software:PyCharm
import os
import shutil
import python_minifier
import shutil
import os
import shutil
import subprocess
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
def move_files_from_dist(dist_folder, subfolder_path):
    """
    Moves files from the dist folder to the specified subfolder, overwriting any existing files.
    """
    # 确保目标文件夹存在
    os.makedirs(subfolder_path, exist_ok=True)

    # 遍历dist文件夹中的所有文件和子文件夹
    for item in os.listdir(dist_folder):
        source = os.path.join(dist_folder, item)
        destination = os.path.join(subfolder_path, item)

        # 检查是否是文件
        if os.path.isfile(source):
            # 如果目标文件已存在，则替换它
            if os.path.exists(destination):
                os.remove(destination)
                # 移动文件
            shutil.move(source, destination)
            # 如果是文件夹，则递归处理
        elif os.path.isdir(source):
            # 递归调用自身来处理子文件夹
            move_files_from_dist(source, destination)
            # 删除空的源子文件夹
            if not os.listdir(source):
                os.rmdir(source)


def process_subfolder(subfolder_path):
    try:
        # 切换到子文件夹
        os.chdir(subfolder_path)
        command1 = ["pipreqs","./" ,"--use-local", "--encoding=utf-8"]  # "-e","360",
        subprocess.run(command1, check=True)
        # 执行 pyarmor 命令
        command = ["pyarmor", "gen", "-O","dist","-r", "."]#"-e","360",
        subprocess.run(command, check=True)
        print(f"Processed: {subfolder_path}")

        # 删除目标文件夹下除了dist以外的所有文件和文件夹
        # delete_files_except_dist(subfolder_path)

        # 移动dist文件夹中的内容到目标目录
        dist_folder = os.path.join(subfolder_path, "dist")
        move_files_from_dist(dist_folder, subfolder_path)

        # 如果需要，也可以删除dist文件夹（根据需求选择是否保留）
        shutil.rmtree(dist_folder)

    except subprocess.CalledProcessError as e:
        print(f"Error processing {subfolder_path}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {subfolder_path}: {e}")


def 执行转码(main_folder):
    # 遍历主文件夹下的第一层子文件夹
    for dir_name in os.listdir(main_folder):
        subfolder_path = os.path.join(main_folder, dir_name)
        # 检查是否是文件夹
        if os.path.isdir(subfolder_path):
            # 对每个子文件夹执行操作
            print(subfolder_path)
            process_subfolder(subfolder_path)

    print("All subfolders in the first level have been processed.")

def delete_directory(path):
    """删除指定路径的文件夹及其所有内容"""
    try:
        shutil.rmtree(path)
        print(f"文件夹 {path} 及其所有内容已被删除!")
    except OSError as e:
        print(f"删除文件夹 {path} 时出错: {e.strerror}")
    return
# 使用函数

def minify_python_files(source_dir: str, target_dir: str):
    未处理列表=[]
    print('开始混淆')
    for root, _, files in os.walk(source_dir):
        if '__pycache__' not in root:
            # 过滤 pyc 文件
            for file in files:
                source_file_path = os.path.join(root, file)
                target_root = root.replace(source_dir, target_dir, 1)
                if not os.path.exists(target_root):
                    os.makedirs(target_root)
                target_file_path = os.path.join(target_root, file)
                if file.endswith('.py') and file not in ['swcommands.py', ]:
                    with open(source_file_path, 'r',encoding='utf-8') as rf:
                            未处理列表.append(file)
                            shutil.copy(source_file_path, target_file_path)
                            print('未处理',file,'文件已移动')
                            continue
                    with open(target_file_path, 'w',encoding='utf-8') as wf:
                            未处理列表.append(file)
                            shutil.copy(source_file_path, target_file_path)
                            print('未处理', file, '文件已移动')
                            continue
                    print('已处理',file)
                else:
                    shutil.copy(source_file_path, target_file_path)
    print('未处理列表已复制',未处理列表)
    return
def 生成pyc(路径=r'E:\mechanical-calculation-4\发布程序文件'):
    print('开始生成pyc')
    import os
    import compileall
    compileall.compile_dir((路径), force=True, legacy=True)
    for root, dirs, files in os.walk(路径):
        for file in files:
            if file.endswith('.py'):
                os.remove(os.path.join(root, file))
    print('Compilationcomplete')
    return
import os
import pyautogui
import time
import subprocess

    # 设置要处理的文件夹路径
def pdf处理 (folder_path):

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
if __name__ == '__main__':
  print('开始打包')
  源码路径=r'E:\mechanical-design-program-4-master'
  发布路径 = r'E:\开放程序'  # 替换为你要删除的目录的路径
  delete_directory(发布路径)
  minify_python_files(源码路径,发布路径)
  pdf处理(r'E:\开放程序\数据文件')
  #执行转码(发布路径)
  #生成pyc(路径=发布路径)