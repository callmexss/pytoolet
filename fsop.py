'''
File:          fsop.py
File Created:  Saturday, 18th May 2019 10:33:38 am
Author:        xss (callmexss@126.com)
Description:   File system operations.
-----
Last Modified: Saturday, 18th May 2019 10:34:03 am
Modified By:   xss (callmexss@126.com)
-----
'''

import os
import re
import hashlib
import shutil
import functools
import inspect

import pysnooper

# I may define some file types here, like pictures, videos file format
PICTURES = ['jpg', 'jpeg', 'png', 'svg', 'bmp', 'gif']


def find_all_files(path='.', absolute=False, recursively=False):
    """Find all files in given path
    
    Keyword Arguments:
        path {str} -- path to find (default: {'.'})
        absolute {bool} -- absolute or not (default: {False})
        recursively {bool} -- recursively find or not (default: {False})
    
    Returns:
        list -- list of all files in given path
    """
    if not recursively:
        return os.listdir(path)
    else:
        all_files = []

        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if not absolute:
                    all_files.append(file_path)
                else:
                    all_files.append(os.path.abspath(file_path))

        return all_files 


def find_files_by_type(path, file_type, absolute=False, recursively=False):
    """Find files by type
    
    Arguments:
        type {list} -- a list of file types.
    
    Keyword Arguments:
        absolute {bool} -- absolute path or not (default: {False})

    Returns:
        list -- a list of files matches given type.
    """
    ret = []
    all_files = find_all_files(recursively=recursively)
    for file in all_files:
        extname = os.path.splitext(file)[-1]
        if extname in file_type:
            ret.append(file)
    return ret


def find_files_by_pattern(pattern):
    pass


def find_files_by_size(size):
    pass