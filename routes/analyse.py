from itertools import combinations
from app import app, db
from flask import render_template,session,request,redirect
from routes.tools import rows2dicts, get_alert, get_nick, csrf_check

def find_best_and_worst(aid, uid):
    match = {}
    comb = db.analyse.combinations(aid)
    if len(comb)<1:
        comb=[(uid,uid)]
    min, minme, max, maxme = 101, 101, -1, -1
    for pair in comb:
        match[pair] = int(db.analyse.compare(aid,pair[0],pair[1]))
        if match[pair] < min:
            min = match[pair]
            min_pair = pair
        if match[pair] > max:
            max = match[pair]
            max_pair = pair
        if pair[0]==uid or pair[1]==uid:
            if match[pair] < minme:
                minme = match[pair]
                minme_pair = pair
            if match[pair] > maxme:
                maxme = match[pair]
                maxme_pair = pair
    return ( { 
        'min': min, 'min_u1': min_pair[0], 'min_u2': min_pair[1],
        'max': max, 'max_u1': max_pair[0], 'max_u2': max_pair[1],
        'minme': minme, 'minme_u1': minme_pair[0], 'minme_u2': minme_pair[1],
        'maxme': maxme, 'maxme_u1': maxme_pair[0], 'maxme_u2': maxme_pair[1] })


@app.route("/pages/analyse.html")
def analyse():
    if "id" in session:
        sid = session["id"]
    else:
        return render_template(
                "analyse.html",
                caller="analyse",
                alert=get_alert()
            )

    if "answer_id" in session and db.quiz.user(session["answer_id"],sid):
        aid = session["answer_id"]
    else:
        return render_template(
                "analyse.html",
                caller="analyse",
                alert=get_alert(),
                nick=get_nick()
            )

    uid1 = session["anal_user1"] if "anal_user1" in session else sid
    uid1 = sid if uid1 != sid and not db.quiz.user(aid,uid1) else uid1

    uid2 = session["anal_user2"] if "anal_user2" in session else sid
    uid2 = sid if uid2 != sid and not db.quiz.user(aid,uid2) else uid2
    
    best = find_best_and_worst(aid, sid)
    
    if uid1 == uid2:
        uid1 = best['maxme_u1']
        uid2 = best['maxme_u2']


    return render_template(
            "analyse.html",
            caller="analyse",
            alert=get_alert(),
            nick=get_nick(),
            code=db.quiz.get_link(aid),
            questions = rows2dicts( db.analyse.pagedata( aid, uid1, uid2 ),
                    ['q','n','p','a1','a2','c'] ),
            users = rows2dicts( db.quiz.users(aid), ['id','nick'] ),
                user1=int(uid1),
                user2=int(uid2),
                avg = int(db.analyse.compare(aid,uid1,uid2)),
                best = best
        )

@app.route("/set/compare",methods=["POST"])
def set_compare():
    if csrf_check():
        return redirect("/#analyse")
    session["anal_user1"] = request.form["user1"]
    session["anal_user2"] = request.form["user2"]
    return redirect("/#analyse")
            
