from sqlalchemy.sql import text

class DBQuestion:
    def __init__(self, db):
        self.db = db
        
    def new(self, question, neg_ans, pos_ans ):
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

