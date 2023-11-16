from app import app
from flask import render_template, session, request, redirect
import db_actions as D


@app.route("/new_quiz",methods=["POST"])
def new_quiz():
    if not "id" in session.keys():
        session["alert"]="Tarvitset nimimerkin loudaksesi"
        return redirect("/#nick")
    user_id = session["id"]
    session["quiz_id"] = D.quiz_new( user_id )
    return redirect("/#create")
