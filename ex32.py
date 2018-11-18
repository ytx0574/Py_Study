# coding:utf-8

import  ex5

list = []
tuple = ()
for i in range(0, 11):
    list.append(str(i))
    # tuple += (i * i,)

print  ""
print len(list)

while len(list) < 22:
    list.append("VVV")



# print  list, tuple
#
# if 6 > 11:
#     print  "xxxx"
# elif:
#     print  "xxxx"
# else:
#     print  "xxxx"


value = 2222

def changeValue():
    global value
    value = 999


print value
changeValue()
print value

CAONIMA = 888
global CAONIMA
print  CAONIMA


s = lambda y: y ** y

print s(3)

g = lambda x, y:  (x * y * 100) + 1

print g(2, 2)




try:
    fh = open('/Users/johnson/Desktop/MM.TXT', 'r')
    fh.write("000000")
except IOError, TypeError:
    print "IO Error"
else:
    print "no thing"
    fh.close()


fh = open('/Users/johnson/Desktop/MMM.TXT', 'r')
try:
    fh.write("MMMMMMMMM")
except IOError, (argument, argument1):

    print "IO Error", argument, argument1
finally:
    print "no thing"
    fh.close()
def exceptionFunc():
    if False:
        raise RuntimeError("我抛出异常")
    else:
        raise Exception("error", 1)

try:
    exceptionFunc()
except TypeError, (arg):
    print "xxx", arg
except Exception, value:
    print value

else:
    pass



