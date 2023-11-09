from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_filename='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.config['DEBUG'] = True 
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    app.config['UPLOAD_FOLDER'] = 'project/static/prof_image'
    app.config['UPLOAD_FOLDER_EXHIBIT'] = 'project/static/exhibit'
    app.config['UPLOAD_FOLDER_DEMOEXHIBIT'] = 'project/static/demo_exhibit'
    from project.models import T_User , T_Exhibit , T_Paramerter

    @login_manager.user_loader
    def load_user(user_id):
        return T_User.query.get(int(user_id))

    from project.views import bp as main_bp
    app.register_blueprint(main_bp)

    return app
