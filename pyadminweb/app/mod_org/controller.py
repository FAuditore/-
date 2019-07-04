from app.mod_org.models import Org

def get_all_org():
    return Org.query.all()

def select_by_id(id):
    return Org.query.filter_by(id=id).first()

