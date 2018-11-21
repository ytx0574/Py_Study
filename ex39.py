
# coding:utf-8

class AA(object):
    def foo(self):
        print "%s" % self


    @classmethod
    def class_foo(cls):
        print("%s" % cls)



    @staticmethod
    def static_foo(value):
        print("%s" % value)


a = AA()
a.foo()
a.class_foo()
a.static_foo(11)

print a.foo
print a.class_foo
print(a.static_foo)