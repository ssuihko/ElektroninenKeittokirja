## Tietokannan rakenne

<img src="" width="400" height="450">

## CREATE TABLE lauseet

CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);

CREATE TABLE recipes (
	id INTEGER NOT NULL, 
	name VARCHAR(130) NOT NULL, 
	method VARCHAR(400) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE ingredient (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	amount VARCHAR(144) NOT NULL, 
	recipe_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id)
);

CREATE TABLE IF NOT EXISTS "recipeIngredient" (
	recipe_id INTEGER NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
);

CREATE TABLE recipe_ingredient (
	recipe_id INTEGER NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	PRIMARY KEY (recipe_id, ingredient_id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
);
