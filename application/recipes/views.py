from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipes
from application.recipes.forms import RecipeForm

@app.route("/recipes", methods=["GET"])
def recipe_index():
    return render_template("recipes/list.html", recipes = Recipes.query.all())

@app.route("/recipes/new/")
@login_required
def recipe_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required
def recipe_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    t = Recipes(form.name.data, form.method.data)
    t.account_id = current_user.id    

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("recipe_index"))

@app.route("/recipes/delete/", methods=["POST"])
@login_required
def recipe_remove():
    
    name = Recipes(request.form.get("name"))
    recipe = Recipes.query.filter_by(name=name).first()
    db.session().delete(recipe)
    db.session().commit()

    return redirect(url_for("recipe_index"))

@app.route("/recipes/update/", methods=["POST"])
@login_required
def recipe_update():

    name = Recipes(request.form.get("name"))
    old = Recipes.query.filter_by(name=name).first()
    methd = Recipes(request.form.get("method"))
    old.method = methd
    
    db.session().commit()

    return redirect(url_for("recipe_index"))
    



