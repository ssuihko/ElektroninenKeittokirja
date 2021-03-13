# Installation guide

This guide is written for the Linux environment. Please make sure that python and sqlite3 are installed in your system.

## Installation

Download the github zip file from the address https://github.com/ssuihko/ElektroninenKeittokirja to your computer and unzip it. 

Use the python virtual environment with the commands below:

```
$ python -m venv venv
$ source venv/bin/activate
```
Install the requirements.txt requirements:

```
$ pip install -r requirements.txt
```

Add an admin account from terminal with the commands below:

```
$ sqlite3 application/recipes.db
sqlite> INSERT INTO account (name, username, password, role_id) VALUES('valinnainen', 'valinnainen', 'valinnainen', 1);
```

role_id = 1 gives ADMIN -privileges, role_id = 2 the priviledges of a normal user

Launch the application with the command

```
$ python run.py
```
And open the address printed on the terminal:
http://localhost:5000/

The application should now work locally.

