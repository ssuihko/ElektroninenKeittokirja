from flask import render_template, session
from application import app
from application.recipes.models import Recipe
from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html", user_count=Recipe.user_count())
    
    
