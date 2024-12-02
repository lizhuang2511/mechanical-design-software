# -*- coding = utf-8 -*-
# @time:2024/10/16 13:57
# Author:lizhuang
# @File:生成依赖代码.py
# @Software:PyCharm
import os
import hashlib
import subprocess
import pipreqs
def process_subfolder(subfolder_path):
    try:
        # 切换到子文件夹
        os.chdir(subfolder_path)
        command1 = ["pipreqs","./" ,"--use-local","--force","--encoding=utf-8","--mode=no-pin",]  # "-e","360",
        subprocess.run(command1, check=True)
        # 执行 pyarmor 命令
        command = ["pyarmor", "gen", "-O","dist","-r", "."]#"-e","360",
        #subprocess.run(command, check=True)
        print(f"Processed: {subfolder_path}")
        # 删除目标文件夹下除了dist以外的所有文件和文件夹
        # delete_files_except_dist(subfolder_path)
        # 移动dist文件夹中的内容到目标目录
    except subprocess.CalledProcessError as e:
        print(f"Error processing {subfolder_path}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {subfolder_path}: {e}")
def 执行转码(main_folder):
    # 遍历主文件夹下的第一层子文件夹
    for dir_name in os.listdir(main_folder):
        print(dir_name)
        if dir_name=='打包输出程序':
            continue
        else:
            subfolder_path = os.path.join(main_folder, dir_name)
            # 检查是否是文件夹
            if os.path.isdir(subfolder_path):
                # 对每个子文件夹执行操作
                print(subfolder_path)
                process_subfolder(subfolder_path)
def get_requirements_files(root_dir):
    """
    递归查找所有文件夹和子文件夹中的requirements.txt文件。
    """

    requirements_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if 'requirements.txt' in filenames:
            requirements_files.append(os.path.join(dirpath, 'requirements.txt'))
    return requirements_files


def read_requirements(file_path):
    """
    读取requirements.txt文件内容。
    """
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def write_requirements(file_path, requirements):
    """
    将去重后的requirements写入文件。
    """
    with open(file_path, 'w') as file:
        for req in requirements:
            file.write(req + '\n')


def hash_requirement(requirement):
    """
    使用哈希函数来为requirements生成唯一的标识，以便去重。
    这里简单使用requirement字符串的hash值。
    """
    return hashlib.md5(requirement.encode('utf-8')).hexdigest()


def merge_requirements(files):
    """
    合并多个requirements.txt文件，并去除重复项。
    """
    unique_requirements = set()
    seen_hashes = set()

    for file_path in files:
        requirements = read_requirements(file_path)
        for req in requirements:
            req_hash = hash_requirement(req)
            if req_hash not in seen_hashes:
                unique_requirements.add(req)
                seen_hashes.add(req_hash)

    return sorted(unique_requirements)


def main(root_dir, output_file):
    执行转码(root_dir)
    requirements_files = get_requirements_files(root_dir)
    merged_requirements = merge_requirements(requirements_files)
    write_requirements(output_file, merged_requirements)


if __name__ == "__main__":
    # 指定根目录和输出文件路径
    root_directory = r'E:\机械设计软件\mechanical-design-program-4-master'
    output_file_path = r'E:\机械设计软件\mechanical-design-program-4-master\requirements.txt'
    main(root_directory, output_file_path)
    print(f"Merged requirements have been written to {output_file_path}")