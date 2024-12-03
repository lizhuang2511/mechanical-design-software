# -*- coding = utf-8 -*-
# @time:2024/12/3 10:30
# Author:lizhuang
# @File:去除空格.py
# @Software:PyCharm
import os


def remove_spaces_from_filenames(directory):
    # 遍历指定目录
    for filename in os.listdir(directory):
        # 获取旧的文件路径
        old_path = os.path.join(directory, filename)

        # 如果是文件而不是文件夹
        if os.path.isfile(old_path):
            # 去除文件名中的空格
            new_filename = filename.replace(" ", "")
            # 获取新的文件路径
            new_path = os.path.join(directory, new_filename)

            # 重命名文件
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} to {new_path}")


# 指定要处理的文件夹路径
directory_path = r"D:\程序文件\图书"

# 调用函数处理文件夹
remove_spaces_from_filenames(directory_path)
