# Py_Study


global 标记全局变量, 可在函数内部修改值.  不同其他语言, global声明必须是已经声明过的变量.(在你需要修改值得地方进行声明)

exec 直接把字符串当做pyton的代码执行

with-as 快速处理异常, 类似try: finally:的操作  with所求值得对象必须有__enter__()和__exit(self, type, value, trace)__函数.  用法上面有点类似swift中的 if let 声明


is 与==同理

lambda 匿名函数. 类似代码块  如 get_sum = lambda x, y, z: x + y + z

pass 空语句, 用于保持程序的完整性, 占位


try: except ExceptionType, ExceptionType: else:
try: except ExceptionType, Argument: else:
try: finally:

with 变量的别名
yield  一个带有yield的函数就是一个generator.  调用的时候看起像个函数调用, 其实是生成一个generator对象, 而普通的函数调用则是返回它的返回值.
当对其使用for循环的时候, 其实内部调用为next(). 当执行到yield时, 就会被中断, 返回迭代值. yield可以让一个函数拥有迭代器的能力, 因为自动保留上一次的值, 所以资源上消耗不大

from  inspect import  isgeneratorfunction
isgeneratorfunction(fab) 通过该函数判断是否为generator

import types
isinstance(fab, Iterable) 判断是否为类的实例

@staticmethod @classmethod instance method.  如果有名称一样的同样的函数, 优先级依次为static class instance.
intance默认第一个参数为self, class默认第一个参数为cls. 外部定义的函数为mudule_method.


print [i * 10 for i in range(10)]  生成的是list
print (i * 10 for i in range(10))  生成的是可next()的generator

map 映射. 可更改每一个元素, 并返回相同的数据结构
reduce 用于所有元素参与计算
sorted 排序.
filter 筛选.

print reduce(lambda x, y: x * y + 10, map(lambda x: int(x), ["1", "32", "2", "3", "11"]))
print sorted(["fdsf", '2222', '323232', '1', '3232'], key=len, reverse=True)


f1, f2, f3 = count()  类似这种写法, 后面必须是一个生成器.


@log
def now()
    print date

def log()
    print 'log'
Decorator 装饰器.  一个函数执行前, 执行另一个函数.  类似AspecBefore操作


int2 = functools.partial(int, base=2)
int2("3333") 输出3333的二进制数值
functools 偏函数, 在原有函数的基础上参数默认值.




python 每一个py文件都是一个module, 如果有两个一样的module就为其添加包名.
包名为一个文件夹, 里面必须包含一个__init__.py的文件, 否则系统会认为这不是一个包而且一个文件夹.  包名不要和系统函数冲突

https://docs.python.org/2.7/library/functions.html
python2.7所有的内置函数:  自己创建函数的时候, 不要和系统的冲突. 否则无法使用系统函数;

Built-in Functions
abs()	divmod()	input()	open()	staticmethod()
all()	enumerate()	int()	ord()	str()
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
bool()	filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reversed()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()
delattr()	help()	next()	setattr()
dict()	hex()	object()	slice()
dir()	id()	oct()	sorted()



__name__ 特殊变量函数(双下划线开头) 如果改module从其他地方导入, __name__ != "__main__"
_private 私有变量函数(单下划线开头). 规范上定义, 但是还是可以访问到的
没有下划线(public变量/函数).
