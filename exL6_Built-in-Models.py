
# coding:utf-8
from collections import  namedtuple

# 给tuple起个别名, 并为每一个值也起一个别名  用法有点c的struct
Rect = namedtuple('CGRect', ['x', 'y', 'width', 'height'])
r = Rect(1, 2, 333, 333)
print r.x, r.width
print Rect




from  collections import deque
q = deque(['1', '2', '2', '2', '2', '2', '2', '2', '2'])
q.append('xxxx')
q.appendleft('..')
print q
# 默认移除最后一个元素
q.remove('2')
q.remove('1')
print(q)
q.pop()
print(q)
del q[0]
print(q)


from collections import defaultdict
d = {'a': 11, 'xx': 'ww'}
print d['xsx']

x
