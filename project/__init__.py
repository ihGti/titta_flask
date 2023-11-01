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

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from project.models import T_User

    @login_manager.user_loader
    def load_user(user_id):
        return T_User.query.get(int(user_id))

    from project.views import bp as main_bp
    app.register_blueprint(main_bp)

    return app
