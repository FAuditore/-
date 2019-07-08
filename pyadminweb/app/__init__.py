from flask import Flask,render_template,send_from_directory,redirect,url_for,flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,login_required,login_manager
class User(UserMixin):
    users = {'user@user.com': {'password': '123'},
             'admin@123.com':{'password':'123'}}
# 创建一个flask实例
app = Flask(__name__)

# 引入config.py文件
app.config.from_object('config')

# 创建一个 SQLAlchemy对象实例.
db = SQLAlchemy(app)

user_login={}

@app.route('/')
def index():
    return render_template("login.html")


@app.route('/index.html')
@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']
    if email in User.users and request.form['password'] == User.users[email]['password']:
        user = User()
        user.id = email
        print('登录成功')
        login_user(user)
        next = request.args.get('next')
        db.session.add(user)
        return redirect(url_for('/index'))

    return render_template("error_auth.html")




from app import views


from app.mod_commodity.blockchain_node import Blockchain

# 商品链链表
chain_list=[]