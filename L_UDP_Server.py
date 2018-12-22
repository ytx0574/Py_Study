import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
print('UDP bind on 8888')
while True:
    dada, addr = s.recvfrom(1024)
    print('Received from %s: data:%s' % (dada, addr))
    s.sendto('--------------', addr)


