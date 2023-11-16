from app import app
from flask import render_template,session
import db_actions as D

def get_alert():
    if "alert" in session:
        alert = session["alert"]
        del session["alert"]
        return f"{alert}"
    return ""
    
def get_nick():
    while "id" in session.keys():
        nick = D.user_get_nick(session["id"])
        if not nick:
            del session['id']
            if "quiz_id" in session.keys():
                del session['quiz_id']
            break
        return nick
    return "(ei nimimerkkiä)"

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/pages/info.html")
def info():
    return render_template("info.html",
            alert=get_alert()
        )

@app.route("/pages/create.html")
def create():
    if "id" not in session.keys():
        return "redirect = #nick"
    if "quiz_id" not in session.keys():
        return "redirect = #quiz"
    return render_template("create.html", 
            alert=get_alert(),
            nick=get_nick()
        )

@app.route("/pages/answer.html")
def answer():
    if "id" not in session.keys():
        return "redirect = #nick"
    return render_template("answer.html", 
            alert=get_alert(),
            nick=get_nick()
        )

@app.route("/pages/analyse.html")
def analyse():
    if "id" not in session.keys():
        return "redirect = #nick"
    return render_template("analyse.html",
            alert=get_alert(),
            nick=get_nick()
        )

@app.route("/pages/moderate.html")
def moderate():
    return render_template("moderate.html",
            alert=get_alert()
        )

@app.route("/pages/nick.html")
def nick():
    return render_template("nick.html", alert=get_alert() )

@app.route("/pages/question.html")
def question():
    return render_template("question.html", alert=get_alert() )

@app.route("/pages/quiz.html")
def build():
    return render_template("quiz.html", alert=get_alert() )
