from app import app
from flask import render_template, session, request, redirect
import db_actions as D


def validate_answer(ans):
    if len(ans)<1:
        return False
    return True
    
def validate_question(question):
    if len(question)<2:
        return False
    return True

@app.route("/set/question",methods=["POST"])
def new_question():
    question = request.form["question"]
    neg_ans = request.form["neg_ans"]
    pos_ans = request.form["pos_ans"]
    answer = request.form["answer"]
    if not validate_question(question):
        msg = "Kysymys on virheellinen"
    elif not validate_answer(neg_ans):
        msg = "Vasen selite on virheellinen"
    elif not validate_answer(pos_ans):
        msg = "Oikea selite on virheellinen"
    elif "id" not in session.keys():
        msg = "Tarvitaan nimimerkki"
    elif "quiz_id" not in session.keys():
        msg = "Ei voi lisätä kysymystä ilman kyselmää"
    else:
        quiz_id = session["quiz_id"]
        user_id = session["id"]
        question_id = D.question_new( question, neg_ans, pos_ans )
        D.quiz_add(quiz_id, question_id)
        D.answer_new(user_id, question_id, answer)        
        return redirect("/#create")
    session["alert"]="Kysymystä ei luotu: "+msg
    return redirect("/#create")
