from app import app
from flask import render_template,session,request,redirect
import db_actions as D
from routes.tools import rows2dicts, get_alert, get_nick, red

@app.route("/pages/analyse.html")
def analyse():
    if "id" in session:
        sid = session["id"]
    else:
        return red["nick"]

    if "answer_id" in session and D.is_user_answered(session["answer_id"],sid):
        aid = session["answer_id"]
    else:
        return render_template("analyse.html",
                alert=get_alert(),
                nick=get_nick()
            )

    uid1 = session["anal_user1"] if "anal_user1" in session else sid
    uid1 = sid if uid1 != sid and not D.is_user_answered(aid,uid1) else uid1

    uid2 = session["anal_user2"] if "anal_user2" in session else sid
    uid2 = sid if uid2 != sid and not D.is_user_answered(aid,uid2) else uid2

    comparable = D.get_comparable( aid, uid1, uid2 )
    avg=0
    for i in range(len(comparable)):
        avg += comparable[i][5]
    avg//=len(comparable)
    

    return render_template("analyse.html",
            alert=get_alert(),
            nick=get_nick(),
            code=D.get_quiz_link(aid),
            questions = rows2dicts( comparable, ['q','n','p','a1','a2','c'] ),
            users = rows2dicts( D.get_users_answered(aid), ['id','nick'] ),
                user1=int(uid1),
                user2=int(uid2),
                avg = avg
        )

@app.route("/set/compare",methods=["POST"])
def set_compare():
    session["anal_user1"] = request.form["user1"]
    session["anal_user2"] = request.form["user2"]
    return redirect("/#analyse")
            
