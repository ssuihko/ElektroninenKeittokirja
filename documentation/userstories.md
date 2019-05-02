# Userstories
1. Ruuanlaitosta kiinnostuneena ihmisenä haluan koota mielireseptini helposti jonnekin, josta ne ovat helposti käsillä. Alustalta
vaadin myös sen, että resepteistä on helppo pitää kirjaa, ja että niiden lisääminen on vaivatonta. 

               INSERT INTO Recipes (name, method) VALUES ('name', 'method');

               SELECT * FROM Recipes;
               
2. Ruoan raaka-aineet ovat minulle tärkeitä, ja haluan pitää myös niistä kirjaa. Elektronisen keittokirjan käyttäjänä voin lisätä niitä sovelluksen kautta
keittokirjaan, josta löydän ne helposti myöhemmin. 

               INSERT INTO ingredient (name, amount) VALUES ('name', 'amount');
               
               SELECT * FROM ingredient;

3. Voin myös lisätä keittokirjaan uusia ainesosia, ja kirjata ylös myös sen määrän, joka reseptiin kuluu.  Voin myös muokata ja poistaa lisäämiäni reseptejä sekä ainesosia keittokirjasta.  

                UPDATE Recipes SET name = newname, method = newmethod WHERE Recipes.id = id;
                
                DELETE FROM Recipes WHERE Recipes.id = id;
 
