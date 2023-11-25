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
    
# 購入テーブル
class T_Cartlist(db.Model):
    F_CartID = db.Column(db.Integer, primary_key=True)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    F_ExID = db.Column(db.Integer, db.ForeignKey('t__exhibit.F_ExID') , nullable=False)
    
    F_CartPrice = db.Column(db.Float, nullable=False)
    
    user = db.relationship('T_User',foreign_keys=[F_UserID], backref='carts')
    
    exhibit = db.relationship('T_Exhibit', foreign_keys=[F_ExID])

# ユーザーのフォロー関連のテーブル
class T_Paramerter(db.Model):
    F_ID = db.Column(db.Integer, primary_key=True)
    F_userid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    F_friendid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    db.UniqueConstraint('F_userid', 'F_friendid', name='unique_friendship')
    
    user = db.relationship('T_User', foreign_keys=[F_userid], backref='friends')
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
    # 掲載期日
    F_Date = db.Column(db.Date, nullable=False)
    # ワクチン接種済み
    F_VeccineR = db.Column(db.String(256), nullable=True)
    # ワクチン登録
    F_VeccineT = db.Column(db.String(256), nullable=True)
    # 健康状態
    F_Health = db.Column(db.String(256), nullable=False)
    # 色
    F_Colors = db.Column(db.String(256),nullable=True)
    # 性別
    F_Seibetu = db.Column(db.String(256), nullable=False)
    # 年齢
    F_Age = db.Column(db.Integer, nullable=False)
    # 大きさ
    F_Size = db.Column(db.Integer, nullable=False)
    # 去勢・避妊
    F_Castration = db.Column(db.String(256) , nullable=True)
    # 特徴
    F_Features = db.Column(db.String(256), nullable=False)
    # 経緯
    F_Background = db.Column(db.String(256), nullable=False)
    # 画像
    F_Image = db.Column(db.String(256), nullable=False)
    # 備考
    F_Remarks = db.Column(db.String(256), nullable=False)
    
    F_CategoryID = db.Column(db.Integer, db.ForeignKey('t__category.F_CategoryID'), nullable=False)
    
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)

# 迷子情報
class T_LostPet(db.Model):
    F_LostPetID = db.Column(db.Integer, primary_key=True)
    
    F_LostTitle = db.Column(db.String(256), nullable=False)
    
    F_LostDate = db.Column(db.Date, nullable=False)
    
    F_LostPlase = db.Column(db.String(256), nullable=False)
    
    F_LostInjury = db.Column(db.String(256), nullable=False)
    
    F_LostInstitution = db.Column(db.String(256), nullable=False)
    
    F_LostPlace = db.Column(db.String(256), nullable=False)
    
    F_LostFeatures = db.Column(db.String(256),nullable=False)
    
    F_LostLocation = db.Column(db.String(256), nullable=False)
        
    F_PetID = db.Column(db.Integer, db.ForeignKey('t__pet.F_PetID'), nullable=False)
    
    pets = db.relationship('T_Pet',foreign_keys=[F_PetID])
    


# 里親情報
class T_FosterPet(db.Model):
    F_FosterPetID = db.Column(db.Integer, primary_key=True)
    
    F_FosterTitle = db.Column(db.String(256), nullable=False)
    
    F_Location = db.Column(db.String(256), nullable=False)
    
    F_FosterPlase = db.Column(db.String(256), nullable=False)
    
    F_Senoir = db.Column(db.String(256), nullable=False)
    
    F_Single = db.Column(db.String(256), nullable=False)
    
    F_FosterDate = db.Column(db.DateTime, default= datetime.utcnow)
    
    F_PetID = db.Column(db.Integer, db.ForeignKey('t__pet.F_PetID'), nullable=False)
    
    pets = db.relationship('T_Pet',foreign_keys=[F_PetID])
    

# チャットルーム
class T_Chat(db.Model):
    F_ChatID = db.Column(db.Integer, primary_key=True)
    
    F_SenderID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    F_ReceiverID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    F_ChatContest = db.Column(db.String(256), nullable=True)
    
    F_ChatImage = db.Column(db.String(256), nullable=True)
    
    F_ChatTime = db.Column(db.DateTime, default=datetime.utcnow)
    
    sender = db.relationship('T_User',foreign_keys=[F_SenderID])
    receiver = db.relationship('T_User',foreign_keys=[F_ReceiverID])
        


class T_UserReview(db.Model):
    F_UserReviewID = db.Column(db.Integer, primary_key=True)
    
    F_ReviewID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    F_ReviewFollowID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    
    F_UserReviewMessage = db.Column(db.String(256), nullable=False)
    
    F_Score = db.Column(db.Integer, nullable=False)
    
    F_Thumnbs = db.Column(db.Integer, nullable=False)
    
    review = db.relationship('T_User', foreign_keys=[F_ReviewID], backref='UserReview')
    
    reviewfollow = db.relationship('T_User', foreign_keys=[F_ReviewFollowID])

