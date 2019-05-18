'''
File:          fsop_test.py
File Created:  Saturday, 18th May 2019 3:30:13 pm
Author:        xss (callmexss@126.com)
Description:   unit test for fsop.py
-----
Last Modified: Saturday, 18th May 2019 3:30:17 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import unittest
import os

import fsop


class TestFsop(unittest.TestCase):
    def test_find_all_files(self):
        all_files = fsop.find_all_files(recursively=True)
        for file in all_files:
            self.assertTrue(os.path.exists(file))


python_files = ['*.py', '*.pyc']
print([x for x in fsop.find_specific_files(patterns=python_files)])
fsop.list_files_by(fsop.find_all_files())