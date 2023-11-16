from time import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

db = SQLAlchemy()

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
    result = db.session.execute(text(sql), { "id":id }).fetchone()
    return result[0] if result else result

def user_exists(nick):
    sql = "SELECT COUNT(id) \
            FROM users \
            WHERE nick=(:nick);"
    return db.session.execute(text(sql), { "nick":nick }).scalar()

def question_new( question, neg_ans, pos_ans ):
    sql = "INSERT \
            INTO questions (question, neg_answer, pos_answer, created) \
            VALUES (:question, :neg_answer, :pos_answer, :created) \
            RETURNING id ;"
    result = db.session.execute(
            text(sql), { 
                    "question":question, 
                    "neg_answer":neg_ans,
                    "pos_answer":pos_ans,
                    "created":int(time()) }
        )
    db.session.commit()
    return result.fetchone()[0]

def quiz_new(user_id):
    sql = "INSERT \
            INTO questionaires (creator_id, created) \
            VALUES (:creator_id, :created) \
            RETURNING id ;"
    result = db.session.execute( text(sql),
        { "creator_id":user_id, "created":int(time()) } )
    db.session.commit()
    return result.fetchone()[0]

def quiz_add( quiz_id, question_id ):
    sql = "UPDATE questionaires \
            SET questionset = ARRAY_APPEND(questionset, :question_id) \
            WHERE id=:quiz_id;"
    db.session.execute(text(sql), {
            "quiz_id":quiz_id,
            "question_id":question_id
        })
    db.session.commit()
    
def answer_new(user_id, question_id, answer):
    sql = "INSERT \
            INTO answers (user_id, question_id,	answer,	created) \
            VALUES (:user_id, :question_id, :answer, :created);"
    db.session.execute( text(sql), {
            "user_id":user_id,
            "question_id":question_id, 
            "answer":answer,
            "created":int(time())
        } )
    db.session.commit()
