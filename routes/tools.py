from random import randint
from flask import session
import db_actions as D

def rows2dicts( rows, names ):
    dlist=[]
    for i in range(len(rows)):
        row={}
        for j in range(len(names)):
            row[names[j]]=rows[i][j]
        dlist.append(row)
    return dlist

def get_alert():
    if "alert" in session:
        alert = session["alert"]
        del session["alert"]
        return f"{alert}"
    return ""
    
def get_nick():
    while "id" in session.keys():
        nick = D.user_get_nick(session["id"])
        if not nick:
            del session['id']
            if "quiz_id" in session.keys():
                del session['quiz_id']
            break
        return nick
    return "(ei nimimerkkiä)"

def generate_link():
    konso="rtpshjklvnm"
    vocal="eyuioa"
    str=""
    for i in range(4):
        str+=konso[randint(0,len(konso)-1)]
        str+=vocal[randint(0,len(vocal)-1)]
    return str

def csrf_check( redir )
    if "csrf" not in session 
            or "csrf" not in request.form
            of session["csrf"]!=request.form["csrf"]:
        session["alert"]="Istuntosi katkesi tai pyyntö toiselta sivulta!"
        return redirect( redir )
