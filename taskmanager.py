# coding:utf=8
# 分布式进程


import random, time, Queue

from  multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = Queue.Queue()
# 接收任务队列
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('result_task_queue', callable=lambda: result_queue)

# 绑定端口5000, 并设置验证码 (socket服务端开启监听)
manager = QueueManager(address=('', 5000), authkey='abc')
# 启动
manager.start()

# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.result_task_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('put task %d' % i)
    task.put(n)

# 从result队列读取结果
print('try get results...')
# 获取结果, 要么等到10次结果都获取到, 要么就超时关掉. 和上面放进去的任务
for i in range(10):
    r = result.get(timeout=111)
    print('result: %s' % r)

# 断开连接
manager.shutdown()

