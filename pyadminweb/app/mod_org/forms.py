from app import app
from flask_login import login_required
from flask import render_template
import app.mod_org.controllers as c


# 导航页面里的href上使用 <a class="" href="{{ url_for('list_all_users') }}"> 或  href="/userlist"都可以路由到这里
@app.route('/orglist')
@login_required
def list_all_orgs():
    o = c.get_all_org()
    return render_template("user/orglist.html",userlist= org)


@app.route('/editorg/<int:id>')
@login_required
def edit_org(id):
    selectuser = c.select_by_id(id)
    print(selectuser)
    return render_template("org/orgform.html",selectuser=selectuser)
