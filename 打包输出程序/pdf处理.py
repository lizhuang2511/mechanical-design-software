# -*- coding = utf-8 -*-
# @time:2024/11/23 13:56
# Author:lizhuang
# @File:pdf处理.py
# @Software:PyCharm
import os
import fitz  # PyMuPDF


def copy_pdfs(src_folder, dest_folder):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

        # 遍历源文件夹中的所有文件
    for filename in os.listdir(src_folder):
        if filename.endswith('.pdf'):
            # 构建完整的文件路径
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)

            # 打开PDF文件
            doc = fitz.open(src_path)
            # 保存PDF文件到目标路径
            doc.save(dest_path)
            # 关闭文档
            # doc.close()
            print(f"Copied: {filename}")

        # 使用当前路径作为源和目标文件夹


current_path = os.getcwd()
source_folder = current_path
destination_folder = os.path.join(current_path, 'copied_pdfs')

copy_pdfs(source_folder, source_folder)
