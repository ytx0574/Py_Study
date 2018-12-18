# coding:utf-8
import socket
import time
import psutil

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

i = 0
ps = psutil.Process()

while True:
    time.sleep(1)
    i += 1
    info = '>>> %d %s %s %s---%s %s' % (i, ps.status(), ps.name(), ps.exe(), ps.pid, ps.ppid())

    s.send(info)
    print('发送到服务端      %s' % info)

    data = s.recv(1024)
    print('输出接收到服务端的消息 %s' % data)
s.close()

