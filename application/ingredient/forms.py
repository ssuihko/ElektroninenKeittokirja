from flask_wtf import FlaskForm
from wtforms import StringField, validators

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=2)])
    recommendation = StringField("Recommendation", [validators.Length(min=2)])

    class Meta:
        csrf = False
