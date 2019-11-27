import datetime
from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return self.product_name

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<Location %r>' % self.location_name

class ProductMovement(db.Model):
    __tablename__ = 'product_movement'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    from_location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable = True)
    to_location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable = True)
    product_id = db.Column(db.Integer,db.ForeignKey('products.id'))
    qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<ProductMovement %r>' % self.id

    