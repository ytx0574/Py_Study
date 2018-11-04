from sys import argv
script, user_name = argv
separator = '|>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "i'd like to ask you a few questions?"
print "Do you like me %s?" % user_name
likes = raw_input(separator)

print '''
Alright, so you said %r about liking me.
you live in %r
''' % (separator, likes)
