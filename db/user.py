from sqlalchemy.sql import text

class DBUser:
    def __init__(self, db):
        self.db = db
        
    def get_nick(self, id):
        sql = "SELECT nick \
                FROM users \
                WHERE id=(:id);"
        result = self.db.session.execute(text(sql), { "id":id }).fetchone()
        return result[0] if result else result

    def new(self, nick):
        sql = "INSERT \
                INTO users (nick) \
                VALUES (:nick) \
                RETURNING id ;"
        result = self.db.session.execute( text(sql), { "nick":nick } )
        self.db.session.commit()
        return result.fetchone()[0]

    def exists(self, nick):
        sql = "SELECT COUNT(id) \
                FROM users \
                WHERE nick=(:nick);"
        return self.db.session.execute(text(sql), { "nick":nick }).scalar()

