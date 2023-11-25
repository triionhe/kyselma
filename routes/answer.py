from app import app
from flask import render_template, session, request, redirect
import db_actions as D
from routes.tools import rows2dicts, get_alert, get_nick, red


@app.route("/pages/new_answer.html")
def new_answer():
    if "id" not in session:
        return red["nick"]
    return render_template("new_answer.html", 
            alert=get_alert(),
            nick=get_nick()
        )

@app.route("/kys/<link>")
def kys_link(link):
    if aid := D.find_quiz_by_link( link ):
        session["answer_id"] = aid
        return redirect("/#answer")
    return redirect("/")

@app.route("/set/answer_id",methods=["POST"])
def answer_id():
    if "id" not in session:
        session["alert"] = "Nimimerkkiä ei ole asetettu."
        return redirect("/#nick")
    else:
        sid = session["id"]

    if "next" not in request.form:
        next = "/#answer"
    else:
        next = "/#"+request.form["next"]
    
    if "link" not in request.form or request.form["link"]=="":
        session["alert"] = "Kyselmän nimeä ei ole annettu."
        return redirect(next)
        
    if aid := D.find_quiz_by_link( request.form["link"] ):
        session["answer_id"] = aid
    else:
        session["alert"] = "Koodilla ei löytynyt kyselmää"
        return redirect(next)
        
    if next == "/#analyse" and not D.is_user_answered( aid, sid ):
        session["alert"] = "Et ole vielä vastannut tähän kyselmään. \
                            Voit tutkia vastaksia vastattuasi."
        return redirect("/#answer")

    return redirect( next )

@app.route("/pages/answer.html")
def answer():
    if "id" in session:
        sid = session["id"]
    else:
        return red["nick"]
        
    if "answer_id" in session:
        aid = session["answer_id"]
    else:
        return red["new_answer"]
        
    if D.is_user_answered(aid, sid):
        return red["new_answer"]
        
    return render_template("answer.html",
            alert = get_alert(),
            nick = get_nick(),
            questions = rows2dicts( D.get_questions(aid), ['i','q','n','p'] ),
            link = D.get_quiz_link( aid )
        )

@app.route("/set/answers",methods=["POST"])
def set_answers():
    if "id" not in session:
        session["alert"]="Nimimerkkiä ei ole vielä valittu!"
        return redirect( "/#nick" )
    if "answer_id" not in session:
        session["alert"]="Kyselyä ei ole valittu vastaamista varten!"
        return redirect( "/#answer" )

    sid = session["id"]
    for qid, answer in request.form.items():
        try: 
            if int(answer) < 0 or int(answer) > 999:
                session["alert"]="Luvattoman pieniä tai suuria lukuja!"
                return redirect( "/#answer" )
            elif D.get_user_answer(sid, int(qid) ):
                session["alert"]="Kyselyyn olikin jo saatu vastauksia."
                return redirect( "/#answer" )
        except ValueError:
            session["alert"] = "Vastaukset ei ole lukuja!"
            return redirect( "/#answer" )

    for qid, answer in request.form.items():
        D.answer_new(sid, int(qid), int(answer))

    return redirect("/#analyse")
