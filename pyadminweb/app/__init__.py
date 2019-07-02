from flask import Flask,render_template,send_from_directory,redirect,url_for,flash,request,json
from flask_sqlalchemy import SQLAlchemy
from app import views
from app.mod_user import forms
from app.mod_org import forms
#page navigation,所有有导航的模块,都必须在这里引入一下,否则没法注册app.route()



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

@app.route('/savecommodity', methods=['POST'])
@login_required
def save_commodity():

    commodity = Commodity()
    commodity.location = request.form["location"]
    commodity.person = request.form["person"]
    commodity.tel = request.form["tel"]
    commodity.desc = request.form["desc"]
    commodity.event_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    commodity.event_name = request.form["eventname"]

    if(not request.form["recordid"]=='None'):
        commodity.id = int(request.form["recordid"])
    else:
        commodity.id = 0

    c.insert_data(commodity)

    return redirect('/commoditylist')

