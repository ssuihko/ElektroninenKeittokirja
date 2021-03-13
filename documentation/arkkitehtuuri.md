## Database structure

<img src="https://github.com/ssuihko/ElektroninenKeittokirja/blob/master/documentation/tietokantakaavio.png">

## CREATE TABLE 

CREATE TABLE role (
	"createdOn" DATETIME, 
	"modifiedOn" DATETIME, 
	roleid INTEGER NOT NULL, 
	name VARCHAR(5) NOT NULL, 
	PRIMARY KEY (roleid)
);
CREATE TABLE ingredient (
	"createdOn" DATETIME, 
	"modifiedOn" DATETIME, 
	ingredientid INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (ingredientid), 
	UNIQUE (name)
);
CREATE TABLE account (
	"createdOn" DATETIME, 
	"modifiedOn" DATETIME, 
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES role (roleid)
);
CREATE TABLE recipe (
	"createdOn" DATETIME, 
	"modifiedOn" DATETIME, 
	recipeid INTEGER NOT NULL, 
	name VARCHAR(130) NOT NULL, 
	method TEXT NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (recipeid), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE recipe_ingredient (
	recipeid INTEGER, 
	ingredientid INTEGER, 
	FOREIGN KEY(recipeid) REFERENCES recipe (recipeid), 
	FOREIGN KEY(ingredientid) REFERENCES ingredient (ingredientid)
);

