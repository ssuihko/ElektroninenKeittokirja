from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    recipes = db.relationship("Recipes", backref='account', lazy=True)
    
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    role = db.relationship("Role")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name






