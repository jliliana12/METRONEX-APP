import os
from flask import Flask, render_template, request, redirect, url_for
from database import init_db, create_equipo, get_all, update_estado

app = Flask(__name__)
app.config.from_mapping({
    "SECRET_KEY": os.environ.get("SECRET_KEY", "clave-segura-local")
})


@app.route("/")
def index():
    equipos = get_all()
    return render_template("index.html", equipos=equipos)


@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        tipo = request.form.get("tipo")
        modelo = request.form.get("modelo")
        create_equipo(tipo, modelo, "Recibido")
        return redirect(url_for("index"))
    return render_template("registrar.html")


@app.route("/actualizar_estado/<int:id>", methods=["GET", "POST"])
def actualizar_estado(id):
    if request.method == "POST":
        nuevo = request.form.get("estado")
        update_estado(id, nuevo)
        return redirect(url_for("historial"))
    return render_template("actualizar_estado.html", id=id)


@app.route("/historial")
def historial():
    equipos = get_all()
    return render_template("historial.html", equipos=equipos)


@app.route("/alertas")
def alertas():
    equipos = get_all()
    return render_template("alertas.html", equipos=equipos)


@app.route("/informes")
def informes():
    equipos = get_all()
    return render_template("informes.html", equipos=equipos)


# Inicializar BD
init_db()


# ✔ Corrección para Render (sin gunicorn)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
