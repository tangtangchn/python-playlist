# encoding: utf-8

import os
import shutil

# 相对路径
# 当前路径
path = './'
files = os.listdir(path)

for f in files:
    # 文件夹名称为文件后缀名
    folder_name = f.split('.')[-1]
    # 判断文件夹是否存在
    if not os.path.exists(folder_name):
        # 创建文件夹
        os.makedirs('./' + folder_name)
        # 移动文件
        shutil.move(f, folder_name)
    else:
        shutil.move(f, folder_name)
