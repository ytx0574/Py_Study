# coding:utf-8



class HelloJ(object):
    pass


def fn(self, name='J'):
    print __name__ + name


# 动态的为HelloJ添加hello()函数, 并绑定到fn函数
HelloJ = type('HelloJ', (object, ), dict(hello=fn))

h = HelloJ()
h.hello('johnson')



# 动态的为类添加函数.  类似oc的category
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    # 指定使用ListMetaclass来定制类.  py3用法不一样
    __metaclass__ = ListMetaclass
    pass

class MyList1(list):
    pass

l = MyList()
l.append(333)
l.add(444)
print(l)

l1 = MyList1()
l1.append(2222)
print l1







# 简易的ORM实现

class Filed(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


class StringField(Filed):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(222)')

class IntegerField(Filed):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mapping = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Filed):
                mapping[k] = v
        for k in mapping.iterkeys():
            # 从字典移除
            attrs.pop(k)

        attrs['__table__'] = name
        attrs['__mapping__'] = mapping
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass
    
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Model has no attribute \'%s\'' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(str(self[k]))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args))
        print('SQL: %s' % sql)
        print('args: %s' % args)


class UserJ(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = UserJ(id = 11, name = 'Johnson', email = 'ytx0573@gmail.com', password = '88888')
u.save()


