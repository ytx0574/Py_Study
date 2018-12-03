# coding:utf=8
# 分布式进程

import time, sys, Queue
from  multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 由于QueueManager是从网络上获取的Queue, 所以注册时之提供名字
QueueManager.register('get_task_queue')
QueueManager.register('result_task_queue')

# 连接到服务器, 也就是运行taskmanager.py的服务器
server_addr = '127.0.0.1'
print('connect to server %s...' % server_addr)

# 端口和验证码和服务端必须保持一致
m = QueueManager(address=(server_addr, 5000), authkey='abc')
# 连接服务器
m.connect()

# 获取Queue对象
task = m.get_task_queue()
result = m.result_task_queue()

# 从task获取任务, 并从把结果写入result队列
for i in range(5):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n , n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')

# 处理结束
print('worker exit.')
