# Intro og oppsett
## Hva er Flask?

Flask er et **mikro-rammeverk** for Python som lar deg lage nettsider og webapplikasjoner. Det kalles "mikro" fordi det gir deg bare det mest nodvendige for a komme i gang, uten masse unodvendig kompleksitet.

Med Flask kan du:

- Lage nettsider med Python
- Bygge APIer
- Haandtere skjemaer og brukerinndata
- Koble til databaser

### Hvordan fungerer en webapplikasjon?

```
Bruker (nettleser)  --->  Flask-server  --->  Svar (HTML-side)
     |                        |
     |   "Gi meg forsiden"    |
     |----------------------->|
     |                        |  (Python-kode kjorer)
     |   "<html>...</html>"   |
     |<-----------------------|
```

Nettleseren sender en **forespørsel** (request) til serveren, og serveren sender tilbake et **svar** (response) - vanligvis en HTML-side.

---

##  Installasjon

### Steg 1: Sjekk at Python er installert

Apne terminalen (Terminal pa Mac, Ledetekst/PowerShell pa Windows) og skriv:

```bash
python --version
```

Du trenger Python 3.7 eller nyere.

### Steg 2: Lag en prosjektmappe

```bash
mkdir mitt-flask-prosjekt
cd mitt-flask-prosjekt
```

### Steg 3: Lag et virtuelt miljo (anbefalt)

Et virtuelt miljo holder pakkene dine adskilt fra andre prosjekter.

```bash
# Mac/Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate
```

Nar det virtuelle miljoet er aktivt, ser terminalen omtrent slik ut:

```
(venv) $
```

### Steg 4: Installer Flask

```bash
pip install flask
```

Sjekk at det fungerte:

```bash
python -c "import flask; print(flask.__version__)"
```

---