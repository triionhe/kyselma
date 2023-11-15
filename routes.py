from app import app
from flask import render_template,session

def get_alert():
    if "alert" in session:
        alert = session["alert"]
        del session["alert"]
        return f"{alert}"
    return ""

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/pages/info.html")
def info():
    return render_template("info.html", alert=get_alert() )

@app.route("/pages/create.html")
def create():
    if "id" not in session:
        return "redirect = #nick"
    return render_template("create.html", alert=get_alert() )

@app.route("/pages/answer.html")
def answer():
    if "id" not in session:
        return "redirect = #nick"
    return render_template("answer.html", alert=get_alert() )

@app.route("/pages/analyse.html")
def analyse():
    if "id" not in session:
        return "redirect = #nick"
    return render_template("analyse.html", alert=get_alert() )

@app.route("/pages/moderate.html")
def moderate():
    return render_template("moderate.html", alert=get_alert() )

@app.route("/pages/nick.html")
def nick():
    return render_template("nick.html", alert=get_alert() )
