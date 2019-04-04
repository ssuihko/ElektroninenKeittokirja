from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.ingredient.models import ingredient
from application.ingredient.forms import IngredientForm

@app.route("/ingredient", methods=["GET"])
def ingredient_list():
    return render_template("ingredient/list.html", ingredient = Ingredient.query.all())
