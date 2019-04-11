from application import app, db, login_required, login_manager
from flask_login import current_user

from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipes
from application.recipes.forms import RecipeForm, RecipeEditForm
from application.ingredient.models import ingredient

@app.route("/recipes/all", methods=["GET"])
@login_required(role="ADMIN")
def ingredients_all():
    return render_template("recipes/list.html", recipes=Recipes.query.all())

@app.route("/recipes", methods=["GET"])
def recipe_index():
    return render_template("recipes/list.html", recipes=current_user.recipes)

@app.route("/recipes/new/")
@login_required()
def recipe_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required()
def recipe_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    t = Recipes(form.name.data, form.method.data)
    t.account_id = current_user.id    

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("recipe_index"))

@app.route("/recipes/<recipes_id>/delete/", methods=["GET"])
@login_required()
def recipe_delete(recipes_id):

    db.session.delete(Recipes.query.get(recipes_id))
    db.session().commit()

    return redirect(url_for("recipe_index"))

@app.route("/recipes/<recipes_id>/update/", methods=["GET", "POST"])
@login_required()
def recipe_update(recipes_id):

    if request.method == "GET":

        recipes = Recipes.query.get(recipes_id)
        form = RecipeEditForm(obj=recipes)

        return render_template("recipes/update.html", form=form, recipes_id=recipes_id)
   
    form = RecipeEditForm(request.form)
    recipes = Recipes.query.get(recipes_id)

    if not form.validate():
        return render_template("recipes/update.html", form=form, recipes_id=recipes_id)

    recipes.name = form.name.data
    recipes.method = form.method.data

    db.session().commit()

    return redirect(url_for("recipe_index"))


