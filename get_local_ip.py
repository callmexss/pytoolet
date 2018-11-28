'''
File:          get_my_local_ip.py
File Created:  Saturday, 14th October 2017 3:14:40 pm
Author:        xss (callmexss@126.com)
Description:   Get private IP address.
-----
Last Modified: Wednesday, 28th November 2018 4:24:04 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import socket
import clipboard

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)

clipboard.copy(myaddr)
