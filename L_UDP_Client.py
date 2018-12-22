import socket
import itertools
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in itertools.count(1):
    s.sendto(str(i), ('127.0.0.1', 8888))
    print(s.recv(1024))
    if i > 10:
        break

s.close()