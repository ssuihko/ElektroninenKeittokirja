from application import db
from application.ingredient.models import ingredient
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
        









