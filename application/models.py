from application import db

class Base(db.Model):

    __abstract__ = True

    createdOn = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedOn = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate = db.func.current_timestamp())

recipeingredient = db.Table('recipe_ingredient',
                            db.Column('recipeid', db.Integer, 
                            db.ForeignKey('recipe.recipeid')),
                            db.Column('ingredientid', db.Integer, 
                            db.ForeignKey('ingredient.ingredientid')))