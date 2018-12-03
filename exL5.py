# -*- coding: utf-8 -*

import json


f = open('/Users/Johnson/Desktop/exL5.txt', 'a')
d = {'name': 'dadada', 'age': 12, 'sex': '1'}
print(d)

# 直接得到json字符串
json_str = json.dumps(d)
print(json_str)
# 直接把json字符串写入文件. 第二个参数为filelike-Object
json.dump(d, f)

# 从json字符串转为dict对象
d1 = json.loads(json_str)
print d1, d1['sex']



class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex



def instance_convert_dict(s):
    print 's.dict', s.__dict__

    return {'name': s.name, 'age': s.age, 'sex': s.sex}

s = Student('jj', 22, True)
# 对象转为json字符串
print json.dumps(s, default=instance_convert_dict)
print json.dumps(s, default=lambda obj: obj.__dict__)


def dict_convert_instance(d):
    return Student(d['name'], d['age'], d['sex'])


# json字符串转为对象
s1 = json.loads(json_str, object_hook=dict_convert_instance)
print s1.name, s1.age




