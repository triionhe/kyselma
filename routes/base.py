from app import app
from flask import render_template,session,request,redirect
import db_actions as D
from routes.tools import rows2dicts, get_alert, get_nick

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/pages/info.html")
def info():
    return render_template("info.html",
            alert=get_alert()
        )
        
@app.route("/pages/nick.html")
def nick():
    return render_template("nick.html",
            alert=get_alert()
        )

@app.route("/set/nick",methods=["POST"])
def new_nick():
    if "id" in session.keys():
        session["alert"]="Sinulla on jo nimimerkki. Käytä sitä."
        return redirect("/")
    if "nick" not in request.form or request.form["nick"]=="":
        session["alert"]="Nimimerkkiä ei voi asettaa ilman nimimerkkiä."
        return redirect("/#nick")
    else:
        nick = request.form["nick"]
    if len(nick) < 4:
        session["alert"]="Nimimerkki on liian lyhyt"
        return redirect("/#nick")
    if not nick.isalnum():
        session["alert"]="Nimimerkissä saa olla vain kirjaimia ja numeroita."
        return redirect("/#nick")
    if D.user_exists(nick):
        session["alert"]="Nimimerkki jonka olet ottamassa on jo varattu."
        return redirect("/#nick")
    session["id"] = D.user_new(nick)
    return redirect("/")



#@app.route("/pages/moderate.html")
#def moderate():
#    return render_template("moderate.html",
#            alert=get_alert()
#        )

