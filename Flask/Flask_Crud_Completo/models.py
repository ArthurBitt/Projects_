from app import db, app


with app.app_context():

    class Jogo(db.Model):
            __tablename__ = 'Jogo'
            id = db.Column(db.Integer, primary_key = True, autoincrement = True)
            jogo = db.Column(db.String)
            categoria = db.Column(db.String)
            console = db.Column(db.String)

    class User(db.Model):
        __tablename__ = 'User'
        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        nome = db.Column(db.String)
        nickname = db.Column(db.String(15))
        senha = db.Column(db.String(20))

