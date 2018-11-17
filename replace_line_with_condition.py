# coding:utf-8

import fileinput
from sys import argv

script, file_path, condition = argv
if condition.startswith('lottery') == False:
    print "condition 必须以lottery开头"
    exit(0)

condition = condition.replace("lottery", "")


# file = open("/Users/johnson/Desktop/project.pbxproj", "r+")
# value = file.read()
#
# print ""
# print value
# print ""


# while True:
#     line = file.readline()
#     print  line
#
#     if not line:
#         break


line_num = 0
value = ""
for line in fileinput.input(file_path):
    line_num += 1
    print  line_num, line
    if condition in line:
        value += ""
    else:
        value += line



file = open(file_path, 'w')
file.write(value)
file.close()







