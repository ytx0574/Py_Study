# coding:utf-8

from sys import  argv
import os


amount_of_cheese = 10
amount_of_crackers = 50

def printTwoArgvs(one, two):
    print one, two
    one = 333
    two = 999
    # 此处值得更改没有意义, 作用域在函数内.
    amount_of_cheese = 100
    print one, two, amount_of_cheese


def printStarArgvs(*args):
    one, two, three = args
    print  one, two, three, "printStarArgs"





printTwoArgvs(11111, 22222)
# printTwoArgs(1111,111,111)
print printStarArgvs(22, 33, 44)
printTwoArgvs(amount_of_cheese, amount_of_crackers)
print amount_of_cheese

number = 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888\
      *\
      888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888\
      *\
      888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888\
      * \
      888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888 \
      * \
      888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888


print  str(number), type(number), type(str(number))



print  argv
script_path, file_path = argv

file = open(file_path, 'r')
print  file.tell()
print file.seek(10, os.SEEK_CUR)
print file.read(10)
print file.seek(10, os.SEEK_CUR)
print file.read(10)


def functionyx(a, b, c):
    print a, b, c

    return a, b, c, "eeee"

valuetuple = functionyx(11, 22, 444)
valuelist = [1, 2, 3]
print type(valuetuple), valuetuple[0]
print type(valuelist), valuelist[0]
