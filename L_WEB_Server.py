# coding:utf-8

# # 启动一个普通的网页服务
# from wsgiref.simple_server import make_server
#
# def application(envirom, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#
#     head = """
#     <head>
#         <style>
#             h1 {
#                 color: #333333;
#                 font-size: 48px;
#                 text-shadow: 3px 3px 3px #666666;
#             }
#         </style>
#     </head>
# """
#
#     return head + '<h1>hello<h1>'
#
# httpd = make_server('', 8008, application)
# httpd.serve_forever()


# 使用Flask创建一个表单服务
from flask import Flask
from flask import request

app = Flask(__name__)
# 主页
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>HELLO</h1>'
# 登录页
@app.route('/signin', methods=['GET'])
def sign_form():
    # 下面的action响应signin/post函数
    return '''
    <form action='/signin_commit' method='post'>    
    <p><input name="username"></p>
    <p><input name="age"></p>
    <p><input name="sex"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>
    '''
# 登录操作
@app.route('/signin_commit', methods=['POST'])
def signin():
    print(request.form)
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h1>hello, admin</h1>'
    return '<h1>username or password was wrong</h1>'

if __name__ == '__main__':
    app.run()