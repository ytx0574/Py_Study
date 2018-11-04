# coding:utf-8

from sys import argv
# script, filename = argv

# text = open(filename)
# print text.read()

path = raw_input("请输入你的文件地址:")
print path
txt = open(path)
print txt.read()
