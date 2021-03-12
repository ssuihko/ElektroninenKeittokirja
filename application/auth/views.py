from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from application import app, db, login_required_admin
from application.auth.models import User, Role
from application.recipes.models import Recipe
from application.ingredient.models import Ingredient
from application.auth.forms import LoginForm, RegisterForm
from application.models import recipeingredient

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("/auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate:
        return render_template("/auth/registerform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)
    u.role_id = 2
    u.role = Role.query.get(2)
    
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index")) 

@app.route("/auth/list", methods=["GET"])
@login_required_admin(role="admin")
def users_all():
    return render_template("auth/list.html", users=User.query.all())

@app.route("/auth/delete_user/<user_id>", methods=["GET"])
@login_required_admin(role="admin")
def user_delete(user_id):

    # get user
    user = User.query.get(user_id)

    # admin can not delete themselves
    if current_user.id == user.id:
        flash('Admin account can not delete themselves!')
        return redirect('auth/list.html', users=User.query.all())

    for r in user.recipes:
        reci_ingre = Ingredient.query.join(recipeingredient).join(Recipe).filter(recipeingredient.c.recipeid == r.recipeid and recipeingredient.c.ingredientid == Ingredient.ingredientid).all()
        for ingredient in reci_ingre:
            r.ingredients.remove(ingredient)

        db.session().commit()

        db.session.delete(r)
        db.session().commit()

    db.session.delete(User.query.get(user_id))
    db.session().commit()

    return render_template("auth/list.html", users=User.query.all())

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))