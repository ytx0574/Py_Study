# coding:utf-8
from gevent import monkey;
monkey.patch_socket()
monkey.patch_ssl()

import os
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i

        # 让gevent交替运行
        gevent.sleep(0)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()


import urllib2
def ff(url):
    print('get url %s' % url)
    re = urllib2.urlopen(url)
    data = re.read()
    print('%d bytes received from %s' % (len(data), url))

    url = url.replace("https://", '')
    url = url.replace('/', '')

    path = os.path.dirname(__file__) + "/" + url + ".html"
    f = open(path, 'w')
    f.write(data)
    print path

gevent.joinall([
    gevent.spawn(ff, 'https://www.youtube.com/'),
    gevent.spawn(ff, 'https://www.jd.com/'),
    gevent.spawn(ff, 'https://github.com/')
])


