# -*- coding: utf-8 -*-

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# 版本：v1
# 用途：盘点整理文件夹资料，生成Excel清单
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


import os
import sys
import xlwt


# 存储所有文件路径
filepaths = []


# 遍历文件夹
def readdir(directory):
    # 当前目录路径，子目录，非目录子文件
    for dirPath, dirNames, fileNames in os.walk(directory):
        for fileName in fileNames:
            filepath = os.path.join(dirPath, fileName)
            print(filepath)
            filepaths.append(filepath)
        for dirName in dirNames:
            readdir(dirName)


# 处理Excel工作表
def dir2excel(rootdir):
    # 新建一个Excel工作簿
    wb = xlwt.Workbook()
    # 新建一张Excel工作表
    ws = wb.add_sheet('资料清单')

    # 遍历目标文件夹
    readdir(rootdir)

    # 写入Excel工作表
    # 工作表的行
    i = 0
    for filepath in filepaths:
        ws.write(i, 0, filepath)
        i += 1

    # 命名并保存Excel工作簿
    wb.save('资料清单.xls')


def main(argv):
    if argv[1] is None:
        print('请提供一个文件夹路径 :)')
    else:
        dir2excel(argv[1])
        print('资料清单生成成功 :)')


if __name__ == '__main__':
    main(sys.argv)
