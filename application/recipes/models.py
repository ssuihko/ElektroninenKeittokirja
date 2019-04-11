from application import db
from application.ingredient import models
from application.auth import models
from sqlalchemy.sql import text

association_table = db.Table('recipeIngredient', 
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), nullable=False),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
)

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(130), nullable=False)
    method = db.Column(db.String(400), nullable=False)

    association_table = db.relationship('ingredient', secondary=association_table, backref=db.backref('ingredient', lazy='dynamic'))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)



    def __init__(self, name, method):
        self.name = name
        self.method = method


    @staticmethod
    def list_recipes():
        stmt = text("SELECT name FROM recipes")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            
            response.append({"name":row[0]})

        return response

    @staticmethod 
    def find_recipes_with_ingredient(id):
        stmt = text("SELECT DISTINCT recipes.id, recipes.name "
                    " FROM recipes, ingredient, recipe_ingredient WHERE ingredient.id = :param "
                    " AND ingredient.id = recipe_ingredient.ingredient_id "
                    " AND recipe_ingredient.recipe_id = recipes.id;").params(param=id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

    class recipe_ingredient(db.Model):
        recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'),
        primary_key=True)
        ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'),
        primary_key=True)

        recipe = db.relationship("Recipes", lazy=True)
        ingredient = db.relationship("ingredient", lazy=True)

        def __init__(self, recipe, ingredient):
            self.recipe_id = recipes.id
            self.ingredient_id = ingredient.id

        def __repr__(self):
            return '{} - {}'.format(self.recipe_id, self.ingredient_id)









