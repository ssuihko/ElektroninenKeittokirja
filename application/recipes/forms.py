from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class RecipeEditForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
    method = TextAreaField("Method", [validators.Length(min=2, message="method must be at least 2 characters long")])
   
    class Meta:
        csrf = False

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, message="name must be at least 2 characters long")])
    method = TextAreaField("Method", [validators.Length(min=2, message="method must be at least 2 characters long")])

    class Meta:
        csrf = False

class RecipeIngreForm(FlaskForm):
    name = StringField("Recipe name" , [validators.Length(min=2, message="name must be at least 2 characters long")])

    class Meta:
        csrf = False




