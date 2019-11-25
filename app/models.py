
from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<Product %r>' % self.name

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<Location %r>' % self.name
    