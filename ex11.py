# coding:utf8

print "How lod are u?",
age = raw_input()
print "What's your name?",
name = raw_input()


name += ""

print age, "<>", name

print "%s" % name



str = raw_input("raw_input:")
print str

# input() 接收的必须是一个表达式, 如果输入的字符串必须要用引号括起来 
# python3中input()默认为str类型
value = input("请输入一个表达式:")  
print value
