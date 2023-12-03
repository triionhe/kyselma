from sqlalchemy.sql import text

class DBAnalyse:
    def __init__(self, db):
        self.db = db
        
    def pagedata(self, quiz_id,user1,user2):
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
            
    def compare(self, quiz_id,user1,user2):
        sql = "SELECT \
                AVG (100 - ABS( a1.answer - a2.answer ) / 10 ) \
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
            } ).scalar()
        
        
    def combinations(self, quiz_id):
        sql = "SELECT u1.id, u2.id \
                FROM questionaires quiz \
                JOIN answers a1 ON a1.question_id = quiz.questionset[1] \
                JOIN answers a2 ON a2.question_id = quiz.questionset[1] \
                JOIN users u1 ON u1.id = a1.user_id \
                JOIN users u2 ON u2.id = a2.user_id \
                WHERE quiz.id = (:quiz_id) AND u1.id > u2.id;"
        return self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id
                } ).fetchall()

