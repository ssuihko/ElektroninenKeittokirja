from application import db, app
from sqlalchemy.sql import text
from application.recipes import models
from application.models import Base, recipeingredient

class Ingredient(Base):

    __tablename__ = "ingredient"

    ingredientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False, unique=True)

    # relationships
#    recipeingredient = db.relationship("Recipe", secondary=recipeingredient,
#                                        backref=db.backref('ingredients', lazy='dynamic'))

    def __init__(self, name ):
        self.name = name
     
    @staticmethod
    def ingredientWithRecipes():
        stmt = text("SELECT ingredient.ingredientid, COUNT(recipe_ingredient.recipeid) FROM ingredient"
                    " LEFT JOIN recipe_ingredient ON ingredient.ingredientid = recipe_ingredient.ingredientid"
                    " WHERE recipe_ingredient.recipeid IS NOT NULL"
                    " GROUP BY ingredient.ingredientid;")
        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"id":row[0], "count":row[1]})
        
        return ids


        


   
