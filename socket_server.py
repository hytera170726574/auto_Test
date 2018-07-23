import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",9999))
print("Bind UDP on 9999...")
while True:
    data,addr=sock.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    sock.sendto(b'Hello, %s!' % data, addr)
