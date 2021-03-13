## Unimplemented features 2019

### Ingredient create -method

Ingredients and their names are not visible on the ingredient lists, although the information gets uploaded to the database. 

#### 2021 update

Fixed, every user can see the name of the ingredient and the usage count of the ingredient on the list all ingredients page. Only admin can modify and delete ingredients.

### Normalization

The user can add multiple ingredients to the ingredients table with the same name.

#### 2021 update

Fixed, user can no more add ingredients with the same name to the recipe.

### ingredient form validate and ingredient update 

Ingredient -create method does not have form validation, and the ingredient_update method is visible in the application, but not usable.

#### 2021 update

Validation is now in use for the ingredient create -method. Admin can modify ingredients. 

## Known bugs 2021

User can not delete the first ingredient in both all ingredients listing and recipe specific ingredient listing. 





