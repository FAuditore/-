from flask import Flask,render_template,send_from_directory,redirect,url_for,flash,request,json
from flask_sqlalchemy import SQLAlchemy

# 创建一个flask 实例
app = Flask(__name__)

# 引入config.py文件
app.config.from_object('config')

#创建一个 SQLAlchemy对象实例.
db = SQLAlchemy(app)

@app.route('/')
@app.route('/login.html')
@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'GET':
        return render_template("login.html")
