from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_sqlalchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
config_sqlalchemy(app,True,False)

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug = True)  