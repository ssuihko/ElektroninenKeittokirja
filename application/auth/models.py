from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
   
    role_id = db.Column(db.Integer, db.ForeignKey('role.roleid'), nullable=True)
    
     #relationships
    recipes = db.relationship("Recipe", backref='account', lazy='dynamic')

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

    def role(self):
        return self.role_id


class Role(Base):

    roleid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @staticmethod
    def whatismyrole(accountId):
        stmt = text("SELECT name FROM role LEFT JOIN user ON user.role_id = role.roleid"
                " WHERE user.id = :accountid").params(accountid=current_user.get_id) 

        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"id": row[0], "name": row[1]})

    @staticmethod
    def ingredientWithRecipes():
        stmt = text("SELECT user., COUNT(recipe_ingredient.recipeid) FROM ingredient"
                    " LEFT JOIN recipe_ingredient ON ingredient.ingredientid = recipe_ingredient.ingredientid"
                    " WHERE recipe_ingredient.recipeid IS NOT NULL"
                    " GROUP BY ingredient.ingredientid;")
        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"id":row[0], "count":row[1]})
        
        return ids



