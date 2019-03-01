from models import User, Blog, Comment
from transwarp import db

db.create_engine(user='root', password='12345678', database='awesomej')

u = User(name='Test', email='text@example.com', password='1234567', image='about:blank')
u.insert()

print('new user id: %d' % u.id)

u1 = User.find_first('where email=?', 'test@example.com')
print('1find first user name:%s' % u1.name)

u1.delete()

u2 = User.find_first('where email=?', 'test@example.com')
print('2find first user name:%s' % u2.name)
