'''
File:          format_yu_writer_code.py
File Created:  Friday, 13th October 2017 2:35:09 pm
Author:        xss (callmexss@126.com)
Description:   Yu writer formater.
-----
Last Modified: Wednesday, 28th November 2018 4:36:35 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import clipboard
import time
import os

root_path = os.getcwd()

data_path = os.path.join(root_path, r'data/')
if not os.path.isdir(data_path):
    os.mkdir(data_path)

file_path = os.path.join(data_path, 'yu_code_format.txt')

os.system("notepad " + file_path)

lines = []

with open(file_path, "r") as f:
    lines = f.readlines()

s = ''.join(lines)

res = s.replace('\t', '    ').replace('\n\n', '\n')
clipboard.copy(res)

with open(file_path, "w+") as f:
    lines = f.write('')
