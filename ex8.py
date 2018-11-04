formatter = "%r %r %r %r %s"

print formatter % (1, 2, 3, 4, "66")
print formatter % ("one", "two", "three", "four", "99")

print formatter % (formatter, formatter, formatter, formatter, formatter)


formatter1 = "%r %r %r" % ("fde", 99, "666")
print formatter1


print '''
kljfklsdjlfjdsljfljfljslfjdsljflsj
fdfjlkjlf
fjsdljflkdsjlfj
fdjslfjl
'''

str = """fdsfkjskljfdls
fdjjjlfjds
fjsdljflkdsj%rlfjfjksdlj
jlf%3ds

fdjslfjljlfsd
""" % (999, 8), "..."
print str[1]