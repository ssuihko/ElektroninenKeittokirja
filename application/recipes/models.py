from application import db
from application.ingredient import models
from application.auth import models
from sqlalchemy.sql import text
from application.models import Base, recipeingredient

class Recipe(Base):

    __tablename__ = "recipe"

    recipeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(130), nullable=False)
    method = db.Column(db.Text, nullable=False)


    #relationships
    recipeingredient = db.relationship('Ingredient', secondary=recipeingredient,
        backref=db.backref('recipes', lazy='dynamic'))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, method, user):
        self.name = name
        self.method = method
        self.account_id = user

    @staticmethod 
    def user_count():
        stmt = text("SELECT COUNT(account.name) FROM account")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"amount":row[0] })

        return response

    #find_recipe_ingredients

    @staticmethod 
    def find_recipe_ingredients(idd):
        stmt = text("SELECT ingredient.ingredientId, ingredient.name FROM ingredient"
                    " INNER JOIN recipe_ingredient ON recipe_ingredient.ingredientId = ingredient.ingredientId"
                    " INNER JOIN recipe ON recipe_ingredient.recipeId = recipe.recipeId"
                    " WHERE recipe.recipeId = :idd").params(idd=idd) 

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            print('find_recipe_ingredients')
            print(row)
            response.append({"id":row[0],"name": row[1]})

        return response

    @staticmethod
    def find_recipes_with_no_ingredients():
        stmt = text("SELECT recipe.recipeId, recipe.name FROM recipe"
                    " LEFT JOIN recipe_ingredient ON recipe_ingredient.recipeId = recipe.recipeId"
                    " GROUP BY recipe.recipeId"
                    " HAVING COUNT(recipe_ingredient.ingredientId) = 0")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name": row[1]})
            
        return response












