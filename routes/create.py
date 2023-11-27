from app import app
from flask import render_template,session,request,redirect
import db_actions as D
from routes.tools import rows2dicts, get_alert, get_nick, generate_link, csrf_check


@app.route("/pages/create.html")
def create():
    if "id" not in session:
        return render_template(
                "create.html",
                caller="create",
                alert=get_alert()
            )
    if "quiz_id" not in session:
        return render_template(
                "create.html",
                caller="create",
                alert=get_alert(),
                nick=get_nick()
            )
    if D.get_quiz_link(session["quiz_id"]):
        return render_template(
                "create.html",
                caller="create",
                alert=get_alert(),
                nick=get_nick()
            )

    return render_template(
            "create.html", 
            caller="create",
            alert=get_alert(),
            nick=get_nick(),
            quiz_set=True,
            questions=rows2dicts(
                D.get_questions(session["quiz_id"]),
                ['i','q','n','p','a']
            )
        )

@app.route("/set/quiz",methods=["POST"])
def new_quiz():
    if csrf_check():
        return redirect("/#create")
    if not "id" in session.keys():
        session["alert"]="Tarvitset nimimerkin loudaksesi."
        return redirect("/#create")
    user_id = session["id"]
    session["quiz_id"] = D.quiz_new( user_id )
    return redirect("/#create")


@app.route("/set/quiz_ready",methods=["POST"])
def quiz_ready():
    if csrf_check():
        return redirect("/#create")
    if "quiz_id" not in session.keys():
        session["alert"] = "Kyselmä jota ei ole aloitettu ei voi olla valmis."
        return redirect("/#create")
    if not D.is_user_answered(session["quiz_id"], session["id"]):
        session["alert"] = "Tyhjän kyselmän luominen ei käy päinsä!"
        return redirect("/#create")
    quiz_id = session["quiz_id"]
    session["answer_id"] = session["quiz_id"]
    D.set_quiz_link(session["quiz_id"], generate_link())
    return redirect("/#analyse")
