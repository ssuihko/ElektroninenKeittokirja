from application import app, db, login_manager
from flask_login import current_user, login_required
from flask import redirect, render_template, request, url_for, session, flash
from sqlalchemy import func
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm, RecipeEditForm
from application.ingredient.models import Ingredient
from application.auth.models import User
from application.ingredient.forms import IngredientForm
from application.models import recipeingredient
import sys
import datetime

# Why is this ingredients all? 
#@app.route("/recipes/all", methods=["GET"])
#@login_required(role="ADMIN")
#def ingredients_all():
#    return render_template("recipes/list.html", recipes=Recipe.query.all())

@app.route("/recipes", methods=["GET"])
@login_required
def recipe_index():
    
    q = request.args.get('q')

    if q:
        recipes = Recipe.query.filter(Recipe.name.contains(q))
    else: 
        recipes = Recipe.query.order_by(func.lower(Recipe.name))

    return render_template("recipes/list.html", recipes=recipes)

@app.route("/recipes/user/", methods=["GET"])
@login_required
def only_my_recipes():
    holder = current_user.recipes  
    return render_template("recipes/list.html", recipes=current_user.recipes.order_by(func.lower(Recipe.name)))

@app.route("/recipes/new/")
@login_required
def recipe_form():

    ingredients = Ingredient.query.all()
    form = RecipeForm()
    form.ingredients.choices = [(ingredient.ingredientid, ingredient.name) for ingredient in ingredients]

    return render_template("recipes/new.html", form = form)

@app.route("/recipes/", methods=["POST"])
@login_required
def recipe_create():

    form = RecipeForm(request.form)
    ingredients = Ingredient.query.all()
    form.ingredients.choices = [(ingredient.ingredientid, ingredient.name) for ingredient in ingredients]
 
    r = Recipe(form.name.data, form.method.data, current_user.id)

    ingredient_ids = form.ingredients.data   

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    
    db.session().add(r)
    db.session().commit()

    db.session.refresh(r)

    for id in ingredient_ids:
        i = Ingredient.query.get(id)
        r.recipeingredient.append(i)
        db.session().commit()

    return redirect(url_for("recipe_index"))

@app.route("/recipes/<recipes_id>/delete/", methods=["POST"])
@login_required
def recipe_delete(recipes_id):

    recipe = Recipe.query.get(recipes_id)

    if recipe not in current_user.recipes:
        flash('You can not delete recipes which are not yours')
        return redirect(url_for("recipe_index"))

    reci_ingre = Ingredient.query.join(recipeingredient).join(Recipe).filter(recipeingredient.c.recipeid == recipe.recipeid and recipeingredient.c.ingredientid == Ingredient.ingredientid).all()

    for ingredient in reci_ingre:
        recipe.recipeingredient.remove(ingredient)
    db.session().commit()

    db.session.delete(recipe)
    db.session().commit()

    return redirect(url_for("recipe_index"))

@app.route("/recipes/<recipes_id>/update/", methods=["GET", "POST"])
@login_required
def recipe_update(recipes_id):

    recipe = Recipe.query.get(recipes_id)
    if recipe not in current_user.recipes:
        flash('You can not edit recipes which are not yours')
        return redirect(url_for("recipe_index"))

    if request.method == "GET":

        recipes = Recipe.query.get(recipes_id)
        form = RecipeEditForm(obj=recipes)

        return render_template("recipes/update.html", form=form, recipes_id=recipes_id)
   
    form = RecipeEditForm(request.form)
    recipes = Recipe.query.get(recipes_id)

    if not form.validate():
        return render_template("recipes/update.html", form=form, recipes_id=recipes_id)

    recipes.name = form.name.data
    recipes.method = form.method.data

    db.session().commit()

    return redirect(url_for("recipe_index"))




