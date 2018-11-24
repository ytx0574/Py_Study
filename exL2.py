# coding:utf-8

from enum import Enum
from numpy import unique


Month = Enum('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',)

WEEK = Enum('Monday', 'Thursday', '星期三', '星期四', 'Friday', 'Satday', 'Sunday', '334', '33')


print(Month.Jan)
print WEEK.Monday

print(type(Month.Jan))
print(WEEK.Thursday)


for name in WEEK:
    print(name)
    print(type(name))


print( '星期四' in WEEK)
