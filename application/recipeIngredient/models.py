from application import db
from application.recipes.models import Recipes
from application.ingredient.models import ingredient
from sqlalchemy.sql import text


class recipe_ingredient(db.Model):
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'),
    primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'),
    primary_key=True)

    recipe = db.relationship("Recipes", lazy=True)
    ingredient = db.relationship("ingredient", lazy=True)

    def __init__(self, recipe_id, ingredient_id):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id

    def __repr__(self):
        return '{} - {}'.format(self.recipe_id, self.ingredient_id)