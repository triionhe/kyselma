from flask_sqlalchemy import SQLAlchemy

from app import app

from db.user import DBUser
from db.quiz import DBQuiz
from db.question import DBQuestion
from db.answer import DBAnswer
from db.analyse import DBAnalyse

class DB:
    def __init__(self):
        self.db = SQLAlchemy()
        self.db.init_app(app)

        self.user = DBUser(self.db)
        self.quiz = DBQuiz(self.db)
        self.question = DBQuestion(self.db)
        self.answer = DBAnswer(self.db)
        self.analyse = DBAnalyse(self.db)
    