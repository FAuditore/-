from app import app
from flask_login import login_required
from flask import render_template,request,redirect
from app.mod_commodity.models import Commodity
import app.mod_commodity.controllers as c


#导航页面里的href上使用 <a class="" href="{{ url_for('list_all_commodities') }}"> 或  href="/commoditylist"都可以路由到这里
@app.route('/commoditylist')
@login_required
def list_all_commodities():
    commodity = c.get_all_data()
    return render_template("commodity/commoditylist.html",commoditylist= commodity)

@app.route('/editcommodity/<int:id>')
@login_required
def edit_commodity(id):
    commodity = Commodity()
    if(id != 0):
        commodity = c.select_by_id(id)
    print(commodity.__dict__)
    return render_template("commodity/commodityform.html",selectcommodity= commodity)

