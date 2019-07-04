from app import db

class Org(db.Model):
    # 表的名字:,或者derived from the class name converted to lowercase and with “CamelCase” converted to “camel_case
    __tablename__ = 'sys_user'
    #colums
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.String(80), unique=False, nullable=True)
    isactive = db.Column(db.String(20), unique=False, nullable=True)
    created = db.Column(db.DateTime, nullable=False)

def __repr__(self):
    return '<Org %r>' % self.name

