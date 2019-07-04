from app.mod_commodity.models import Commodity
from app import db


def get_all_data():
    return Commodity.query.all()


def select_by_id(id):
    return Commodity.query.filter_by(id=id).first()
