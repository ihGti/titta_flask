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
    
    points = db.relationship('T_Point', backref='user', lazy=True)
    
    pet = db.relationship('T_Pet',backref='user',lazy=True)
    
    def get_id(self):
        return str(self.F_UserID)
    

# 出品・お試し出品用のテーブル
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
    
    F_ExTime = db.Column(db.DateTime, default=datetime.utcnow)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    F_CategoryID = db.Column(db.Integer, db.ForeignKey('t__category.F_CategoryID'), nullable=False)

# ユーザーのフォロー関連のテーブル
class T_Paramerter(db.Model):
    F_ID = db.Column(db.Integer, primary_key=True)
    F_userid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    F_friendid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    db.UniqueConstraint('F_userid', 'F_friendid', name='unique_friendship')
    
    user = db.relationship('T_User', foreign_keys=[F_userid])
    friend = db.relationship('T_User', foreign_keys=[F_friendid])
    

# 商品カテゴリーのテーブル
class T_Category(db.Model):
    F_CategoryID = db.Column(db.Integer, primary_key=True)
    
    F_CategoryName = db.Column(db.String(256), unique=True , nullable=False)
    
    F_CategoryCode = db.Column(db.String(256), nullable=True)
    
    exhibits = db.relationship('T_Exhibit', backref='T_Category',lazy=True)
    
    pet = db.relationship('T_Pet', backref='T_Category',lazy=True)
    
    def __repr__(self):
        return f'<Category {self.F_CategoryName}>'
    


# お気に入りテーブル
class T_Favorite(db.Model):
    F_FavoriteID = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    exhibit_id = db.Column(db.Integer, db.ForeignKey('t__exhibit.F_ExID'), nullable=False)
    
    user = db.relationship('T_User',foreign_keys=[user_id])
    
    exhibit = db.relationship('T_Exhibit',foreign_keys=[exhibit_id])

# ポイントテーブル
class T_Point(db.Model):
    F_PointID = db.Column(db.Integer, primary_key=True)
    
    F_PointQuantity = db.Column(db.Integer, nullable=False , default=100)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    

# ペット基本情報
class T_Pet(db.Model):
    F_PetID = db.Column(db.Integer, primary_key=True)
    
    F_Date = db.Column(db.Date, default=datetime.utcnow)
    
    F_VeccineR = db.Column(db.String(256), nullable=False)
    
    F_VeccineT = db.Column(db.String(256), nullable=False)
    
    F_Health = db.Column(db.String(256), nullable=False)
    
    F_Colors = db.Column(db.String(256))
    
    F_Seibetu = db.Column(db.String(256), nullable=False)
    
    F_Age = db.Column(db.Integer, nullable=False)
    
    F_Size = db.Column(db.String(256), nullable=False)
    
    F_Castration = db.Column(db.String(256))
    
    F_Features = db.Column(db.String(256), nullable=False)
    
    F_Background = db.Column(db.String(256), nullable=False)
    
    F_Image = db.Column(db.String(256), nullable=False)
    
    F_Remarks = db.Column(db.String(256), nullable=False)
    
    F_CategoryID = db.Column(db.Integer, db.ForeignKey('t__category.F_CategoryID'), nullable=False)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)

# 迷子情報

# 里親情報