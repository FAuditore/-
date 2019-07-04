from app import app
from flask_login import login_required
from flask import render_template
import app.mod_user.controllers as c


#导航页面里的href上使用 <a class="" href="{{ url_for('list_all_users') }}"> 或  href="/userlist"都可以路由到这里
@app.route('/userlist')
@login_required
def list_all_users():
    user = c.get_all_user()
    return render_template("user/userlist.html",userlist= user)


@app.route('/edituser/<int:id>')
@login_required
def edit_user(id):
    selectuser = c.select_by_id(id)
    print(selectuser)
    return render_template("user/userform.html",selectuser= selectuser)
