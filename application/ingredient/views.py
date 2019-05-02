from application import app, db
from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for, session
from application.ingredient.models import ingredient
from application.ingredient.forms import IngredientForm, IngredientEditForm
from application.recipes.forms import RecipeIngreForm
from application.recipes import models
from application.recipes.models import Recipes
from application.recipeIngredient.models import recipe_ingredient

@app.route("/ingredient", methods=["GET"])
def ingredient_all():
    return render_template("ingredient/listall.html", ingredient=ingredient.query.all())

@app.route("/ingredient/new/<recipes_id>/", methods=["GET"])
@login_required
def ingredient_form(recipes_id):
    session["recipesid"] = recipes_id
    return render_template("ingredient/new.html", recipes_id=recipes_id, form=IngredientForm())

@app.route("/ingredient/<recipes_id>/", methods=["GET"])
def ingredient_list(recipes_id):

    session["recipesid"] = recipes_id
    id = session["recipesid"]

    rec = Recipes.query.get(id)

    return render_template("ingredient/list.html", recipes_id=recipes_id, ingredient=ingredient.query.filter_by(recipe_id=id))
 
@app.route("/ingredient/recipe/<recipes_id>/", methods=["GET", "POST"])
@login_required
def ingredient_create(recipes_id):

    recipe = Recipes.query.get(recipes_id)

    form = IngredientForm(request.form)

    ingre = ingredient(form.name.data, form.amount.data)
    ingre.recipe_id = recipes_id

    db.session().add(ingre)
    db.session().commit()

    ri = recipe_ingredient(recipes_id, ingre.id)
        
    db.session().add(ri)

    db.session().commit()

    return render_template("ingredient/list.html", recipes_id=recipes_id, ingredient=ingredient.query.filter_by(recipe_id=recipes_id))

@app.route("/ingredient/<ingredient_id>/<recipes_id>/delete", methods=["GET"])
@login_required
def ingredient_delete(recipes_id, ingredient_id):

    db.session.delete(ingredient.query.get(ingredient_id))
    r = recipe_ingredient.query.get((recipes_id, ingredient_id))
    db.session.delete(r)
    db.session().commit()

    return render_template("ingredient/listall.html", ingredient=ingredient.query.all())









    

   
