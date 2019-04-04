from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.ingredient.models import ingredient
from application.ingredient.forms import IngredientForm

@app.route("/ingredient", methods=["GET"])
def ingredient_list():
    return render_template("ingredient/list.html", ingredient = ingredient.query.all())

@app.route("/ingredient/new")
@login_required
def ingredient_form():
    return render_template("ingredient/new.html", form = IngredientForm())

@app.route("/ingredient/", methods=["POST"])
@login_required
def ingredient_create():
    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredient/new.html", form=form)

    i = ingredient(form.name.data, form.recommendation.data)

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("recipe_index"))
    

   
