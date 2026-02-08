from flask import Flask, render_template, request, redirect, url_for
from db import get_db

app = Flask(__name__)

# Enkel liste som "database" for gjesteboka
meldinger = []


# --- Forside ---

@app.route("/")
def forside():
    return render_template("forside.html")


# --- Om oss ---

@app.route("/om")
def om_oss():
    return render_template("om.html")


# --- Dynamisk rute: Hils paa noen ---

@app.route("/hils/<navn>")
def hils(navn):
    return render_template("hils.html", navn=navn)


# --- Elever (eksempel paa for-lokke i mal) ---

@app.route("/elever")
def elever():
    elev_liste = ["Ola", "Kari", "Per", "Lisa"]
    return render_template("elever.html", elever=elev_liste)


# --- Soek (eksempel paa GET/POST) ---

@app.route("/sok", methods=["GET", "POST"])
def sok():
    resultat = None
    if request.method == "POST":
        resultat = request.form["sokeord"]
    return render_template("sok.html", resultat=resultat)


# --- Gjestebok (skjema med liste-lagring) ---

@app.route("/gjestebok")
def gjestebok():
    return render_template("gjestebok.html", meldinger=meldinger)


@app.route("/gjestebok/ny", methods=["POST"])
def ny_melding():
    navn = request.form["navn"]
    melding = request.form["melding"]
    meldinger.append({"navn": navn, "melding": melding})
    return redirect(url_for("gjestebok"))


# --- Spillere (MariaDB-database) ---

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
