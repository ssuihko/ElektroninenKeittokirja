from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User, Role
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("/auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate:
        return render_template("/auth/registerform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)
    u.role = Role.query.get(1)
    
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index")) 

@app.route("/auth/list", methods=["GET"])
@login_required(role="ADMIN")
def users_all():
    return render_template("auth/list.html", users=User.query.all())

@app.route("/auth/delete_user/<user_id>", methods=["GET"])
@login_required(role="ADMIN")
def user_delete(user_id):
    db.session.delete(User.query.get(user_id))
    db.session().commit()

    return render_template("auth/list.html", users=User.query.all())

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))