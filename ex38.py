# coding:utf-8

import ex34

class Thing(object):

    def __init__(self, aa):
        self.aa = aa

    def test(self):
        print("-------instance method")

    @classmethod
    def test(cls):
        print("-------class method")

    @staticmethod
    def test():
        print("-------static method")



    @classmethod
    def class_method(cls):
        print(cls)

    @staticmethod
    def static_method():
        print staticmethod


def module_method():
    print 'module_method'


a = Thing("11")
a.test()
Thing.test()
print "a.aa = %r" % a.aa
print  module_method

# 外部不能直接调用__init__函数, py的类每一个函数都必须要包含一个参数, 第一个为self.  类型oc的msgsend行数, 第一个必须为接收消息的对象
a1 = Thing.__init__(a, "9999")
print(a1)



print '-\n' * 11



value1 = ex34.Object()

print(value1, a)
print value1.aa
value1.object_test()
