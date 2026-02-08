1. `pip3 install -r requirements.txt`eller `uv pip install -r requirements.txt`hvis du bruker uv. 
2. Sett opp databasen: `mysql -u root -p < setup_database.sql`
3. Lag ny bruker med passord og oppdater `db.py`
4. Kjør programmet med `python app.py` eller eventuelt med `uv run app.py`om du bruker uv.
5. Åpne http://127.0.0.1:5000
___
Prosjektet dekker alle konseptene fra guiden i én samlet app - fra enkle ruter og maler helt til MariaDB-integrasjon, med 4 eksempel-spillere ferdig lagt inn i databasen.