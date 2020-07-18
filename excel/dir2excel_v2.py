# -*- coding: utf-8 -*-

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# 版本：v2
# 用途：盘点整理文件夹资料，生成Excel清单
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


import os
import sys
import re
import xlwt
from datetime import datetime


# 存储所有文件路径
filepaths = []


# 遍历文件夹
def readdir(directory):
    # 当前目录路径，子目录，非目录子文件
    # topdown是代表要从上而下遍历还是从下往上遍历
    for dirPath, dirNames, fileNames in os.walk(directory, topdown=True):
        filepath = [dirPath, []]
        if len(fileNames) != 0:
            for fileName in fileNames:
                filepath[1].append(fileName)
                filepath[1].append('\n')
            print(filepath)
            filepaths.append(filepath)
        for dirName in dirNames:
            readdir(dirName)


# 处理Excel工作表
def dir2excel(rootdir):
    # 遍历目标文件夹
    readdir(rootdir)

    # 以'\'符号分割根文件夹的绝对路径
    rootdir = re.split(r'\\', rootdir)
    # 获取根文件夹名称
    rootname = rootdir[-1]

    # 新建一个Excel工作簿
    wb = xlwt.Workbook()
    # 新建一张Excel工作表
    ws = wb.add_sheet(rootname)

    # 写入Excel工作表
    # 工作表的行
    i = 0
    for filepath in filepaths:
        # 以'\'符号分割文件夹的绝对路径
        paths = re.split(r'\\', filepath[0])
        # 工作表的列
        j = 0
        for path in paths:
            ws.write(i, j, path)
            j += 1
        ws.write(i, j, filepath[1])
        i += 1

    # 命名并保存Excel工作簿
    wb.save(rootname + '_资料清单.xls')


def main(argv):
    if argv[1] is None:
        print('请提供一个文件夹路径 :)')
    else:
        # 开始时间
        starttime = datetime.now()
        dir2excel(argv[1])
        # 结束时间
        endtime = datetime.now()
        # 计算处理用时
        processtime = (endtime - starttime).seconds
        print('处理用时：' + str(processtime) + 's')
        print('资料清单生成成功 :)')


if __name__ == '__main__':
    main(sys.argv)
