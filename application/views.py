from flask import render_template, session
from application import app
from application.recipes.models import Recipe
from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html", rec_per_user=Recipe.find_users_with_recipes(), user_count=Recipe.user_count(), rec_no_ing=Recipe.find_recipes_with_no_ingredients())
    
    
