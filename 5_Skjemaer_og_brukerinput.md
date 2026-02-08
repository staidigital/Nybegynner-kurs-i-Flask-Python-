## 5. Skjemaer og brukerinndata

### Et enkelt soekeskjema

Lag filen `templates/sok.html`:

```html
{% extends "base.html" %}

{% block innhold %}
    <h1>Soek</h1>

    <form method="POST" action="/sok">
        <label for="sokeord">Skriv inn et soekeord:</label>
        <input type="text" id="sokeord" name="sokeord" required>
        <button type="submit">Soek</button>
    </form>

    {% if resultat %}
        <h2>Resultat</h2>
        <p>Du soekte etter: <strong>{{ resultat }}</strong></p>
    {% endif %}
{% endblock %}
```

Oppdater `app.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sok", methods=["GET", "POST"])
def sok():
    resultat = None
    if request.method == "POST":
        resultat = request.form["sokeord"]
    return render_template("sok.html", resultat=resultat)
```

### Forklaring av GET og POST

| Metode | Bruksomraade | Eksempel |
|---|---|---|
| **GET** | Hente data / vise en side | Besoeke en nettside |
| **POST** | Sende data til serveren | Sende inn et skjema |

### Et mer avansert skjema - gjesteboka

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Enkel liste som "database"
meldinger = []

@app.route("/gjestebok")
def gjestebok():
    return render_template("gjestebok.html", meldinger=meldinger)

@app.route("/gjestebok/ny", methods=["POST"])
def ny_melding():
    navn = request.form["navn"]
    melding = request.form["melding"]
    meldinger.append({"navn": navn, "melding": melding})
    return redirect(url_for("gjestebok"))

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/gjestebok.html -->
{% extends "base.html" %}

{% block innhold %}
    <h1>Gjestebok</h1>

    <form method="POST" action="{{ url_for('ny_melding') }}">
        <div>
            <label for="navn">Navn:</label>
            <input type="text" id="navn" name="navn" required>
        </div>
        <div>
            <label for="melding">Melding:</label>
            <textarea id="melding" name="melding" required></textarea>
        </div>
        <button type="submit">Legg til</button>
    </form>

    <h2>Meldinger</h2>
    {% if meldinger %}
        {% for m in meldinger %}
            <div class="melding">
                <strong>{{ m.navn }}</strong>
                <p>{{ m.melding }}</p>
            </div>
        {% endfor %}
    {% else %}
        <p>Ingen meldinger ennaa. Vaer den forste!</p>
    {% endif %}
{% endblock %}
```

### Viktige funksjoner

| Funksjon | Forklaring |
|---|---|
| `request.form["felt"]` | Henter data fra et skjemafelt |
| `request.method` | Sjekker om det er GET eller POST |
| `redirect(url)` | Sender brukeren til en annen side |
| `url_for("funksjonsnavn")` | Genererer URL fra et funksjonsnavn |

---