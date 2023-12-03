from app import app, D
from flask import render_template, session, request, redirect
from routes.tools import rows2dicts, get_alert, get_nick, csrf_check


@app.route("/kys/<link>")
def kys_link(link):
    if aid := D.find_quiz_by_link( link ):
        session["answer_id"] = aid
        return redirect("/#answer")
    return redirect("/")

@app.route("/set/answer_id",methods=["POST"])
def answer_id():
    next = "/#"+request.form["caller"] if "caller" in request.form else "/"
    if csrf_check():
        return redirect(next)
    if "id" not in session:
        session["alert"] = "Nimimerkkiä ei ole asetettu."
        return redirect(next)
    else:
        sid = session["id"]

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

    if next == "/#answer" and D.is_user_answered( aid, sid ):
        session["alert"] = "Olet jo vastannut valitsemaasi kyselyyn."
        return redirect("/#analyse")

    return redirect( next )

@app.route("/pages/answer.html")
def answer():
    if "id" in session:
        sid = session["id"]
    else:
        return render_template(
                "answer.html",
                caller = "answer",
                alert = get_alert()
            )
        
    if "answer_id" in session:
        aid = session["answer_id"]
    else:
        return render_template(
                "answer.html",
                caller = "answer",
                alert = get_alert(),
                nick = get_nick()
            )
        
    if D.is_user_answered(aid, sid):
        return render_template(
                "answer.html",
                caller = "answer",
                alert = get_alert(),
                nick = get_nick()
            )
        
    return render_template(
            "answer.html",
            caller = "answer",
            alert = get_alert(),
            nick = get_nick(),
            questions = rows2dicts( D.get_questions(aid), ['i','q','n','p'] ),
            link = D.get_quiz_link( aid )
        )

@app.route("/set/answers",methods=["POST"])
def set_answers():
    if csrf_check():
        return redirect("/#answer")
    if "id" not in session:
        session["alert"]="Nimimerkkiä ei ole vielä valittu!"
        return redirect( "/#answer" )
    if "answer_id" not in session:
        session["alert"]="Kyselyä ei ole valittu vastaamista varten!"
        return redirect( "/#answer" )

    sid = session["id"]
    for question, answer in request.form.items():
        if question=="csrf":
            continue
        try: 
            if int(answer) < 0 or int(answer) > 999:
                session["alert"]="Luvattoman pieniä tai suuria lukuja!"
                return redirect( "/#answer" )
            elif D.get_user_answer(int(sid), int(question)) != -1:
                session["alert"]="Kyselyyn olikin jo saatu vastauksia."
                return redirect( "/#answer" )
        except ValueError:
            session["alert"] = "Vastaukset ei ole lukuja!"
            return redirect( "/#answer" )

    for question, answer in request.form.items():
        if question=="csrf":
            continue
        D.answer_new(int(sid), int(question), int(answer))

    return redirect("/#analyse")
