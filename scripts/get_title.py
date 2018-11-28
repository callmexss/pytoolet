'''
File:          get_title.py
File Created:  Wednesday, 28th November 2018 5:07:41 pm
Author:        xss (callmexss@126.com)
Description:   Get title format string.
-----
Last Modified: Wednesday, 28th November 2018 5:07:52 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import clipboard

s = input("input the title: ")
clipboard.copy(s.title())