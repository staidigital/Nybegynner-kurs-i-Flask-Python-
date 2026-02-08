## 6. Database med MariaDB

Hittil har vi lagret data i Python-lister, men da forsvinner alt naar serveren stopper. Med en **database** kan vi lagre data permanent. Vi bruker **MariaDB** (en populaer variant av MySQL).

### Oversikt over hvordan det fungerer

```
Bruker (nettleser)  --->  Flask-server  --->  MariaDB-database
     |                        |                     |
     |   Fyller ut skjema     |                     |
     |----------------------->|                     |
     |                        |   INSERT INTO ...   |
     |                        |-------------------->|
     |                        |   OK / data tilbake |
     |                        |<--------------------|
     |   Viser resultat       |                     |
     |<-----------------------|                     |
```

### Steg 1: Installer MariaDB

#### Windows

Last ned og installer MariaDB fra [mariadb.org/download](https://mariadb.org/download/). Velg standard-innstillinger og sett et passord for root-brukeren.

#### Mac

```bash
brew install mariadb
brew services start mariadb
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install mariadb-server
sudo systemctl start mariadb
```

### Steg 2: Opprett en database og tabell

Logg inn i MariaDB fra terminalen:

```bash
mysql -u root -p
```

Skriv inn passordet du satte under installasjonen. Deretter kjorer du disse SQL-kommandoene:

```sql
-- Lag en ny database
CREATE DATABASE flask_spilldb;

-- Bytt til den nye databasen
USE flask_spilldb;

-- Lag en tabell for spillere
CREATE TABLE spillere (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(100) NOT NULL,
    favorittspill VARCHAR(200) NOT NULL
);

-- Sjekk at tabellen ble opprettet
DESCRIBE spillere;
```

#### Forklaring av tabellen

| Kolonne | Type | Forklaring |
|---|---|---|
| `id` | `INT AUTO_INCREMENT` | Unikt nummer som oeker automatisk |
| `navn` | `VARCHAR(100)` | Tekstfelt for navn (maks 100 tegn) |
| `favorittspill` | `VARCHAR(200)` | Tekstfelt for favorittspill (maks 200 tegn) |

> **Tips:** `PRIMARY KEY` betyr at `id` er unik for hver rad og brukes til aa identifisere den.

### Steg 3: Installer Python-pakken for MariaDB

```bash
pip install mysql-connector-python
```

Denne pakken lar Python snakke med MariaDB-databasen.

### Steg 4: Koble Flask til MariaDB

Oppdater mappestrukturen:

```
mitt-flask-prosjekt/
    app.py
    db.py                  <-- NY FIL for database-tilkobling
    templates/
        base.html
        spillere.html      <-- NY FIL
        ny_spiller.html    <-- NY FIL
    static/
        style.css
```

#### Lag filen `db.py` - Database-tilkobling

```python
import mysql.connector

def get_db():
    """Kobler til MariaDB-databasen og returnerer tilkoblingen."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ditt_passord",  # Bytt til ditt MariaDB-passord
        database="flask_spilldb"
    )
    return connection
```

> **Viktig:** Bytt ut `"ditt_passord"` med passordet du satte da du installerte MariaDB.

#### Oppdater `app.py`

```python
from flask import Flask, render_template, request, redirect, url_for
from db import get_db

app = Flask(__name__)

@app.route("/")
def forside():
    return render_template("forside.html")

@app.route("/spillere")
def spillere():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM spillere")
    alle_spillere = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("spillere.html", spillere=alle_spillere)

@app.route("/spillere/ny", methods=["GET", "POST"])
def ny_spiller():
    if request.method == "POST":
        navn = request.form["navn"]
        favorittspill = request.form["favorittspill"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO spillere (navn, favorittspill) VALUES (%s, %s)",
            (navn, favorittspill)
        )
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for("spillere"))

    return render_template("ny_spiller.html")

@app.route("/spillere/slett/<int:id>")
def slett_spiller(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM spillere WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for("spillere"))

if __name__ == "__main__":
    app.run(debug=True)
```

### Steg 5: Lag HTML-malene

#### `templates/ny_spiller.html` - Skjema for ny spiller

```html
{% extends "base.html" %}

{% block tittel %}Ny spiller{% endblock %}

{% block innhold %}
    <h1>Legg til ny spiller</h1>

    <form method="POST" action="{{ url_for('ny_spiller') }}">
        <div>
            <label for="navn">Navn:</label>
            <input type="text" id="navn" name="navn" required>
        </div>
        <div>
            <label for="favorittspill">Favorittspill:</label>
            <input type="text" id="favorittspill" name="favorittspill" required>
        </div>
        <button type="submit">Legg til</button>
    </form>

    <p><a href="{{ url_for('spillere') }}">Tilbake til spillerlisten</a></p>
{% endblock %}
```

#### `templates/spillere.html` - Vis alle spillere

```html
{% extends "base.html" %}

{% block tittel %}Spillere{% endblock %}

{% block innhold %}
    <h1>Spillere og favorittspill</h1>

    <p><a href="{{ url_for('ny_spiller') }}">+ Legg til ny spiller</a></p>

    {% if spillere %}
        <table>
            <thead>
                <tr>
                    <th>Navn</th>
                    <th>Favorittspill</th>
                    <th>Handling</th>
                </tr>
            </thead>
            <tbody>
                {% for spiller in spillere %}
                <tr>
                    <td>{{ spiller.navn }}</td>
                    <td>{{ spiller.favorittspill }}</td>
                    <td>
                        <a href="{{ url_for('slett_spiller', id=spiller.id) }}"
                           onclick="return confirm('Er du sikker?')">
                            Slett
                        </a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>Ingen spillere registrert ennaa.</p>
    {% endif %}
{% endblock %}
```

### Steg 6: Legg til CSS for tabellen

Legg til dette nederst i `static/style.css`:

```css
/* Tabell-styling */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #333;
    color: white;
}

tr:hover {
    background-color: #f5f5f5;
}

/* Skjema-styling */
form div {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"], textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #333;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}
```

### Forklaring av de viktigste database-operasjonene

| Operasjon | SQL-kommando | Python-kode |
|---|---|---|
| **Hente alle rader** | `SELECT * FROM spillere` | `cursor.fetchall()` |
| **Legge til rad** | `INSERT INTO spillere VALUES (...)` | `cursor.execute(sql, verdier)` |
| **Slette rad** | `DELETE FROM spillere WHERE id = ?` | `cursor.execute(sql, (id,))` |
| **Lagre endringer** | - | `db.commit()` |
| **Lukke tilkobling** | - | `db.close()` |

### Viktig om sikkerhet: Parameteriserte sporringer

Legg merke til at vi **aldri** setter brukerdata direkte inn i SQL-strengen. Vi bruker `%s` som plassholdere:

```python
# RIKTIG - trygt mot SQL-injeksjon
cursor.execute(
    "INSERT INTO spillere (navn, favorittspill) VALUES (%s, %s)",
    (navn, favorittspill)
)

# FEIL - saarbart for SQL-injeksjon! Gjoer ALDRI dette!
cursor.execute(
    f"INSERT INTO spillere (navn, favorittspill) VALUES ('{navn}', '{favorittspill}')"
)
```

> **SQL-injeksjon** er en type angrep der noen skriver ondsinnet SQL-kode i et skjemafelt. Ved aa bruke `%s`-plassholdere beskytter Flask/MySQL-connector oss mot dette automatisk.

### Vanlige feilmeldinger

| Feilmelding | Aarsak | Losning |
|---|---|---|
| `Access denied for user 'root'` | Feil passord i `db.py` | Sjekk at passordet stemmer |
| `Unknown database 'flask_spilldb'` | Databasen finnes ikke | Kjor `CREATE DATABASE flask_spilldb;` i MariaDB |
| `Table 'spillere' doesn't exist` | Tabellen er ikke opprettet | Kjor `CREATE TABLE`-kommandoen fra steg 2 |
| `Can't connect to MySQL server` | MariaDB kjorer ikke | Start MariaDB-tjenesten |