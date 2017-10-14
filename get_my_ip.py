import socket
import clipboard

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)

clipboard.copy(myaddr)
