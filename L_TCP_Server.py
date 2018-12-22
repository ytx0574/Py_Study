# coding:utf-8
import socket
import threading
import time


def tcplink(sock, addr):
    sock.send('Welcome connected...')
    while True:
        data = sock.recv(1024)
        print('接收到客户端的消息 %s' % data)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello  %s' % data)
    sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
# 当前等待连接数量
s.listen(5)
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



