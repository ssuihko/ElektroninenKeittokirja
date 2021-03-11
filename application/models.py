from application import db

class Base(db.Model):

    __abstract__ = True

    createdOn = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedOn = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate = db.func.current_timestamp())

recipeingredient = db.Table('recipe_ingredient',
                            db.Column('recipeId', db.Integer, 
                            db.ForeignKey('recipe.recipeId')),
                            db.Column('ingredientId', db.Integer, 
                            db.ForeignKey('ingredient.ingredientId')))