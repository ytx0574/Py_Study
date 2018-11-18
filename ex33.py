
from  inspect import  isgeneratorfunction

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print a, b
        a, b = b, a + b
        n = n + 1

print(fab(11))


def fab1(max):
    n, a, b = 0, 0, 1

    list = []
    while n < max:
        list.append(b)
        a, b = b, a + b
        n = n + 1

    return list

print(fab1(11))

def func0():
    pass





print(func0())


for i in range(5):
    print i
for i in xrange(5):
    print i


print  range(10)
print  xrange(10)


class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


for n in Fab(5):
    print n


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


print(fab(5))
print(fab1(5))
for n in fab(5):
    print(n)

f = fab(5)
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()


print(isgeneratorfunction(fab))
print(isgeneratorfunction(fab1))



def read_file(fpath):
    read_size = 10
    with open(fpath, 'r') as f:
        while True:
            value = f.read(read_size)
            if value:
                yield value
            else:
                return


for value in read_file(__file__):
    print(value)