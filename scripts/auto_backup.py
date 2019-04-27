#!/usr/bin/python3
'''
File:          auto_backup.py
File Created:  Friday, 14th December 2018 11:20:50 am
Author:        xss (callmexss@126.com)
Description:   Automatically backup my files.
-----
Last Modified: Friday, 14th December 2018 11:20:56 am
Modified By:   xss (callmexss@126.com)
-----
'''

import os
import platform
import zipfile
import time

from apscheduler.schedulers.blocking import BlockingScheduler

config_filename = 'data/auto_backup_conf.privd'  # This should be default

if platform.system().lower() == 'windows':
    backup_dir = r'd:/Backup/auto_backup'
elif platform.system().lower() == 'linux':
    backup_dir = r'/backup/auto_backup'
if not os.path.isdir(backup_dir):
    os.makedirs(backup_dir)


def check_priv_config():
    # create a new one if not exists
    if not os.path.exists(config_filename):
        with open(config_filename, 'w') as f:
            f.write('# one path per line')

    # clean the duplicated paths
    with open(config_filename, 'r') as f:
        lines = f.readlines()
        comment = lines[0]
        paths = [x.strip() for x in lines if os.path.exists(x.strip())]

    with open(config_filename, 'w') as f:
        f.write('\n'.join([comment] + list(set(paths))))


def get_all_target_path():
    with open(config_filename, 'r') as f:
        lines = f.readlines()
        return [x.strip() for x in lines if os.path.exists(x.strip())]


def backup(target):
    """Backup all the files in target directory to a zip file.

    Arguments:
        target {str} -- Directory to be backed up.

    TODO:
        Make the logic more easily to understand.
    """

    directory = os.path.split(target)[1]
    backup_path = os.path.abspath(os.path.join(backup_dir, directory))
    print('Auto backup {} -> {}'.format(target, backup_path))
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)

    basename = os.path.basename(backup_path)
    if ' ' in basename:
        #  Eliminate the space in folder name.
        basename = '_'.join(basename.split(' '))

    time_str = '_'.join(list(map(str, time.localtime()[:6])))
    zip_filename = basename + '_' + time_str + '.zip'
    zip_filepath = os.path.abspath(os.path.join(backup_path, zip_filename))

    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
        files_path = []
        for root, _, files in os.walk(target):
            for file in files:
                files_path.append(os.path.join(root, file))
        for each in files_path:
            print('Compress file {}...'.format(each))
            zip_file.write(each,
                           each[each.find(os.path.basename(backup_path)):])


def auto_backup():
    target_path_list = get_all_target_path()
    # print(target_path_list)
    for each in target_path_list:
        try:
            backup(each)
        except Exception as err:
            print(err)
            continue
    print('Done!')


def start():
    check_priv_config()
    auto_backup()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(start, 'cron', hour=8)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

