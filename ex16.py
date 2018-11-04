# coding:utf-8
from sys import argv

script, filename = argv

# print 'path=%r' % filename
# print 'If you don\'t want to that, hit CTRL-C'

# target = open(filename, 'w') 
# print target
# # print target.read()

# # target.truncate()

# line1 = raw_input("line1:")
# line2 = raw_input("line2:")
# line3 = raw_input("line3:")
# target.write(line1 + "\n")
# target.write(line2 + '\n')
# target.write(line3)
# target.close()

# # print target.read()




# target1 = open(filename, 'a')
# target1.write(raw_input("add line"))
# target1.write(raw_input("add line"))
# # print target1.read()
# target1.close()

# print open(filename, 'r').read()


# target3 = open(filename, 'r+')
# print "\n\n\ntarget3 read\n" + target3.read()
# target3.write("KK")
# target3.write(raw_input(">>>>"))
# target3.close()


target4 = open(filename, 'rb')
# 一行一行的读取, 从第一行开始, 不填参数默认读取整行. 参数大于一行则读取一行, 如果上一次该行未读完, 下一次接着读
print "readline:" + target4.readline(3)
print "readline:" + target4.readline(10)
print "readline:" + target4.readline(111)
print "readline:" + target4.readline(3)
print len(target4.readline(9))
print "readline:" + target4.readline(10)

#  第一个参数偏移量, 第二个参数起始位置:(0文件头, 1当前位置, 2文件尾)
print target4.seek(6, 0)  
#此处循环从第3个字符开始, 前面readline已经读取了一部分了
for line in target4: print "8" + line




