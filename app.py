from secrets import token_hex
from flask import Flask
from os import getenv

app = Flask(__name__, static_url_path='')

if db_uri := getenv("SQLALCHEMY_DATABASE_URI"):
    app.config["SQLALCHEMY_DATABASE_URI"]=db_uri
else:
    app.config["SQLALCHEMY_DATABASE_URI"]="postgresql:///"
    
if s_key := getenv("SECRET_KEY"):
    app.secret_key = s_key
else:
    app.secret_key = token_hex()
    
from db.db import DB
db = DB()
    
import routes.base
import routes.answer
import routes.create
import routes.analyse
import routes.question
