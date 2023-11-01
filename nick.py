from app import app
from flask import render_template, session, request, redirect

@app.route("/nick",methods=["POST"])
def set_nick():
    nick = request.form["nick"]
    session["nick"] = nick
    return redirect("/")
    
    
