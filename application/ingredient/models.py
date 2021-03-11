from application import db, app
from sqlalchemy.sql import text
from application.recipes import models
from application.models import Base, recipeingredient

class Ingredient(Base):

    __tablename__ = "ingredient"

    ingredientId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False, unique=True)

    # relationships
#    recipeingredient = db.relationship("Recipe", secondary=recipeingredient,
#                                        backref=db.backref('ingredients', lazy='dynamic'))

    def __init__(self, name ):
        self.name = name
     
    @staticmethod
    def ingredientWithRecipes():
        stmt = text("SELECT ingredient.ingredientId, COUNT(recipe_ingredient.recipeId) FROM ingredient"
                    " LEFT JOIN recipe_ingredient ON ingredient.ingredientId = recipe_ingredient.ingredientId"
                    " WHERE recipe_ingredient.recipeId IS NOT NULL"
                    " GROUP BY ingredient.ingredientId;")
        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"id":row[0], "count":row[1]})
        
        return ids


        


   
