## Toteuttamatta jääneet ominaisuudet 2019

### Ingredient create -metodi

Yksi selkein puute sovelluksessa on se, etteivät ainesosien nimet ja määrät näy sarakkeissa, vaikka muu informaatio menee tietokantaan. 

#### 2021 päivitys

Virhe korjattu, jokainen käyttäjä näkee ainesosien nimet, sekä sen, kuinka monessa reseptissä ainesosa on käytössä. Vain admin voi poistaa tai muokata ainesosia. 

### normalisointi 

Myös tietokannan normalisoinnissa on puutteita ingredients -taulun suhteen. Ingrediet -taulussa voi tällä hetkellä käytännössä olla useita samannimisiä ja samanmääräisiä ainesosia.

#### 2021 päivitys

Korjattu, samannimisiä ainesosia ei voi enää lisätä. 

### ingredient form validate ja ingredient update 

Tällä hetkellä ingredient -create metodissa ei ole form validate -ominaisuutta. Sovelluksen koodissa on nähtävillä myös ingredient_update metodi, joka ei ole sovelluksessa käytössä.

#### 2021 päivitys

validointi käytössä.


## Tiedetyt bugit 2021

Käyttäjä ei voi poistaa ainesosalistasta ensimmäistä ainesosaa. Bugi ilmenee sekä reseptikohtaisessa ainesosalistauksessa että kaikkien ainesosien listauksessa.



