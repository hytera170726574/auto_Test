import socket
import time
import datetime
while True:
    ipname=socket.getfqdn(socket.gethostname())
    myadd=str(socket.gethostbyname_ex(ipname))
    t=str(time.localtime(time.time()))
    a=t+myadd+"\n"
    file_handle = open('1.txt', mode='a')
    file_handle.write(a)
    time.sleep(1)
    file_handle.close()
    print a