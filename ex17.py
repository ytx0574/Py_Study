from sys import argv
from os.path import exists
from shutil import  copyfile

script, from_path, to_path = argv
print "from_file: %s, to_file: %s" % (from_path, to_path)

# from_file = file(from_path, 'r')
# from_data = from_file.read()
#
#
#
# print "from_data length:%r" % len(from_data)
# print "from_path is exist?: %r, to_path is exits?: %r" % (exists(from_path), exists(to_path))
# to_file = file(to_path, 'w')
# to_file.write(from_data)
#
# from_file.close()
# to_file.close()


# file(to_path, 'w').write( file(from_path, 'r').read() )

# 直接copy文件
# copyfile(from_path, to_path)

