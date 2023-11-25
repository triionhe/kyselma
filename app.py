from flask import Flask
from os import getenv
from db_actions import db

app = Flask(__name__, static_url_path='')
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)

import routes.base
import routes.answer
import routes.create
import routes.analyse
import routes.question

