from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash
from project import db

# T_Userクラス
class T_User(db.Model,UserMixin):
    F_UserID = db.Column(db.Integer, primary_key=True)
    
    F_UserName = db.Column(db.String(40), unique=True, nullable=False)
    
    F_Password = db.Column(db.String(256), nullable=False)
    
    F_SignUpDay = db.Column(db.DateTime, default = datetime.utcnow)
    
    F_BirthDay = db.Column(db.DateTime, default = datetime.utcnow)
    
    F_Gender = db.Column(db.String(10), nullable=True)
    
    F_Telphone = db.Column(db.String(16), nullable=False)
    
    F_Email = db.Column(db.String(256), nullable=False)
    
    F_Residence = db.Column(db.String(256), nullable=False)
    
    F_PosttalCode = db.Column(db.String(256), nullable=False)
    
    F_LastName = db.Column(db.String(256), nullable=False)
    
    F_FirstName = db.Column(db.String(256), nullable=False)
    
    F_LastName_Kana = db.Column(db.String(256), nullable=False)
    
    F_FirstName_Kana = db.Column(db.String(256), nullable=False)
    
    F_ProfileImage = db.Column(db.String(256), nullable=False)


class T_Tore_do(db.Model):
    
    F_ExID = db.Column(db.Integer, primary_key=True)
    
    F_ExTitle = db.Column(db.String(256), unique=True ,nullable=False)
    
    F_ExPrice = db.Column(db.Integer, nullable=False)
    
    F_ExInfo = db.Column(db.String(256), nullable=False)
    
    F_ExPhoto = db.Column(db.String(256), nullable=False)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('T_User.F_UserID'), nullable=False)
    
    
