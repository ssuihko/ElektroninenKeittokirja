from flask import render_template
from application import app
from application.recipes.models import Recipes

@app.route('/')
def index():
    return render_template("index.html", rec_per_user=Recipes.find_users_with_recipes(), rec_no_ing=Recipes.find_recipes_with_no_ingredients())
    
    
