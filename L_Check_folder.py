# coding:utf-8

import os
from os.path import join, getsize


path = '/Users/johnson/Desktop/KKCP.xcassets'

def getdirsize(dir):
    size = 0L
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size




filesize = getdirsize(path)
print 'There are %f' % (filesize)
