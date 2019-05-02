from application import db
from application.ingredient import models
from application.auth import models
from sqlalchemy.sql import text

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(130), nullable=False)
    method = db.Column(db.String(400), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)



    def __init__(self, name, method):
        self.name = name
        self.method = method


    @staticmethod 
    def find_users_with_recipes():
        stmt = text("SELECT account.id, account.name, COUNT(recipes.id) AS recipes FROM account"
                    " LEFT JOIN recipes ON recipes.account_id = account.id"
                    " WHERE recipes.account_id = account.id"
                    " GROUP BY account.id")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id":row[0],"name": row[1], "recipes": row[2]})

        return response

    @staticmethod
    def find_recipes_with_no_ingredients():
        stmt = text("SELECT recipes.id, recipes.name FROM recipes"
                    " LEFT JOIN recipe_ingredient ON recipe_ingredient.recipe_id = recipes.id"
                    " GROUP BY recipes.id"
                    " HAVING COUNT(recipe_ingredient.ingredient_id) = 0")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name": row[1]})
            
        return response












