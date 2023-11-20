from flask import Flask
# flask-sqlalchemyの取り込み
from flask_sqlalchemy import SQLAlchemy
# flask-migrateの取り込み
from flask_migrate import Migrate
# flask-loginの取り込み
from flask_login import LoginManager

# sqlalchemyの定義
db = SQLAlchemy()
# migrateの定義
migrate = Migrate()
# loginの定義
login_manager = LoginManager()

# flaskのアプリケーション登録
def create_app(config_filename='config.py'):
    # アプリ名
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.config['DEBUG'] = True 
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    app.config['UPLOAD_FOLDER'] = 'project/static/prof_image'
    app.config['UPLOAD_FOLDER_TOREDO'] = 'project/static/toredo'
    app.config['UPLOAD_FOLDER_DEMOEXHIBIT'] = 'project/static/demo_toredo'
    app.config['UPLOAD_FOLDER_LOSTPET'] = 'project/static/lost_pet'
    app.config['UPLOAD_FOLDER_FOSTERPET'] = 'project/static/foster_pet'
    from project.models import T_User , T_Exhibit , T_Paramerter , T_Category , T_Favorite , T_Point , T_Cartlist , T_Pet

    @login_manager.user_loader
    def load_user(user_id):
        return T_User.query.get(int(user_id))

    from project.views import bp as main_bp
    app.register_blueprint(main_bp)

    return app
