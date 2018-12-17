'''
File:          lucky.py
File Created:  Monday, 17th December 2018 3:39:11 pm
Author:        xss (callmexss@126.com)
Description:   Google lucky search.
-----
Last Modified: Monday, 17th December 2018 3:39:21 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import requests
import bs4
import sys
import webbrowser

print('Googling...')  # display text while downloading the Google page
res = requests.get(
    'http://google.com/search?q=' + ' '.join(sys.argv[1:]),
    proxies={'http': 'socks5://127.0.0.1:1080'}
    )
res.raise_for_status()

# webbrowser.open("google.com")
