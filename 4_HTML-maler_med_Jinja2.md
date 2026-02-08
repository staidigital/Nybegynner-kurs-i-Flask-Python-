## 4. HTML-maler med Jinja2

Å skrive HTML direkte i Python-koden blir fort rotete. Flask bruker **Jinja2** som mal-motor (template engine), slik at du kan lage egne HTML-filer.

### Mappestruktur

```
mitt-flask-prosjekt/
    app.py
    templates/
        forside.html
        om.html
        base.html
    static/
        style.css
```

> **Viktig:** Mappen **maa** hete `templates` (med s). Flask leter automatisk etter maler i denne mappen.

### Steg 1: Lag en base-mal

Lag filen `templates/base.html`:

```html
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block tittel %}Min Flask-app{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="/">Forside</a>
        <a href="/om">Om oss</a>
    </nav>

    <main>
        {% block innhold %}{% endblock %}
    </main>

    <footer>
        <p>Laget med Flask</p>
    </footer>
</body>
</html>
```

### Steg 2: Lag en sidmal som arver fra basen

Lag filen `templates/forside.html`:

```html
{% extends "base.html" %}

{% block tittel %}Forsiden{% endblock %}

{% block innhold %}
    <h1>Velkommen!</h1>
    <p>Dette er forsiden til min Flask-app.</p>

    {% if navn %}
        <p>Hei, {{ navn }}! Hyggelig aa se deg.</p>
    {% else %}
        <p>Hei, gjest!</p>
    {% endif %}
{% endblock %}
```

### Steg 3: Oppdater app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def forside():
    return render_template("forside.html", navn="Ola")

@app.route("/om")
def om_oss():
    return render_template("om.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### Jinja2 - de viktigste funksjonene

| Syntaks | Forklaring | Eksempel |
|---|---|---|
| `{{ variabel }}` | Skriver ut en verdi | `{{ navn }}` |
| `{% if ... %}` | If-setning | `{% if alder > 18 %}` |
| `{% for ... %}` | For-lokke | `{% for elev in elever %}` |
| `{% block ... %}` | Definer en blokk | `{% block innhold %}` |
| `{% extends ... %}` | Arv fra en annen mal | `{% extends "base.html" %}` |

### Lokker i maler

```python
# I app.py
@app.route("/elever")
def elever():
    elev_liste = ["Ola", "Kari", "Per", "Lisa"]
    return render_template("elever.html", elever=elev_liste)
```

```html
<!-- I templates/elever.html -->
{% extends "base.html" %}

{% block innhold %}
    <h1>Elever</h1>
    <ul>
        {% for elev in elever %}
            <li>{{ elev }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

---

## 6. Statiske filer (CSS og bilder)

Statiske filer (CSS, JavaScript, bilder) legges i mappen `static/`.

### Lag en CSS-fil

Lag filen `static/style.css`:

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

nav {
    background-color: #333;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
}

nav a {
    color: white;
    text-decoration: none;
    margin-right: 15px;
}

nav a:hover {
    text-decoration: underline;
}

h1 {
    color: #333;
    margin-bottom: 10px;
}

footer {
    margin-top: 40px;
    padding-top: 10px;
    border-top: 1px solid #ccc;
    color: #666;
}
```

### Lenke til statiske filer i HTML

Bruk alltid `url_for()` for aa lenke til statiske filer:

```html
<!-- CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<!-- Bilde -->
<img src="{{ url_for('static', filename='bilde.jpg') }}" alt="Beskrivelse">

<!-- JavaScript -->
<script src="{{ url_for('static', filename='script.js') }}"></script>
```
