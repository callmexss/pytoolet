'''
File:          process_from_clipboard.py
File Created:  Saturday, 8th December 2018 12:05:09 pm
Author:        xss (callmexss@126.com)
Description:   Process text from clipboard and send it
               back.
-----
Last Modified: Saturday, 8th December 2018 12:06:57 pm
Modified By:   xss (callmexss@126.com)
-----
'''

# -*- coding: utf-8 -*-

import re
import time
from pprint import pprint

import clipboard


class Processor(object):
    """Process the given text."""

    def __init__(self, text):
        self.text = text
        self.remove_list = [Processor.process]
        self.function_list = []

        self.re_dict = {
            'hanzi': r'[\u4e00-\u9fa5]',
            '2bytes chars': r'[^\x00-\xff]'
        }

    def _get_function_list(self):
        li = [
            y for x, y in Processor.__dict__.items()
            if not x.startswith('_') and y not in self.remove_list
        ]
        return sorted(li, key=lambda f: f.__name__)

    def _print_info(self):
        print('Functions List'.center(79))
        for n, func in enumerate(self._get_function_list(), 1):
            self.function_list.append(func)
            name = func.__name__
            doc = func.__doc__
            # wid = (79 - len(name) - len(doc)) // 2
            print(n, name.ljust(35, '.'), doc.rjust(40, '.'))

    def _input_valid(self, tasks):
        """Whether the input is valid"""
        if not tasks:
            print('Empty input.')
            return False

        test_li1 = [i.isdigit()
                    for i in tasks]  # Whether they are numeric input.
        if not all(test_li1):
            print("Invalid input. Input must be integer.")
            return False

        test_li2 = [0 < int(i) <= len(self.function_list)
                    for i in tasks]  # Whether they are in valid range.
        if not all(test_li2):
            print("Input out of range! It should be in {} - {}".format(
                1, len(self.function_list)))
            return False

        return True

    def process(self):
        self._print_info()
        tasks = input("Your choice(seperate by space): ")
        res = []
        if not self._input_valid(tasks):
            return '\n'.join(res)
        for task in list(map(int, tasks.split(' '))):
            res.append(self.function_list[task - 1](self))
        return '\n'.join(res)

    def extract_phone_number(self, end='\n'):
        """Extract phone numbers from given text."""
        res = []
        phone_regex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?                # area code
            (\s|-|\.)?                        # separator
            (\d{3})                           # first 3 digits
            (\s|-|\.)                         # separator
            (\d{4})                           # last 4 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
            )''', re.VERBOSE)
        match = phone_regex.findall(self.text)
        for groups in match:
            # print(groups)
            phone_number = groups[0]
            res.append(phone_number)
        return end.join(res)

    def extract_email(self, end='\n'):
        """Extract Email from given text."""
        res = []
        email_regex = re.compile(r'''(
            ([0-9a-zA-Z]+)                    # username
            @                                 # @ symbol
            ([0-9a-zA-Z]+)                    # domain name
            (\.[a-zA-Z]{2,4})                 # dot something
            )''', re.VERBOSE)
        match = email_regex.findall(self.text)
        for groups in match:
            email_address = groups[0]
            res.append(email_address)
        return end.join(res)

    def format_BBC(self, end='\n'):
        """Format BBC news, the headlines."""
        pc = re.compile(r'\w+' + self.re_dict['2bytes chars'] + r'\s?' + self.re_dict['2bytes chars'] + r'+[^\s]+')
        pe = re.compile(r'[a-zA-Z0-9\']+\s+.*\.')
        chinese = pc.findall(self.text)
        english = pe.findall(self.text)
        chinese = [x + '。\n' for x in chinese]
        final = [x + '\n' + y for x, y in zip(english, chinese)]
        return end.join(final)


if __name__ == '__main__':
    text = clipboard.paste()
    # pprint(Processor.__dict__)
    processor = Processor(text)
    text = processor.process()
    clipboard.copy(text)
    print("Finished!")
    time.sleep(3)
