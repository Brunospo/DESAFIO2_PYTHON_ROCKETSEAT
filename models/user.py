from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(128), nullable=False)

# Relacionamento com ListaDeCompras
  meals = db.relationship('Meal', backref='users', lazy=True)