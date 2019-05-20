'''
File:          auto_kill_vs.py
File Created:  Wednesday, 4th April 2018 4:25:41 pm
Author:        xss (callmexss@126.com)
Description:   Auto kill the visual studio progress
-----
Last Modified: Wednesday, 28th November 2018 4:59:51 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import psutil
import os
import time

# information = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'devenv' in p.info['name']]
# print(information)

while ([
        p.info for p in psutil.process_iter(attrs=['pid', 'name'])
        if 'devenv' in p.info['name']
]):
    os.system(f"taskkill /F /im devenv.exe")

time.sleep(3)