from sqlalchemy.sql import text

class DBAnswer:
    def __init__(self, db):
        self.db = db
        
    def new(self, user_id, question_id, answer):
        sql = "INSERT \
                INTO answers (user_id, question_id, answer ) \
                VALUES (:user_id, :question_id, :answer);"
        self.db.session.execute( text(sql), {
                "question_id":question_id, 
                "user_id":user_id,
                "answer":answer
            } )
        self.db.session.commit()

    def get(self, user_id, question_id):
        sql = "SELECT answer \
            FROM answers \
            WHERE question_id = (:question_id) AND user_id = (:user_id);"
        result = self.db.session.execute( text(sql), { 
                'question_id': question_id,
                'user_id': user_id 
                } ).fetchone()
        return result[0] if result else -1


