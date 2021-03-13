# RecipeApplication Guide

The application is available on heroku on the address <https://tsoha-keittokirja.herokuapp.com/>, or locally on the address <http://127.0.0.1:5000/>

## Login and register

At the moment there are 2 default accounts on the application

|Username|Password|Role |
|--------|--------|-----|
|kokki   |kirja   |admin|
|kakku   |leipuri |user |

Click the login button on the front page to login, or the register button to create a new account. 

### Functionalities
#### Front page

The front page shows the current user count of the application.  
On the front page there are also links on the navigation bar which can be accessed only by an authenticated user: List Recipes, Add a Recipe and All Ingredients. 

#### List recipes

By clicking the List Recipes link the user can see all the recipes on on the database. The user can modify and delete their own recipes and search recipes by name. The user can see the full description of the recipe by pressing the Open Recipe button. The user can add ingredients to the recipe by clicking the Add an ingredient button on the Recipes description page. 

#### Add recipe

User can add a recipe to the database by clicking the Add a Recipe button on the navigation bar. To select multiple ingredients to the recipe hold the shift button down while clicking. 

#### List ingredients

By clicking the link List ingredients the user can see all the ingredients in the database, the popularity of the ingredient by the usage count. 

### Admin specific functionalities

#### List ingredients
Only admin can delete and modify ingredients.

#### User List
Only admin can see the All Users link on the navigation bar and delete users. The user's recipes will be deleted from the database upon the deletion of their account. 

