from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from app import app

from db.user import DBUser

class DB:
    def __init__(self):
        self.db = SQLAlchemy()
        self.db.init_app(app)
        self.user = DBUser(self.db)
        
    def question_new(self, question, neg_ans, pos_ans ):
        sql = "INSERT \
                INTO questions (question, neg_answer, pos_answer) \
                VALUES (:question, :neg_answer, :pos_answer) \
                RETURNING id ;"
        result = self.db.session.execute(
                text(sql), { 
                        "question":question, 
                        "neg_answer":neg_ans,
                        "pos_answer":pos_ans }
            )
        self.db.session.commit()
        return result.fetchone()[0]

    def quiz_new(self, user_id):
        sql = "INSERT \
                INTO questionaires (creator_id) \
                VALUES (:creator_id) \
                RETURNING id ;"
        result = self.db.session.execute( text(sql),
            { "creator_id":user_id } )
        self.db.session.commit()
        return result.fetchone()[0]

    def quiz_add(self, quiz_id, question_id ):
        sql = "UPDATE questionaires \
                SET questionset = ARRAY_APPEND(questionset, :question_id) \
                WHERE id=:quiz_id;"
        self.db.session.execute(text(sql), {
                "quiz_id":quiz_id,
                "question_id":question_id
            })
        self.db.session.commit()
    

    def set_quiz_link( self, quiz_id, link ):
        sql = "INSERT \
                INTO quiz_links (quiz_id, link) \
                VALUES (:quiz_id, :link)"
        result = self.db.session.execute( text(sql),
            {  "quiz_id":quiz_id, "link":link } )
        self.db.session.commit()


    def find_quiz_by_link( self, link ):
        sql = "SELECT quiz_id \
                FROM quiz_links \
                WHERE link=:link;"
        result = self.db.session.execute(text(sql), { "link":link }).fetchone()
        return result[0] if result else False


    def get_quiz_link( self, quiz_id ):
        sql = "SELECT link \
                FROM quiz_links \
                WHERE quiz_id=:quiz_id;"
        result = self.db.session.execute(text(sql), { "quiz_id":quiz_id }).fetchone()
        return result[0] if result else result

    
    def answer_new(self, user_id, question_id, answer):
        sql = "INSERT \
                INTO answers (user_id, question_id, answer ) \
                VALUES (:user_id, :question_id, :answer);"
        self.db.session.execute( text(sql), {
                "user_id":user_id,
                "question_id":question_id, 
                "answer":answer
            } )
        self.db.session.commit()


    def get_questions(self, quiz_id):
        sql = "SELECT q.id, q.question, q.neg_answer, q.pos_answer, a.answer \
                FROM questionaires quiz \
                JOIN questions q ON q.id = ANY(quiz.questionset) \
                JOIN answers a ON a.user_id = quiz.creator_id \
                WHERE a.question_id = q.id AND quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql), { "quiz_id":quiz_id } ).fetchall()

    def get_comparable(self, quiz_id,user1,user2):
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
        return self.db.session.execute( text(sql), {
                "quiz_id":quiz_id,
                "user1":user1,
                "user2":user2
            } ).fetchall()


    def get_user_answer(self, user_id, question_id):
        sql = "SELECT answer \
            FROM answers \
            WHERE question_id = (:question_id) AND user_id = (:user_id);"
        result = self.db.session.execute( text(sql), { 
                'question_id': question_id,
                'user_id': user_id 
                } ).fetchone()
        return result[0] if result else -1


    def get_user_answers_for_quiz(self, quiz_id, user_id):
        sql = "SELECT a.question_id, a.answer \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = ANY(quiz.questionset) \
                WHERE a.user_id = (:user_id) AND quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql), { 
                'user_id': user_id,
                'quiz_id': quiz_id
                } ).fetchall()

    def get_users_answered(self, quiz_id):
        sql = "SELECT DISTINCT a.user_id, u.nick \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = quiz.questionset[1] \
                JOIN users u ON u.id = a.user_id \
                WHERE quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id
                } ).fetchall()

    def is_user_answered(self, quiz_id, user_id):
        sql = "SELECT a.answer \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = quiz.questionset[1] \
                WHERE quiz.id = (:quiz_id) AND a.user_id = (:user_id);"
        results = self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id,
                'user_id': user_id
                } ).fetchone()
        return True if results else False


    def get_all_answers_for_quiz(self, quiz_id):
        sql = "SELECT a.question_id, a.user_id, a.answer \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = ANY(quiz.questionset) \
                WHERE quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id
                } ).fetchall()

    