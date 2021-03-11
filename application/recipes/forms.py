from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, DateTimeField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, message="name must be at least 2 characters long")])
    method = TextAreaField("Method", [validators.Length(min=2, message="method must be at least 2 characters long")])
    ingredients = SelectMultipleField('Ingredients', coerce=int, render_kw={"class": "chosen-select"})
    
    class Meta:
        csrf = False

class RecipeEditForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
    method = TextAreaField("Method", [validators.Length(min=2, message="method must be at least 2 - 64 characters long")])
    ingredients = SelectMultipleField('ingredients', coerce=int, render_kw={"class": "chosen-select"})
    createdon = DateTimeField("Created on", render_kw={"readonly class": "form-control"})
    modifiedon = DateTimeField("Modified on", render_kw={"readonly class": "form-control"})
    
    class Meta:
        csrf = False

