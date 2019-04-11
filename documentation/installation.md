# Sovelluksen asentaminen 

Ohjeet on kirjoitettu Linux -järjestelmälle. Koneessa on oltava asennettuna python ja sqlite3

## Asentaminen

Lataa osoitteesta https://github.com/ssuihko/ElektroninenKeittokirja koneellesi zip -tiedosto ja pura se. 

Ota Pythonin virtuaaliympäristö käyttöön seuraavilla komennoilla

```
$ python -m venv venv
$ source venv/bin/activate
```
Asenna requirements.txt:ssä lukevat riippuvuudet

```
$ pip install -r requirements.txt
```

Lisää ensimmäinen käyttäjä

```
$ sqlite3 application/recipes.db
sqlite> INSERT INTO account (name, username, password, role_id) VALUES('valinnainen', 'valinnainen', 'valinnainen', 2);

role_id = 2 antaa käyttäjälle ADMIN -oikeudet, role_id = 1 tavallisen käyttäjän oikeudet

Käynnistä sovellus komennolla

```
$ python run.py
```
Ja klikkaa osoitetta 
http://localhost:5000/

Sovellus toimii nyt paikallisessa verkkoympäristössä

