# coding:utf-8

from types import MethodType

class Student(object):
    # __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    name = 'xxx'
    hello = 'Student_hello'


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name, age, sex):
        self.name = name;
        self.age = age
        self.sex = sex

    def printInfo(self):
        print('name = ' + self.hello)



s = Student("java", 22, 1)

print(s.name)
print(Student.name)
s.printInfo()


Student.name = "x'x"
print(Student.name)

def set_nickname(self, nickname):
    self.nickname = nickname

# 动态给实例绑定属性
s.set_nickname = MethodType(set_nickname, s)
s.set_nickname('xjj')
print s.nickname


# 给类绑定属性, 类和实例都可以使用
Student.nickname = set_nickname
s.nickname = 'xxxx'
print s.nickname

Student.nickname = "____"
print Student.nickname
print dir(s)



class Person(object):

    # __slots__ = ('name', 'nickname')
    # def __init__(self, name, nickname):
    #     pass

    _nickname = ''
    _name = ''

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        self._nickname = nickname


    @property
    def name(self):
        return self._name

    def name(self, aaa, bbb):
        return self._name + aaa + bbb


p = Person()
p.nickname
p.nickname = 'xiao xx'

p.name
print p.name("aaa", 'xxx')
