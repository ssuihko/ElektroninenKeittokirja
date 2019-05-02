from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SearchForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2,max=60,message="Name must be between 2-60 characters long")])

    class Meta:
        csrf = False

class IngredientEditForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=2,max=60,message="Name must be between 2-60 characters long")])
    amount = StringField("Amount: ", [validators.Length(min=2, message="Recommendation must be at least 2 characters long")])
     
    class Meta:
        csrf = False

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name ", [validators.Length(min=2, message="name must be at least 2 characters long")])
    amount = StringField("Amount ", [validators.Length(min=2, message="amount must be at least 2 characters long")])
    recipe_id = IntegerField()
    
    class Meta:
        csrf = False


