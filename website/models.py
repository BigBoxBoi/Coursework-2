from . import db
from flask_login import UserMixin



class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10,2))
    carbon_footprint = db.Column(db.Numeric(10,2))
    #user_reviews = db.relationship('user_reviews')


class User_accounts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))
    #user_reviews = db.relationship('user_reviews')



##class User_reviews(db.Model, UserMixin):
#    id = db.Column(db.Integer, primary_key=True)
 #   user_id = db.Column(db.Integer, db.ForeignKey('User_accounts.user_id'))
  #  product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'))
  #  rating = db.Column(db.Integer)
  #  comment = db.Column(db.Text)
  #  created_at = db.Column(db.DateTime(timezone=True), default=func.now())##


