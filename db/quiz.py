from sqlalchemy.sql import text

class DBQuiz:
    def __init__(self, db):
        self.db = db
        
    def new(self, user_id):
        sql = "INSERT \
                INTO questionaires (creator_id) \
                VALUES (:creator_id) \
                RETURNING id ;"
        result = self.db.session.execute( text(sql),
            { "creator_id":user_id } )
        self.db.session.commit()
        return result.fetchone()[0]


    def add(self, quiz_id, question_id ):
        sql = "UPDATE questionaires \
                SET questionset = ARRAY_APPEND(questionset, :question_id) \
                WHERE id=:quiz_id;"
        self.db.session.execute(text(sql), {
                "quiz_id":quiz_id,
                "question_id":question_id
            })
        self.db.session.commit()
    

    def set_link( self, quiz_id, link ):
        sql = "INSERT \
                INTO quiz_links (quiz_id, link) \
                VALUES (:quiz_id, :link)"
        result = self.db.session.execute( text(sql),
            {  "quiz_id":quiz_id, "link":link } )
        self.db.session.commit()


    def find_by_link( self, link ):
        sql = "SELECT quiz_id \
                FROM quiz_links \
                WHERE link=:link;"
        result = self.db.session.execute(text(sql), { "link":link }).fetchone()
        return result[0] if result else False


    def get_link( self, quiz_id ):
        sql = "SELECT link \
                FROM quiz_links \
                WHERE quiz_id=:quiz_id;"
        result = self.db.session.execute(text(sql), 
                { "quiz_id":quiz_id }).fetchone()
        return result[0] if result else result


    def questions(self, quiz_id):
        sql = "SELECT q.id, q.question, q.neg_answer, q.pos_answer, a.answer \
                FROM questionaires quiz \
                JOIN questions q ON q.id = ANY(quiz.questionset) \
                JOIN answers a ON a.user_id = quiz.creator_id \
                WHERE a.question_id = q.id AND quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql),
                { "quiz_id":quiz_id } ).fetchall()

    def answers(self, quiz_id):
        sql = "SELECT a.question_id, a.user_id, a.answer \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = ANY(quiz.questionset) \
                WHERE quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id
                } ).fetchall()


    def users(self, quiz_id):
        sql = "SELECT DISTINCT a.user_id, u.nick \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = quiz.questionset[1] \
                JOIN users u ON u.id = a.user_id \
                WHERE quiz.id = (:quiz_id);"
        return self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id
                } ).fetchall()

    def user(self, quiz_id, user_id):
        sql = "SELECT a.answer \
                FROM questionaires quiz \
                JOIN answers a ON a.question_id = quiz.questionset[1] \
                WHERE quiz.id = (:quiz_id) AND a.user_id = (:user_id);"
        results = self.db.session.execute( text(sql), { 
                'quiz_id': quiz_id,
                'user_id': user_id
                } ).fetchone()
        return True if results else False

