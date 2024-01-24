SECRET_KEY = '@lphaCoffee15' # session secrete key

def config_sqlalchemy(app,echo ,modifications):
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\flask_project2\\app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = modifications
