from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.ingredient.models import ingredient
from application.ingredient.forms import IngredientForm, IngredientEditForm
from application.recipes.models import Recipes

@app.route("/ingredient", methods=["GET"])
def ingredient_list():
    return render_template("ingredient/list.html", ingredient=ingredient.query.all())

@app.route("/ingredient/new")
@login_required
def ingredient_form():
    return render_template("ingredient/new.html", form=IngredientForm())

@app.route("/ingredient/new/", methods=["POST"])
@login_required
def ingredient_create(recipe_id):

    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredient/new.html", form=form)

    ingredient = ingredient(form.name.data, form.amount.data)
    ingredient.id = form.id.data

    this_recipe = Recipes.query.get(recipe_id)
   
    this_recipe.association_table.append(ingredient.id)

    db.session().add(ingredient)
    db.session().add(this_recipe)
    db.session().commit()

    return redirect(url_for("ingredient_list"))

@app.route("/ingredient/<ingredient_id>/edit/", methods=["GET", "POST"])
@login_required
def ingredient_update(ingredient_id):

    if request.method == "GET":

        ingredient = ingredient.query.get(ingredient_id)
        form = ingredientEditForm(obj=ingredient)

        return render_template("ingredient/update.html", form=form, ingredient_id=ingredient_id)

    form = IngredientEditForm(request.form)
    ingredient = ingredient.query.get(ingredient_id)

    if not form.validate():
        return render_template("ingredient/update.html", form=form, ingredient_id=ingredient_id)

    ingredient.name = form.name.data
    ingredient.amount = form.amount.data

    db.session().commit()

    return redirect(url_for("ingredient_list"))

@app.route("/ingredient/<ingredient_id>/delete", methods=["GET"])
@login_required
def ingredient_delete(ingredient_id):

    db.session.delete(ingredient.query.get(ingredient_id))
    db.session().commit()

    return redirect(url_for("ingredient_list"))






    

   
