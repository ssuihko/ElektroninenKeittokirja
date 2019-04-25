from application import db
from application.recipes import models
from sqlalchemy.sql import text

class ingredient(db.Model):

    __tablename__ = "ingredient"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.String(144), nullable=False)
  
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'),
                           nullable=False)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

   
