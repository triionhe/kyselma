from time import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import text

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def user_new(nick):
    sql = "INSERT \
            INTO users (nick, created) \
            VALUES (:nick, :created) \
            RETURNING id ;"
    result = db.session.execute(
            text(sql), { "nick":nick, "created":int(time()) }
        )
    db.session.commit()
    return result.fetchone()[0]

def user_get_nick(id):
    sql = "SELECT nick \
            FROM users \
            WHERE id=(:id);"
    return db.session.execute(text(sql), { "id":id }).fetchone()[0]

def user_exists(nick):
    sql = "SELECT COUNT(id) \
            FROM users \
            WHERE nick=(:nick);"
    return db.session.execute(text(sql), { "nick":nick }).scalar()
