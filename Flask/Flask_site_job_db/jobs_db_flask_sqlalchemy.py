from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def flask_init():
    app  = Flask(__name__)
    return app

def connect(app):
    app = app
    app.config['SQLALCHEMY_ECHO'] = True
    engine = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\Flask_Project1\\jobs.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    return db


def criar():
    # with app.app_context():
    #     db.create_all()
    #     print("Tabelas criada")
    pass

if __name__ == "__main__":
    pass 