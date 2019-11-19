'''
File:          auto_download_pic.py
File Created:  Monday, 11th November 2019 8:55:01 pm
Author:        xss (callmexss@126.com)
Description:   download pictures when copy address.
-----
Last Modified: Monday, 11th November 2019 9:00:11 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import time
import os

import requests
import clipboard


pic_fmt = [".jpg", ".jpeg", ".gif", ".png"]
doc_fmt = [".doc", ".txt", ".pdf"]
old = ""
new = clipboard.paste()


def process(new, fmts, ftype):
    for fmt in fmts:
        if fmt in new or fmt.upper() in new:
            # print(new[:new.index(fmt)] + fmt)
            new = new[:new.index(fmt)] + fmt
            os.system(f"proxychains4 "
                      f"wget -P /mnt/c/Users/Public/{ftype} {new}")
            break


if __name__ == "__main__":
    try:
        while True:
            new = clipboard.paste()
            if old == new:
                continue
                time.sleep(0.2)
            else:
                process(new, pic_fmt, "Pictures")
                process(new, doc_fmt, "Documents")
                old = new
    except KeyboardInterrupt:
        print("exit")
