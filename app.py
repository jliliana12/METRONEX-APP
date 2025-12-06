from flask import Flask, render_template
from flask import jsonify, request
from waitress import serve  # Opcional para pruebas locales

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

@app.route("/actualizar_estado")
def actualizar_estado():
    return render_template("actualizar_estado.html")

@app.route("/historial")
def historial():
    return render_template("historial.html")

@app.route("/alertas")
def alertas():
    return render_template("alertas.html")

@app.route("/informes")
def informes():
    return render_template("informes.html")

# Para pruebas locales (opcional)
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
