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
    
    F_BirthDay = db.Column(db.Date, nullable=False)
    
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
    
    F_Profile_Comment = db.Column(db.String(256), nullable=True)
    
    images = db.relationship('T_Exhibit', backref='user',lazy=True)
    
    def get_id(self):
        return str(self.F_UserID)
    

class T_Exhibit(db.Model):
    
    F_ExID = db.Column(db.Integer, primary_key=True)
    
    F_ExTitle = db.Column(db.String(256), unique=True ,nullable=False)
    
    F_ExPrice = db.Column(db.Integer, nullable=False)
    
    F_ExTag = db.Column(db.String(256), nullable=False)
    
    F_ExSit = db.Column(db.String(256), nullable=False)
    
    F_ExDeli = db.Column(db.String(256) , nullable=False)
    
    F_ExInfo = db.Column(db.String(256), nullable=False)
    
    F_ExPhoto = db.Column(db.String(256), nullable=False)
    
    F_ExPhotoS = db.Column(db.String(256), nullable=True)
    
    F_ExPhotoT = db.Column(db.String(256), nullable=True)
    
    F_ExPhotoF = db.Column(db.String(256), nullable=True)
    
    F_ExPhotoH = db.Column(db.String(256), nullable=True)
    
    F_EXhibitType = db.Column(db.Integer, nullable=False)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    


class T_Paramerter(db.Model):
    F_ID = db.Column(db.Integer, primary_key=True)
    F_userid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    F_friendid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    db.UniqueConstraint('F_userid', 'F_friendid', name='unique_friendship')
    
    user = db.relationship('T_User', foreign_keys=[F_userid])
    friend = db.relationship('T_User', foreign_keys=[F_friendid])
    

class T_Category(db.Model):
    F_CategoryID = db.Column(db.Integer, primary_key=True)
    
    F_CategoryName = db.Column(db.String(256), unique=True , nullable=False)