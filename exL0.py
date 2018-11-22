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

int16 = functools.partial(int, base=16)

print(int16("110"))