## 2. Din forste Flask-app

Lag en ny fil som heter `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def forside():
    return "<h1>Hei, verden!</h1><p>Min forste Flask-app!</p>"

if __name__ == "__main__":
    app.run(debug=True)
```

### Kjoer appen

```bash
python app.py
```

Du vil se noe slikt i terminalen:

```
 * Running on http://127.0.0.1:5000
```

Apne nettleseren og ga til **http://127.0.0.1:5000** - da ser du nettsiden din!

### Forklaring linje for linje

```python
from flask import Flask          # Importerer Flask-biblioteket

app = Flask(__name__)            # Lager en Flask-applikasjon

@app.route("/")                  # Denne funksjonen kjorer nar noen besoker forsiden
def forside():
    return "<h1>Hei, verden!</h1>"  # Sender HTML tilbake til nettleseren

if __name__ == "__main__":
    app.run(debug=True)          # Starter serveren. debug=True gir
                                 # automatisk omstart ved endringer
```

> **Tips:** `debug=True` gjor at serveren starter pa nytt automatisk hver gang du lagrer endringer i koden. Veldig nyttig under utvikling!