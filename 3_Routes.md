## 3. Ruter (Routes)

En **rute** (route) er en URL-sti som er koblet til en Python-funksjon. Nar noen besoker den URLen, kjorer funksjonen.

### Flere sider

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def forside():
    return "<h1>Forsiden</h1><p>Velkommen til min nettside!</p>"

@app.route("/om")
def om_oss():
    return "<h1>Om oss</h1><p>Vi er elever som laerer Flask.</p>"

@app.route("/kontakt")
def kontakt():
    return "<h1>Kontakt</h1><p>Send oss en e-post!</p>"

if __name__ == "__main__":
    app.run(debug=True)
```

Na kan du besoeke:

- `http://127.0.0.1:5000/` - Forsiden
- `http://127.0.0.1:5000/om` - Om oss
- `http://127.0.0.1:5000/kontakt` - Kontakt

### Dynamiske ruter

Du kan lage ruter som tar imot verdier fra URLen:

```python
@app.route("/hils/<navn>")
def hils(navn):
    return f"<h1>Hei, {navn}!</h1>"
```

Naa kan du besoeke `http://127.0.0.1:5000/hils/Ola` og se "Hei, Ola!".

### Flere eksempler pa dynamiske ruter

```python
@app.route("/elev/<navn>/<alder>")
def elev_info(navn, alder):
    return f"<p>{navn} er {alder} aar gammel.</p>"

@app.route("/kvadrat/<int:tall>")
def kvadrat(tall):
    resultat = tall ** 2
    return f"<p>{tall} i annen er {resultat}</p>"
```

> **Merk:** `<int:tall>` betyr at Flask automatisk konverterer verdien til et heltall.