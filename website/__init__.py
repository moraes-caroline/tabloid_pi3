from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# iniciando o banco de dados
db = SQLAlchemy()

DB_NAME = "database.db" # para o sqlite
DB_POSTGRES = "dbqhkl5cujq3q7"
USER = 'ovybufamtcbrav'
PASSWORD = 'd3601440e22f02078db17ef7c5fdd2cbaffccabcc9b70de2fe5916a4bc3a1544'
HOST = 'ec2-18-204-142-254.compute-1.amazonaws.com'

def create_app():
    app = Flask(__name__)
 #Sqlite configuração
    app.config['SECRET_KEY'] = 'grhteyeuwhhs fgdhjajakuww'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
 #Postgres
 #   app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DB_POSTGRES}'
    db.init_app(app)



    from .views import views
    from .auth import auth
    from .api.usuarios import api
    from  .api.produtos import api
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/' )
    
    

    from .models import User, Comercios_items, Estabelecimentos, Servicos, Segmentos
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    return app
def create_database(app):
    db.create_all(app=app)
    if not path.exists('website/' + DB_NAME):
       db.create_all(app=app)
       print('Created Database')

    