import socket,sys
import time
#import socket
'''sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",9999))
print("Bind UDP on 9999...")
while True:
    data,addr=sock.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    sock.sendto(b'Hello, %s!' % data, addr)'''



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host="10.110.15.135"
port=38000
s.bind(("10.110.15.136",38000))

try:
    s.settimeout(5)
    data=s.recvfrom(1024)
    print data
except socket.timeout as e:
    print "time_out"

