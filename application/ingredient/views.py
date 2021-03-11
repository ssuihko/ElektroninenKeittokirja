from application import app, db, login_required_admin
from flask_login import current_user, login_required
from sqlalchemy import func
from flask import redirect, render_template, request, url_for, session, flash
from application.ingredient.models import Ingredient
from application.ingredient.models import models
from application.ingredient.forms import IngredientForm, IngredientEditForm
#from application.recipes.forms import RecipeIngreForm
from application.recipes.forms import RecipeForm
from application.recipes import models
from application.recipes.models import Recipe
#from application.recipeIngredient.models import recipe_ingredient
from application.models import recipeingredient

@app.route("/ingredients", methods=["GET", "POST"]) 
#@login_required(role="ADMIN")
@login_required
def ingredient_all():

    ingredients = Ingredient.query.all()
    included_ingredients = Ingredient.ingredientWithRecipes()

    return render_template("ingredient/listall.html", included_ingres=included_ingredients, ingredient=ingredients)

@app.route("/recipe/ingredients/<recipes_id>/", methods=["GET", "POST"])
def ingredient_list(recipes_id):

    recipe = Recipe.query.get(recipes_id)

    method = Recipe.query.get(recipes_id).method

    idd = Recipe.query.get(recipes_id).recipeId

    return render_template("ingredient/list.html", recipe=recipe, recipemethod=method, ingredient=Recipe.find_recipe_ingredients(idd))

@app.route("/ingredient/new/<recipes_id>/", methods=["GET"])
def ingredient_form(recipes_id):
    recipe = Recipe.query.get(recipes_id)

    if recipe not in current_user.recipes:
        flash('You can not add ingredients to recipes which are not yours')
        return redirect(url_for("ingredient_list", recipes_id=recipes_id))

    form = IngredientForm()
    return render_template("ingredient/new.html", form=form, recipe=recipe)

@app.route("/recipe/create/ingredient/<recipes_id>/", methods=["POST"])
def ingredient_create(recipes_id):
    
    form = IngredientForm(request.form)

    ingredients = Ingredient.query.all()
    recipe = Recipe.query.get(recipes_id)

    ingre = Ingredient(form.name.data)
 
    if not form.validate():
        return render_template("ingredient/new.html", form=form, recipe=recipe)
    
    # The ingredient is already in the recipe
    for ing in recipe.recipeingredient:
        if ing.name == ingre.name:
            flash('This ingredient is already in the recipe')
            return render_template("ingredient/new.html", form=form, recipe=recipe)

    # The ingredient is not already in the database, add it
    if Ingredient.query.filter_by(name = ingre.name).first() is None:
        db.session().add(ingre)
        db.session().commit()
        nowIngredient = Ingredient.query.filter_by(name=ingre.name).first()
    else:
        nowIngredient = Ingredient.query.filter_by(name=ingre.name).first()

    recipe.recipeingredient.append(nowIngredient)
    db.session().commit()

    return redirect(url_for("ingredient_list", recipes_id=recipes_id))

@app.route("/ingredient/<ingredient_id>/delete", methods=["POST"])
@login_required_admin(role="admin")
def ingredient_delete(ingredient_id):

    ingre = Ingredient.query.get(ingredient_id)

    if ingre is None:
        ingre = Ingredient.query.first()
        print(ingre)

    print('päästiin tänne!')
    print(ingre.name)
    print(ingre.ingredientId)
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHH')
 
    reci_ingre = Recipe.query.join(recipeingredient).join(Ingredient).filter(recipeingredient.c.ingredientId == ingre.ingredientId).all()

    for recipe in reci_ingre:
        print(recipe)
        recipe.recipeingredient.remove(ingre)

    try:

        db.session().commit()

        db.session.delete(ingre)
    
        db.session().commit()

    except Exception as e:
        print(e)


    return redirect(url_for("ingredient_all"))

@app.route("/recipe/ingredient/<ingredient_id>/<recipe_id>/delete", methods=["POST"])
@login_required
def ingredient_delete_from_recipe(ingredient_id, recipe_id):

    #etsi ainesosa
    ingre = Ingredient.query.get(ingredient_id)
    reci = Recipe.query.get(recipe_id)

    print('ingreinfooooooooooooooooooooooooooooooooooooo')
    print(ingredient_id)
    print(ingre.name)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('recipeinfoooooooooooooooooooooooooooooooooooooooo')
    print(recipe_id)
    print(reci.name)
    print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeennnnddddddddd')

    if reci not in current_user.recipes:
        flash('You can not delete ingredients in recipes which are not yours')
        return redirect(url_for("ingredient_list", recipes_id=recipe_id))

    #poista tästä reseptistä
    reci.recipeingredient.remove(ingre)
    db.session().commit()

    return redirect(url_for("ingredient_list", recipes_id=recipe_id))

@app.route("/ingredient/<ingredient_id>/update", methods=["GET", "POST"])
@login_required_admin(role="admin")
def ingredient_update(ingredient_id):

    if request.method == "GET":

        ingredient = Ingredient.query.get(ingredient_id)
        form = IngredientEditForm(obj=ingredient)

        return render_template("ingredient/update.html", form=form, ingredient_id=ingredient.ingredientId)

    form = IngredientEditForm(request.form)
    ingredient = Ingredient.query.get(ingredient_id)

    if not form.validate():
        return render_template("ingredient/update.html", form=form, ingredient_id=ingredient.ingredientId)

    ingredient.name = form.name.data

    db.session().commit()

    return redirect(url_for("ingredient_all"))







    

   
