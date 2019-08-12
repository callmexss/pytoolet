'''
File:          add_star_at_begin.py
File Created:  Friday, 7th December 2018 7:49:25 pm
Author:        xss (callmexss@126.com)
Description:   An simple exercise add star at each
               line's beginning.
-----
Last Modified: Friday, 7th December 2018 7:53:59 pm
Modified By:   xss (callmexss@126.com)
-----
TODO: Make this one more useful? For markdown use?
-----
'''

import clipboard


def handle(t):
    clipboard.copy('\n'.join(['* ' + l for l in t.split('\n')]))


if __name__ == '__main__':
    text = clipboard.paste()
    handle(text)
