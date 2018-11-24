import functools

# list
print [i * 10 for i in range(10)]
# generator
print (i * 10 for i in range(10))

print reduce(lambda x, y: x * y, map(lambda x: int(x), ["1", "2", "3", 4, "5"]))


print sorted(["fdsf", '2222', '323232', '1', '3232'], key=len, reverse=True)



a, b, c = (i for i in range(3))

print a, b, c


print( int("110", base=16) )

# 偏函数
int16 = functools.partial(int, base=16)

print(int16("110"))


# 获取对象所有的属性及函数
print(dir("xx"))
print "".__doc__
print("fdf,2 fjflj jfkljdsl fjslj flsj lfjdl flkaj fljl jflsj flsdjla ".split(' '))

# 获取是否包含某属性或函数
print(getattr('', 'lower'))
