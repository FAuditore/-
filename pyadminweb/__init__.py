# page navigation,所有有导航的模块,都必须在这里引入一下,否则没法注册app.route()
from app import views
from app.mod_user import forms,models,controller
from app.mod_org import forms,models,controller
from app.mod_commodity import forms,models,blockchain,blockchain_node,controller,controllers
from app.mod_user import controller,forms,models

