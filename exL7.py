import time

def customer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('customer   %s' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    print(type(c))
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('producing %s...' % n)
        r = c.send(n)
        print('customer return %s' % r)
    c.close()

if __name__ == '__main__':
    c = customer()
    produce(c)