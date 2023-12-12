from secrets import token_urlsafe
from app import app, db
from flask import render_template,session,request,redirect
from routes.tools import rows2dicts, get_alert, get_nick, csrf_check

@app.route("/")
def index():
    session["csrf"] = token_urlsafe()
    return app.send_static_file("index.html")

@app.route("/pages/info.html")
def info():
    if "id" in session:
        return render_template(
                "info.html",
                caller="info",
                alert=get_alert(),
                nick=get_nick()
            )
    return render_template(
            "info.html",
            caller="info",
            alert=get_alert()
        )
        
@app.route("/pages/nick_reset.html")
def nick_reset():
    if "id" in session:
        return render_template(
                "nick_reset.html",
                caller="info",
                nick=get_nick()
            )
    return redirect("/")
        
@app.route("/set/nick",methods=["POST"])
def new_nick():
    next = "/#"+request.form["caller"] if "caller" in request.form else "/"
    if csrf_check():
        return redirect(next)
    if "id" in session.keys() and "reset" not in request.form:
        session["alert"]="Sinulla on jo nimimerkki. Käytä sitä."
        return redirect(next)
    if "nick" not in request.form or request.form["nick"]=="":
        session["alert"]="Nimimerkkiä ei voi asettaa ilman nimimerkkiä."
        return redirect(next)
    else:
        nick = request.form["nick"]
    if len(nick) < 4:
        session["alert"]="Nimimerkki on liian lyhyt"
        return redirect(next)
    if not nick.isalnum():
        session["alert"]="Nimimerkissä saa olla vain kirjaimia ja numeroita."
        return redirect(next)
    if db.user.exists(nick):
        session["alert"]="Nimimerkki jonka olet ottamassa on jo varattu."
        return redirect(next)
    session["id"] = int(db.user.new(nick))
    return redirect(next)


