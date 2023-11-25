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
    

def set_quiz_link( quiz_id, link ):
    sql = "INSERT \
            INTO quiz_links (quiz_id, link, created) \
            VALUES (:quiz_id, :link, :created)"
    result = db.session.execute( text(sql),
        {  "quiz_id":quiz_id, "link":link, "created":int(time()) } )
    db.session.commit()
    

def find_quiz_by_link( link ):
    sql = "SELECT quiz_id \
            FROM quiz_links \
            WHERE link=:link;"
    result = db.session.execute(text(sql), { "link":link }).fetchone()
    return result[0] if result else result


def get_quiz_link( quiz_id ):
    sql = "SELECT link \
            FROM quiz_links \
            WHERE quiz_id=:quiz_id;"
    result = db.session.execute(text(sql), { "quiz_id":quiz_id }).fetchone()
    return result[0] if result else result

    
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


def get_questions(quiz_id):
    sql = "SELECT q.id, q.question, q.neg_answer, q.pos_answer, a.answer \
            FROM questionaires quiz \
            JOIN questions q ON q.id = ANY(quiz.questionset) \
            JOIN answers a ON a.user_id = quiz.creator_id \
            WHERE a.question_id = q.id AND quiz.id = (:quiz_id);"
    return db.session.execute( text(sql), { "quiz_id":quiz_id } ).fetchall()

def get_comparable(quiz_id,user1,user2):
    sql = "SELECT q.question, q.neg_answer, q.pos_answer, \
            a1.answer, a2.answer, \
            100 - ABS( a1.answer - a2.answer ) / 10 \
            FROM questionaires quiz \
            JOIN questions q ON q.id = ANY(quiz.questionset) \
            JOIN answers a1 ON a1.user_id = (:user1) \
            JOIN answers a2 ON a2.user_id = (:user2) \
            WHERE a1.question_id = q.id \
            AND a2.question_id = q.id \
            AND quiz.id = (:quiz_id);"
    return db.session.execute( text(sql), {
            "quiz_id":quiz_id,
            "user1":user1,
            "user2":user2
        } ).fetchall()


def get_user_answer(user_id, question_id):
    sql = "SELECT answer \
        FROM answers \
        WHERE question_id = (:question_id)  AND user_id = (:user_id);"
    result = db.session.execute( text(sql), { 
            'question_id': question_id,
            'user_id': user_id 
            } ).fetchone()
    return result[0] if result else result


def get_user_answers_for_quiz(quiz_id, user_id):
    sql = "SELECT a.question_id, a.answer \
            FROM questionaires quiz \
            JOIN answers a ON a.question_id = ANY(quiz.questionset) \
            WHERE a.user_id = (:user_id) AND quiz.id = (:quiz_id);"
    return db.session.execute( text(sql), { 
            'user_id': user_id,
            'quiz_id': quiz_id
            } ).fetchall()

def get_users_answered(quiz_id):
    sql = "SELECT DISTINCT a.user_id, u.nick \
            FROM questionaires quiz \
            JOIN answers a ON a.question_id = quiz.questionset[1] \
            JOIN users u ON u.id = a.user_id \
            WHERE quiz.id = (:quiz_id);"
    return db.session.execute( text(sql), { 
            'quiz_id': quiz_id
            } ).fetchall()

def is_user_answered(quiz_id, user_id):
    sql = "SELECT a.answer \
            FROM questionaires quiz \
            JOIN answers a ON a.question_id = quiz.questionset[1] \
            WHERE quiz.id = (:quiz_id) AND a.user_id = (:user_id);"
    results = db.session.execute( text(sql), { 
            'quiz_id': quiz_id,
            'user_id': user_id
            } ).fetchone()
    return results[0] if results else results
