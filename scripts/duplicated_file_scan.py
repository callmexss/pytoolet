'''
File:          duplicate_file_scan.py
File Created:  Wednesday, 28th November 2018 8:37:29 pm
Author:        xss (callmexss@126.com)
Description:   Find all the specific duplicated files.
-----
Last Modified: Wednesday, 28th November 2018 8:41:44 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import os
import sys
from pprint import pprint

import fsop


class DuplicatedScaner:
    def __init__(self):
        self.hash_table = {}
        self.size_table = {}

    def scan(self):
        for root, _, files in os.walk(os.getcwd()):
            for f in files:
                filename = os.path.join(root, f)
                filesize = os.path.getsize(filename)
                if filesize not in self.size_table:
                    self.size_table[filesize] = []
                self.size_table[filesize].append(filename)

        for size, files in self.size_table.items():
            if len(files) > 1:
                for file in files:
                    self.hash_table[file] = fsop.calculate_file_md5(file)

    def report(self):
        pprint(sorted(self.hash_table.items(), key=lambda x: x[1]))


if __name__ == '__main__':
    # pprint(hash_table)
    scaner = DuplicatedScaner()
    scaner.scan()
    scaner.report()
