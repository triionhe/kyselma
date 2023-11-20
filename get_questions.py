from app import app
from flask import render_template, session, request, redirect, jsonify
import db_actions as D


@app.route("/get_questions",methods=["GET"])
def get_questions_by_id():
    if "quiz_id" not in session.keys():
        return "KUOLETTAVA: Sessiota / kyselmä id:tä ei ole"

    results = D.get_questions(session['quiz_id'])
    r={}
    names=['i','q','n','p','a']
    for i in range(len(results)):
        r[i]={}
        for j in range(len(results[i])):
            r[i][names[j]]=results[i][j]
    return (jsonify(r))
