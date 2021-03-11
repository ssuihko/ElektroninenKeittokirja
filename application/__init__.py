from flask import Flask, redirect, url_for
app = Flask(__name__)
from flask_login import current_user

# database functionality and ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


from application.auth.models import User, Role
#Roles in login required
from functools import wraps

def login_required_admin(role):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                print('ei nykyinen kayttaja')
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                print('autentikoinnissa mattaa')
                return login_manager.unauthorized()
            
            unauthorized = False

            rolename = Role.query.get(current_user.role_id)

            if str(rolename) != role:
                print('roolinnimi eri kuin rooli')
                print(role)
                print(rolename)
                unauthorized = True

            if unauthorized:
                print('unauthorized')
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
   
# application content
from application import views

from application.recipes import models
from application.recipes import views

from application.ingredient import models
from application.ingredient import views

from application.auth import models
from application.auth import views

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database creation

try:
    db.create_all()

except:
    pass

