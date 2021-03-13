# Userstories

1. As a user I want to collect my recipes easily to a database. Searching for recipes and adding recipes should be easy. 

               INSERT INTO Recipes (name, method) VALUES ('name', 'method');

               SELECT * FROM Recipes;
               
2. As a user I want to be able to list ingredients in the database and see a list of specific ingredients which I have included to a recipe.

               INSERT INTO ingredient (name, amount) VALUES ('name', 'amount');
               
               SELECT * FROM ingredient;

               "SELECT NAME FROM ingredient INNER JOIN recipe_ingredient ON recipe_ingredient.ingredientid = ingredient.id
               INNER JOIN recipe ON recipe_ingredient.recipeid = recipe.id WHERE recipe.recipeid = recipe.id"

3. As a user I can add ingredients to my recipes. I can also delete ingredients from my recipes, and delete my recipes from de database.

                UPDATE Recipes SET name = newname, method = newmethod WHERE Recipes.id = id;
                
                DELETE FROM Recipes WHERE Recipes.id = id;
 


