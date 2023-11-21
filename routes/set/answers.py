from app import app
from flask import render_template, session, request, redirect
import db_actions as D

def validate_answer(ans):
    if len(ans)<1:
        return False
    try:
        value=int(ans)
        if value<0 or value>1000:
            return False
    except ValueError:
        return False        
    return True
    
@app.route("/set/answers",methods=["POST"])
def set_answers():
    if "id" not in session.keys():
        return "KUOLETTAVA: Nimimerkkiä ei ole vielä valittu!"
    if "quiz_id" not in session.keys():
        return "KUOLETTAVA: Yrität vastata kyselyyn ilman sen valintaa!"

    user_id = session["id"]
    for id, answer in request.form.items():
        question_id = int(id)
        if not validate_answer(answer):
            return "KUOLETTAVA: Epäkelpo vastaus!"
        if D.get_user_answer(user_id,question_id):
            return "KUOLETTAVA: On jo vastattu!"
        D.answer_new(user_id, question_id, answer)

    return redirect("/#analyse")
