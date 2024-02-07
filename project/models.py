from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash
from project import db

# T_Userクラス
class T_User(db.Model,UserMixin):
    # 主キー
    F_UserID = db.Column(db.Integer, primary_key=True)
    # ユーザーネーム
    F_UserName = db.Column(db.String(40), unique=True, nullable=False)
    # パスワード
    F_Password = db.Column(db.String(256), nullable=False)
    # 登録日
    F_SignUpDay = db.Column(db.DateTime, default = datetime.utcnow)
    # 誕生日
    F_BirthDay = db.Column(db.Date, nullable=False)
    # 性別
    F_Gender = db.Column(db.String(10), nullable=True)
    # 電話番号
    F_Telphone = db.Column(db.String(16), nullable=False)
    # メールアドレス
    F_Email = db.Column(db.String(256), nullable=False , unique=True)
    # 
    F_Residence = db.Column(db.String(256), nullable=False)
    # 住所
    F_PosttalCode = db.Column(db.String(256), nullable=False)
    # 名前
    F_LastName = db.Column(db.String(256), nullable=False)
    # 名字
    F_FirstName = db.Column(db.String(256), nullable=False)
    # カナ文字
    F_LastName_Kana = db.Column(db.String(256), nullable=False)
    # カナ文字
    F_FirstName_Kana = db.Column(db.String(256), nullable=False)
    # プロフ画像
    F_ProfileImage = db.Column(db.String(256), nullable=False)
    # プロフコメント
    F_Profile_Comment = db.Column(db.String(256), nullable=True)
        
    images = db.relationship('T_Exhibit', backref='user',lazy=True)
    
    points = db.relationship('T_Point', backref='user', lazy=True)
    
    pet = db.relationship('T_Pet',backref='user',lazy=True)
    
    contest = db.relationship('T_Contest',backref='user', lazy=True)
    
    coupons = db.relationship('T_CouponPos', backref='user', lazy=True)
    
    message = db.relationship('T_Message', backref='user',lazy=True)
    
    def get_id(self):
        return str(self.F_UserID)
    

# 出品・お試し出品用のテーブル
class T_Exhibit(db.Model):
    # 主キー
    F_ExID = db.Column(db.Integer, primary_key=True)
    # タイトル
    F_ExTitle = db.Column(db.String(256) ,nullable=False)
    # 金額
    F_ExPrice = db.Column(db.Integer, nullable=False)
    # タグ
    F_ExTag = db.Column(db.String(256), nullable=False)
    # 説明
    F_ExSit = db.Column(db.String(256), nullable=False)
    # 配達方法
    F_ExDeli = db.Column(db.String(256) , nullable=False)
    # 説明
    F_ExInfo = db.Column(db.String(256), nullable=False)
    # 画像1
    F_ExPhoto = db.Column(db.String(256), nullable=False)
    # 画像2
    F_ExPhotoS = db.Column(db.String(256), nullable=True)
    # 画像3
    F_ExPhotoT = db.Column(db.String(256), nullable=True)
    # 画像4
    F_ExPhotoF = db.Column(db.String(256), nullable=True)
    # 画像5
    F_ExPhotoH = db.Column(db.String(256), nullable=True)
    # 出品形態
    F_EXhibitType = db.Column(db.Integer, nullable=False)
    # 出品時間
    F_ExTime = db.Column(db.DateTime, default=datetime.utcnow)
    # 商品状態
    F_Sold = db.Column(db.Boolean , default=False)
    # 商品の縦の長さ
    F_Width = db.Column(db.Integer, nullable=False)
    # 商品の横の長さ
    F_Height = db.Column(db.Integer, nullable=False)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_CategoryID = db.Column(db.Integer, db.ForeignKey('t__category.F_CategoryID'), nullable=False)
    
# 購入テーブル
class T_Cartlist(db.Model):
    # 主キー
    F_CartID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_ExID = db.Column(db.Integer, db.ForeignKey('t__exhibit.F_ExID') , nullable=False)
    # 購入合計
    F_CartPrice = db.Column(db.Float, nullable=False)
    
    user = db.relationship('T_User',foreign_keys=[F_UserID], backref='carts')
    
    exhibit = db.relationship('T_Exhibit', foreign_keys=[F_ExID])

# ユーザーのフォロー関連のテーブル
class T_Paramerter(db.Model):
    # 主キー
    F_ID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    F_userid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_friendid = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    db.UniqueConstraint('F_userid', 'F_friendid', name='unique_friendship')
    
    user = db.relationship('T_User', foreign_keys=[F_userid], backref='friends')
    friend = db.relationship('T_User', foreign_keys=[F_friendid])
    

# 商品カテゴリーのテーブル
class T_Category(db.Model):
    # 主キー
    F_CategoryID = db.Column(db.Integer, primary_key=True)
    # カテゴリーの名前
    F_CategoryName = db.Column(db.String(256), unique=True , nullable=False)
    # カテゴリー識別コード
    F_CategoryCode = db.Column(db.String(256), nullable=True)
    
    exhibits = db.relationship('T_Exhibit', backref='T_Category',lazy=True)
    
    pet = db.relationship('T_Pet', backref='T_Category',lazy=True)
    
    def __repr__(self):
        return f'<Category {self.F_CategoryName}>'
    


# お気に入りテーブル
class T_Favorite(db.Model):
    # 主キー
    F_FavoriteID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    user_id = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    exhibit_id = db.Column(db.Integer, db.ForeignKey('t__exhibit.F_ExID'), nullable=False)
    
    user = db.relationship('T_User',foreign_keys=[user_id])
    
    exhibit = db.relationship('T_Exhibit',foreign_keys=[exhibit_id])

# ポイントテーブル
class T_Point(db.Model):
    # 主キー
    F_PointID = db.Column(db.Integer, primary_key=True)
    # ポイント合計
    F_PointQuantity = db.Column(db.Integer, nullable=False , default=100)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    

# ペット基本情報
class T_Pet(db.Model):
    # 主キー
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
    F_Size = db.Column(db.String(256), nullable=False)
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
    # 外部キー
    F_CategoryID = db.Column(db.Integer, db.ForeignKey('t__category.F_CategoryID'), nullable=False)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)

# 迷子情報
class T_LostPet(db.Model):
    # 主キー
    F_LostPetID = db.Column(db.Integer, primary_key=True)
    # タイトル
    F_LostTitle = db.Column(db.String(256), nullable=False)
    # 投稿時間
    F_LostDate = db.Column(db.Date, nullable=False)
    # 引き取り場所
    F_LostPlase = db.Column(db.String(256), nullable=False)
    # けが
    F_LostInjury = db.Column(db.String(256), nullable=False)
    # 
    F_LostInstitution = db.Column(db.String(256), nullable=False)
    # 場所
    F_LostPlace = db.Column(db.String(256), nullable=False)
    # 
    F_LostFeatures = db.Column(db.String(256),nullable=False)
    # 場所
    F_LostLocation = db.Column(db.String(256), nullable=False)
    # 迷子発見
    F_FosterPeriod = db.Column(db.Boolean, default=False)
    # 外部キー
    F_PetID = db.Column(db.Integer, db.ForeignKey('t__pet.F_PetID'), nullable=False)
    
    pets = db.relationship('T_Pet',foreign_keys=[F_PetID])
    


# 里親情報
class T_FosterPet(db.Model):
    # 主キー
    F_FosterPetID = db.Column(db.Integer, primary_key=True)
    # タイトル
    F_FosterTitle = db.Column(db.String(256), nullable=False)
    # 場所
    F_Location = db.Column(db.String(256), nullable=False)
    # 保護場所
    F_FosterPlase = db.Column(db.String(256), nullable=False)
    # 恒例
    F_Senoir = db.Column(db.String(256), nullable=False)
    # 単身
    F_Single = db.Column(db.String(256), nullable=False)
    # 投稿時間
    F_FosterDate = db.Column(db.DateTime, default= datetime.utcnow)
    # 里親確定
    F_FosterPeriod = db.Column(db.Boolean, default=False)
    # 外部キー
    F_PetID = db.Column(db.Integer, db.ForeignKey('t__pet.F_PetID'), nullable=False)
    
    pets = db.relationship('T_Pet',foreign_keys=[F_PetID])
    

# チャットルーム
class T_Chat(db.Model):
    # 主キー
    F_ChatID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    F_SenderID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_ReceiverID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 内容
    F_ChatContest = db.Column(db.String(256), nullable=True)
    # 画像
    F_ChatImage = db.Column(db.String(256), nullable=True)
    # 時間
    F_ChatTime = db.Column(db.DateTime, default=datetime.utcnow)
    
    sender = db.relationship('T_User',foreign_keys=[F_SenderID])
    receiver = db.relationship('T_User',foreign_keys=[F_ReceiverID])
        

# ユーザープレビュー
class T_UserReview(db.Model):
    # 主キー
    F_UserReviewID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    F_ReviewID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_ReviewFollowID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # メッセージ
    F_UserReviewMessage = db.Column(db.String(256), nullable=False)
    # 点数
    F_Score = db.Column(db.Integer, nullable=False)
    # 総数
    F_Thumnbs = db.Column(db.Integer, nullable=False)
    
    review = db.relationship('T_User', foreign_keys=[F_ReviewID], backref='UserReview')
    
    reviewfollow = db.relationship('T_User', foreign_keys=[F_ReviewFollowID])
    
# コンテスト開催
class T_ContestMaster(db.Model):
    # 主キー
    F_ContestMasterID = db.Column(db.Integer, primary_key=True)
    # タイトル
    F_ContestMasterTitle = db.Column(db.String(256), nullable=False, unique=True)
    # 画像
    F_ContestMasterImage = db.Column(db.String(256) , nullable=False)
    # 内容
    F_ContestMasterContent = db.Column(db.String(256), nullable=False)
    # 募集期間
    F_ContestMasterTime = db.Column(db.Date , nullable=False)
    # 募集期間終了
    F_ContestPeriod = db.Column(db.Boolean , default=False)
    # 投票期間終了
    F_VotingPeriod = db.Column(db.Boolean, default=False)
    # 外部キー
    F_CouponID = db.Column(db.Integer, db.ForeignKey('t__coupon.F_CouponID'),nullable=False)
    contest = db.relationship('T_Contest',backref='contest',lazy=True)
    
# コンテスト
class T_Contest(db.Model):
    # 主キー
    F_ContestID = db.Column(db.Integer, primary_key=True)
    # タイトル
    F_ContestTitle = db.Column(db.String(256), nullable=False)
    # 画像
    F_ContestImage = db.Column(db.String(256), nullable=False)
    # 内容
    F_ContestComment = db.Column(db.String(256), nullable=False)
    # 投票
    F_Voting = db.Column(db.Integer, nullable=True)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_ContestMasterID = db.Column(db.Integer, db.ForeignKey('t__contest_master.F_ContestMasterID'), nullable=False)
    
#クーポン
class T_Coupon(db.Model):
    # 主キー
    F_CouponID = db.Column(db.Integer, primary_key=True)
    # クーポン名
    F_CouponCode = db.Column(db.String(256), unique=True, nullable=False)
    # クーポン割引
    F_CouponDis = db.Column(db.Float, nullable=False)
    
    coupon = db.relationship('T_CouponPos', backref = 'coupon', lazy=True)
    
    contest = db.relationship('T_ContestMaster', backref='coupon', lazy=True)

# クーポン所持
class T_CouponPos(db.Model):
    # 主キー
    F_CouponPosID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # 外部キー
    F_CouponID = db.Column(db.Integer, db.ForeignKey('t__coupon.F_CouponID'), nullable=False)
    # 所持クーポン枚数
    F_CouponQuantity = db.Column(db.Integer, nullable=False)


class T_Message(db.Model):
    # 主キー
    F_MessageID = db.Column(db.Integer, primary_key=True)
    # 外部キー
    F_UserID = db.Column(db.Integer, db.ForeignKey('t__user.F_UserID'), nullable=False)
    # メッセージ
    F_Message = db.Column(db.String(256), nullable=False)
    # 時間
    F_TimeStamp = db.Column(db.DateTime, nullable=False)