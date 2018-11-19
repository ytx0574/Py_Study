# coding:utf-8

print type(list)

# for生成器  只能被迭代一次, 第二次无法迭代
mygenerator = (x * 1000 for x in xrange(1))

for n in mygenerator:
    print  n

for n in mygenerator:
     print  "sss" + str(n)



print "print my_generator"
def my_generator():
    mylist = xrange(5)
    for x in mylist:
        yield x * 1


generator = my_generator()
for i in generator:
    print i

import  itertools
horses = [1, 2, 3, 4, 5]
# 获取horse内部所有可能的排列顺序
print itertools.permutations(horses)

list = list(itertools.permutations(horses))
print list, len(list)

print  2 ** 7






class Object(object):
    def __init__(self):
        self.aa = "aaaaa"

    def object_test(self):
        print("object_test")


    def class hello():






