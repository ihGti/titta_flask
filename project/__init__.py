from flask import Flask , request , current_app
# flask-sqlalchemyの取り込み
from flask_sqlalchemy import SQLAlchemy
# flask-migrateの取り込み
from flask_migrate import Migrate

from flask_login import LoginManager

from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

from flask_socketio import SocketIO

import os
# sqlalchemyの定義
db = SQLAlchemy()
# migrateの定義
migrate = Migrate()
    # loginの定義
login_manager = LoginManager()
# adminの定義
admin = Admin()
# socketioの定義
socketio = SocketIO()




# flaskのアプリケーション登録
def create_app(config_filename='config.py'):
    # アプリ名
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.config['DEBUG'] = True 
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)
    socketio.init_app(app)
    app.config['UPLOAD_FOLDER'] = 'project/static/prof_image'
    app.config['UPLOAD_FOLDER_TOREDO'] = 'project/static/toredo'
    app.config['UPLOAD_FOLDER_DEMOEXHIBIT'] = 'project/static/demo_toredo'
    app.config['UPLOAD_FOLDER_LOSTPET'] = 'project/static/lost_pet'
    app.config['UPLOAD_FOLDER_FOSTERPET'] = 'project/static/foster_pet'
    app.config['UPLOAD_FOLDER_CHAT'] = 'project/static/chat_image'
    app.config['UPLOAD_FOLDER_CONTEST_MASTER'] = 'project/static/master'
    app.config['UPLOAD_FOLDER_CONTEST'] = 'project/static/contest'

    from project.models import T_User , T_Cartlist , T_Category , T_Chat , T_Contest , T_Exhibit , T_Favorite , T_FosterPet , T_LostPet , T_Paramerter , T_Pet , T_Point , T_UserReview , T_ContestMaster , T_Coupon , T_CouponPos , T_Message
    @login_manager.user_loader
    def load_user(user_id):
        return T_User.query.get(int(user_id))
    # adminページ
    admin.add_view(ModelView(T_User,db.session))
    admin.add_view(ModelView(T_Cartlist,db.session))
    admin.add_view(ModelView(T_Category,db.session))
    admin.add_view(ModelView(T_Chat,db.session))
    admin.add_view(ModelView(T_Contest,db.session))
    admin.add_view(ModelView(T_Exhibit,db.session))
    admin.add_view(ModelView(T_Pet,db.session))
    admin.add_view(ModelView(T_LostPet,db.session))
    admin.add_view(ModelView(T_FosterPet,db.session))
    admin.add_view(ModelView(T_Favorite,db.session))
    admin.add_view(ModelView(T_Paramerter,db.session))
    admin.add_view(ModelView(T_Point,db.session))
    admin.add_view(ModelView(T_UserReview,db.session))
    admin.add_view(ModelView(T_ContestMaster,db.session))
    admin.add_view(ModelView(T_Coupon,db.session))
    admin.add_view(ModelView(T_CouponPos,db.session))
    admin.add_view(ModelView(T_Message,db.session))
    from project.views import bp as main_bp
    app.register_blueprint(main_bp)

    return app
