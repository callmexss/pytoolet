'''
File:          get_global_ip.py
File Created:  Wednesday, 28th November 2018 4:44:53 pm
Author:        xss (callmexss@126.com)
Description:   Get global IP address.
-----
Last Modified: Wednesday, 28th November 2018 4:45:21 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import requests
import clipboard

response = requests.get("http://ip-api.com/json")
print('your ip is {0}'.format(response.json()['query']))
clipboard.copy(response.json()['query'].split(' ')[-1])
