from app import app
from flask import render_template, session, request, redirect
import db_actions as D


@app.route("/new_nick",methods=["POST"])
def new_nick():
    nick = request.form["nick"]
    if "id" in session.keys():
        msg = "You already have a nick."
    elif D.user_exists(nick):
        msg = "Nick is already reserved."
    elif msg := invalid_nick(nick):
        pass
    else:
        session["id"] = D.user_new(nick)
        return redirect("/")
    session["alert"]="Nick in not created: "+msg
    return redirect("/#nick")


def invalid_nick(nick):
    if len(nick)<4:
        return "Nick is too short"
    if not nick.isalnum():
        return "Only letters and numbers are allowed"
    return 0
    