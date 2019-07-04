from app.mod_user.models import User


def get_all_user():
    return User.query.all()


def select_by_id(id):
    return User.query.filter_by(id=id).first()
