from app import app
from flask import render_template,session

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/pages/info.html")
def info():
    return render_template("info.html")

@app.route("/pages/create.html")
def create():
    if "nick" not in session:
        return render_template("nick.html")
    return render_template("create.html")

@app.route("/pages/answer.html")
def answer():
    if "nick" not in session:
        return render_template("nick.html")
    return render_template("answer.html")

@app.route("/pages/analyse.html")
def analyse():
    return render_template("analyse.html")

@app.route("/pages/moderate.html")
def moderate():
    return render_template("moderate.html")
