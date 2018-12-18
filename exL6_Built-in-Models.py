
# coding:utf-8
from collections import  namedtuple

# 给tuple起个别名, 并为每一个值也起一个别名  用法有点c的struct
Rect = namedtuple('CGRect', ['x', 'y', 'width', 'height'])
r = Rect(1, 2, 333, 333)
print r.x, r.width
print Rect



# 解决插入和删除慢得问题, queue实现的高效插入和删除/双向列表
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

# 为不存在的key添加默认实现
from collections import defaultdict
d = {'11': 11, '2': 'ww'}
d['3'] = '3'
d['121'] = '121'
d['9'] = '9'
print d

dd = defaultdict(lambda: None)
print dd['a']

# 为dict添加顺序.  按key的插入删除排序, 不是按照key的值排序
from collections import OrderedDict
orderDict = OrderedDict(d)
orderDict['z'] = 'zz'
orderDict['x'] = 'xx'
orderDict['y'] = 'yy'
print orderDict


# 计数器, 统计字符出现次数
from collections import Counter
c = Counter()
for ch in 'programing':
    c[ch] = c[ch] + 1

print c



# 常规的摘要算法
import hashlib
md5 = hashlib.md5()

md5.update('123456')
print md5.hexdigest()

sha512 = hashlib.sha512()
sha512.update('123456')
print sha512.hexdigest()


# 常规的几种迭代器
import itertools
# 无限迭代器, n每次+1
natuals = itertools.count(99990)
for n in natuals:
    print n
    if n > 100000:
        break

# 无限迭代字符串中的每一个字符  参数必须为一个迭代器对象
cycle = itertools.cycle('johnson')
for n in cycle:
    print n
    if n == 's':
        break

# 自定义重复次数
repeat = itertools.repeat(222, 111)
for n in repeat:
    print n;

# 串联对象, 并进行迭代. 非无限
chain = itertools.chain('123', 'abc')
for n in chain:
    print n

# 把 相邻 的重复元素挑粗来
group = itertools.groupby('11f2ss2llll222332..ffiifjlsjfiwx')
for key, value in group:
    print(key, list(value))


# 惰性计算, 类似lambda, 迭代时才进行计算
# 后面 10 * 10,  20 * 11, 30 * 12

for n in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(10))
    print(n)
# 同上, imap后面必须给两个参数, 并且以长度短的作为计算结果
la = lambda x, y: x * y
for n in itertools.imap(la, [10, 20, 30, 11], [111, 222, 333, 221, 212, 666]):
    print n

