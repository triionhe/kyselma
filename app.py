from flask import Flask
from os import getenv
from db_actions import db

app = Flask(__name__, static_url_path='')
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost/postgres"
db.init_app(app)

import routes
import nick