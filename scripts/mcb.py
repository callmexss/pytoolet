'''
File:          mcb.py
File Created:  Tuesday, 11th December 2018 3:07:00 pm
Author:        xss (callmexss@126.com)
Description:   A Python program to keep track of multiple
               pieces of text. (mcb for multiclipboard)
-----
Last Modified: Tuesday, 11th December 2018 3:07:14 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import os
import shelve
import clipboard


class Guardian(object):
    """Provide cryptography support."""
    pass


class Worker(object):
    """Do the routine."""

    def __init__(self):
        self.clipboard_dir = 'data'
        self.clipboard_name = 'mcb'

        if not os.path.isdir(self.clipboard_dir):
            os.mkdir(self.clipboard_dir)

        self.clipboard_path = os.path.join(self.clipboard_dir, self.clipboard_name)

    def show_contents(self):
        """Show what in the clipboard."""
        pass

    def copy(self):
        """Copy a piece of data to the system clipboard."""
        pass

    def add(self):
        """Add an item to the multiclipboard."""
        pass

    def delete(self):
        """Delete a piece of item from the multiclipboard."""
        pass
