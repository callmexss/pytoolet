'''
File:          auto_backup.py
File Created:  Saturday, 16th September 2017 5:54:36 pm
Author:        xss (callmexss@126.com)
Description:   Automatically backup my files.
-----
Last Modified: Friday, 14th December 2018 11:48:40 am
Modified By:   xss (callmexss@126.com)
-----
'''
# -*- coding: utf-8 -*-

import os
import datetime
import time
import zipfile
from shutil import copytree, rmtree, make_archive  # 用于递归拷贝、删除、压缩文件夹

root_dir = r"D:\Backup\\"


def backup(src, dst):
    time_info = time.localtime()
    # print(time_info)

    name_list = [str(elem) for elem in time_info[:-3]]
    # print(name_list)

    target_name = dst + '-'.join(name_list) + '.backup'

    copytree(src, target_name)

    # adddirfile(temp_file)

    os.chdir(r'D:\Backup\Document')
    # make_archive('-'.join(name_list), 'zip', target_name)
    # rmtree(target_name)

    cwd = os.getcwd()
    print(cwd)

    rm_dirs = os.listdir()[:-7]
    print(rm_dirs)

    print(len(rm_dirs))
    for _ in rm_dirs:
        tag = cwd + '\\' + _
        rmtree(tag)
    rm_dirs = os.listdir()[:-7]
    print(len(rm_dirs))


def freenet_backup():
    src = r"C:\Users\xaut\Documents\Yu Writer Libraries\Freenet"
    dst = r"D:\Backup\Freenet\\"
    backup(src, dst)


def network_backup():
    src = r"C:\Users\xaut\Documents\Yu Writer Libraries\Network"
    dst = r"D:\Backup\Network\\"
    os.chdir(root_dir)
    # cur_dir = os.getcwd()
    dir_list = os.listdir()
    print(dir_list)
    if 'Network' not in dir_list:
        os.mkdir("Network")
        backup(src, dst)
        return
    backup(src, dst)


def yw_lib_backup():
    src = r'C:\Users\xaut\Documents\Yu Writer Libraries'
    dst = r'D:\Backup\Document\\'
    if not os.path.isdir(dst):
        os.mkdir(dst)
    backup(src, dst)


def adddirfile(dir_path):
    pass


def hexo_blog_backup():
    src = r'D:\Code\hexo\blog\source'
    dst = r'D:\Backup\Blog\\'
    if not os.path.isdir(dst):
        os.mkdir(dst)
    backup(src, dst)


if __name__ == "__main__":
    yw_lib_backup()
    hexo_blog_backup()
    input("备份已完成，按任意键退出...")
