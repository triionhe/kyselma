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
