from app import app, db
from flask import render_template,session,request,redirect
from routes.tools import rows2dicts, get_alert, get_nick, csrf_check

@app.route("/pages/question.html")
def question():
    return render_template(
            "question.html",
            caller="create",
            alert=get_alert(),
            nick=get_nick()
        )

@app.route("/set/question",methods=["POST"])
def new_question():
    if csrf_check():
        return redirect("/#create")
    try:       
        question = request.form["question"]
        neg_ans = request.form["neg_ans"]
        pos_ans = request.form["pos_ans"]
        answer = int(request.form["answer"])
    except (KeyError, ValueError):
        session["alert"] = "Nyt kaikkea ei tullut perille tai jotain outoa."
        return redirect("/#question")

    try:
        sid = session["id"]
    except (KeyError):
        session["alert"] = "Nimimerkki puuttuukin."
        return redirect("/#create")
        
    try:
        qid = session["quiz_id"]
    except (KeyError):
        session["alert"] = "Kyselmän luonti ei ollutkaan kesken."
        return redirect("/#create")
        
    for entry in [question, neg_ans, pos_ans]:
        if len(entry.strip()) < 2 or len(entry.strip()) > 80:
            session["alert"] = "Syötteiden tulee olla 2-80 merkkiä pitkiä"
            return redirect("/#question")
            
    if answer < 0 or answer > 999:
        session["alert"] = "Vastauksessasi on nyt jotain häikkää."
        return redirect("/#question")

    question_id = db.question.new( question, neg_ans, pos_ans )
    db.quiz.add(qid, question_id)
    db.answer.new(sid, question_id, answer)        
    return redirect("/#create")

