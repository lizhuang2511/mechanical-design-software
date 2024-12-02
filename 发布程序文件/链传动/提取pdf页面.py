import fitz  # pymupdf

import fitz  # 加载PyMuPDF工具包


def getCover(fileName, outputPrefix, pageNumber):
    # 打开PDF文件
    with fitz.open(fileName) as doc:
        # 根据页码加载页面（注意：页码通常从0开始）
        page = doc.load_page(pageNumber - 1)  # 如果页码从1开始，则减1以转换为索引

        # 将页面渲染为图像（pixmap）
        pixmap = page.get_pixmap(colorspace='rgb', dpi=300)

        # 构建唯一的输出文件名，例如：output_1.png, output_2.png, ...
        outputFileName = f"{outputPrefix}_{pageNumber}.png"

        # 保存图像为PNG格式
        pixmap.save(outputFileName)

        #doc.close()



    # 提取第2页和第3页（注意页码是从1开始的，但在代码中要用0基索引）
'''getCover(r'D:\工作文件\机械设计\机械设计手册 (第五版) 第2卷 机械零部件设计(连接、紧固与传动)阎邦椿主编带书签.pdf',
                  r'D:\工作文件\机械设计\花键计算\图.png')'''
import numpy as np
开始页面=375
结束页面=380
页码=np.linspace(开始页面,结束页面,(结束页面-开始页面+1))
print(页码)
for i in range(len(页码)):
    getCover(r'D:\工作文件\机械设计\机械设计手册 (第五版) 第2卷 机械零部件设计(连接、紧固与传动)阎邦椿主编带书签.pdf',
             r'D:\工作文件\机械设计\花键计算\图',int(页码[i]))
import os
import fitz  # PyMuPDF

import os
import fitz  # PyMuPDF

import os
import fitz  # PyMuPDF

import os
import fitz  # PyMuPDF

def images_to_pdf(input_folder, output_pdf):
    doc = fitz.open()  # 创建一个新的PDF文档对象

    # 遍历指定文件夹下的所有PNG图片
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(input_folder, filename)
            img = fitz.open(image_path)  # 打开每张图片
            rect = img[0].rect  # 获取图片尺寸
            page = doc.new_page(width=rect.width, height=rect.height)  # 创建新的页面
            pix = fitz.Pixmap(image_path)  # 获取图片的pixmap
            page.insert_image(rect, pixmap=pix)  # 将图片插入页面
            pix = None  # 释放pixmap资源

    # 保存文档
    doc.save(output_pdf)
    doc.close()

# 示例用法
input_folder = r'D:\工作文件\机械设计\花键计算' # 指定文件夹路径
output_pdf =r'D:\工作文件\机械设计\output.pdf'  # 输出PDF文件名

images_to_pdf(input_folder, output_pdf)


