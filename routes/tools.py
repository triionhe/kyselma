from random import randint
from flask import session
import db_actions as D

red = {
    "nick": "<script>window.location.hash=\"nick\"</script>",
    "new_answer": "<script>window.location.hash=\"new_answer\"</script>",
    "quiz": "<script>window.location.hash=\"quiz\"</script>"
}


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
