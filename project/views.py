# flask部品の取り込み
from flask import Flask , request , redirect , render_template , Blueprint , current_app , url_for
# flask-loginライブラリの取り込み
from flask_login import login_user, login_required, logout_user, current_user
# パスワードのセキュリティ関連のライブラリ
from werkzeug.security import generate_password_hash, check_password_hash
# 画像のファイル名を保護
from werkzeug.utils import secure_filename
# db接続に使う(更新・追加・削除)
from project import db , create_app
# models.pyで定義したテーブル
from project.models import T_User , T_Exhibit , T_Paramerter , T_Category

import os
# 時間の制約
from datetime import datetime

# 画面表示する
bp = Blueprint('main',__name__)

# app = Flas
# k(__name__)
# トップページ
@bp.route("/top")
# loginしていないと表示できないページが
# login情報の保持
@login_required
def index():
    return render_template("index.html" , username=current_user.F_UserName , user=current_user)


# logout
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

# user関連
# 会員登録
@bp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=="POST":
        mail = request.form.get('email')
        mail_conform = request.form.get('email_conform')
        password = request.form.get('password')
        password_conform = request.form.get('password_conform')
        sei = request.form.get('sei')
        mei = request.form.get('mei')
        sei_kana = request.form.get('sei-kana')
        mei_kana = request.form.get('mei-kana')
        username = request.form.get('username')
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        day = int(request.form.get('day'))
        birthday = datetime(year,month,day)
        gender = request.form.get('seibetu')
        telphone = request.form.get('telphone')
        yuubin = request.form.get('yuubin')
        address = request.form.get('address')
        prof_image = request.files['prof_image']
        


        
        hashed_password = None
        prof_image_filename = secure_filename(prof_image.filename)
        prof_image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], prof_image_filename))

        if mail == mail_conform and password == password_conform:
            hashed_password = generate_password_hash(password, method='sha256')
        else:
            pass


        
        
        user = T_User(
            F_UserName=username,
            F_Password=hashed_password,
            F_SignUpDay=datetime.utcnow(),
            F_BirthDay=birthday,
            F_Gender=gender,
            F_Telphone=telphone,
            F_Email=mail,
            F_Residence=address,
            F_PosttalCode=yuubin,
            F_LastName=sei,
            F_FirstName=mei,
            F_LastName_Kana=sei_kana,
            F_FirstName_Kana=mei_kana,
            F_ProfileImage=prof_image_filename  # 画像のファイル名を保存
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/cor')
    
    else:
        return render_template("signin.html")

# ログインページ
@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        mail = request.form.get('email')
        password = request.form.get('password')
        
        user = T_User.query.filter_by(F_Email=mail).first()
        
        if check_password_hash(user.F_Password,password):
            login_user(user)
            return redirect('/top')
        else:
            return render_template('login.html')
        
    return render_template('login.html')

# 登録完了
@bp.route("/cor")
def cor():
    return render_template("cor.html")

# マイページ
@bp.route("/myprof")
def myprof():
    user = T_User.query.get(current_user.F_UserID)
    
    return render_template("my_profile.html" , user=user)

# マイページ編集
@bp.route("/prof_edit", methods=['GET','POST'])
def prof_edit():
    user = T_User.query.get(current_user.F_UserID)
    if request.method=='POST':
        
        username = request.form.get("username")
        user_description = request.form.get("user-description")
        profile_image = request.files['profile_image']
        
        user.F_UserName = username
        user.F_Profile_Comment = user_description
        
        if profile_image:
            fileimage = secure_filename(profile_image.filename)
            profile_image.save(os.path.join(current_app.config['UPLOAD_FOLDER'],fileimage))
            
            user.F_ProfileImage = fileimage
        
        db.session.commit()
        return redirect('myprof')
    
    return render_template("profile_edit.html",user=user)

# 他者プロフ
@bp.route("/userprof/<int:user_id>")
@login_required
def user_prof(user_id):
    user = T_User.query.get(user_id)
    friends = T_User.query.join(T_Paramerter, T_Paramerter.F_friendid == T_User.F_UserID).filter(T_Paramerter.F_userid == T_User.F_UserID).all()
    
    followers_count = T_Paramerter.query.filter_by(friend_id=user.id).count()
    following_count = T_Paramerter.query.filter_by(user_id=user.id).count()
    return render_template("user_profile.html",user=user, friends=friends , followers_count=followers_count , following_count=following_count)

# フォロー関連
@bp.route("/add_friend/<int:user_id>",methods=['POST'])
@login_required
def add_friend(user_id):
    
    current_user_id = current_user.id
    
    user_friendship = T_Paramerter.query.filter_by(user_id = current_user_id, friend = user_id).first()
    if user_friendship:
        return "すでにフォローされています"
    
    friendship = T_Paramerter(user_id=current_user_id, friend_id=user_id)
    db.session.add(friendship)
    db.session.commit()
    
    return redirect(url_for('userprof', user_id=user_id))

# 出品関連
# 本出品
@bp.route("/upload" , methods=['POST'])
def exhibit():
    
    for i in range(1,6):
        file = request.files.get(f'imageinput{i}')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER_TOREDO'], filename))
        
        
        if i == 1:
            exhibit = T_Exhibit(F_ExPhoto=filename)
            
        elif i == 2:
            exhibit.F_ExPhotoS = filename
        
        elif i == 3:
            exhibit.F_ExPhotoT = filename
            
        elif i == 4:
            exhibit.F_ExPhotoH = filename
            
        elif i == 5:
            exhibit.F_ExPhotoF = filename
    
    title = request.form.get('title')
    
    info = request.form.get('setumei')
    
    situation = request.form.get('situation')
    
    deli = request.form.get('deli')
    
    genre = request.form.get('genre')
    
    category = T_Category.query.get(genre)
    
    many = request.form.get('kane')
    
    tag = request.form.get('tag')
    
    exhibit.F_ExTitle = title
    
    exhibit.F_ExInfo = info
    
    exhibit.F_ExDeli = deli
    
    exhibit.F_CategoryID = category.F_CategoryID
    
    exhibit.F_ExPrice = many
    
    exhibit.F_ExTag = tag
    
    exhibit.F_ExSit = situation
    
    exhibit.F_EXhibitType = 1
    
    exhibit.F_UserID = current_user.F_UserID
    
    db.session.add(exhibit)
    db.session.commit()
    
    return redirect('/exhibit_con')

# 出品
@bp.route('/exhibit', methods=['GET'])
@login_required
def upload_page():
    categories = T_Category.query.all()
    return render_template('exhibit.html' , user=current_user , categories=categories)

# 出品確認
@bp.route("/exhibit_con")
def exhibit_con():
    exhibit = T_Exhibit.query.filter_by(F_UserID = current_user.F_UserID)
    return render_template("exhibit_con.html" , exhibit=exhibit)

# 出品完了
@bp.route("/exhibit_comp")
def exhibit_comp():
    return render_template("exhibit_comp.html")

# お試し出品
@bp.route("/exhibit_trial")
def exhibit_trial():
    return render_template("exhibit_trial.html")

# 商品関連
# 商品一覧
@bp.route("/product")
def product():
    
    return render_template("product.html")

# 商品詳細
@bp.route("/product_detail")
def product_detail():
    return render_template("product_detail.html")


# 目玉機能
# 里親掲示板
@bp.route("/foster_board")
def foster_board():
    return render_template("foster_board.html")

# 迷子掲示板
@bp.route("/lost_petboard")
def lost_petboard():
    return render_template("lost_petboard.html")

# 里親投稿
@bp.route("/foster_post")
def foster_post():
    return render_template("foster_post.html")

# 迷子投稿
@bp.route("/lost_post")
def lost_post():
    return render_template("lost_post.html")

# 里親詳細
@bp.route("/foster_detail")
def foster_detail():
    return render_template("foster_detail.html")

# 迷子詳細
@bp.route("/lost_detail")
def lost_detail():
    return render_template("lost_detail.html")

# ペット一覧
@bp.route("/reg_pet")
def pet_list():
    return render_template("reg_pet.html")

# コンテスト
@bp.route("/contest")
def contest():
    return render_template("contest.html")

# 譲渡会
@bp.route("/assignment")
def assignment():
    return render_template("assignment.html")

# コミュニティルーム
@bp.route("/community")
def community():
    return render_template("community.html")


# 履歴関連
# お気に入り
@bp.route("/favorite")
def favorite():
    return render_template("favorite.html")

# 閲覧履歴
@bp.route("/browsing")
def browsing():
    return render_template("browsing.html")

# 購入履歴
@bp.route("/listing_list")
def listing_list():
    return render_template("listing_list.html")

# 出品リスト
@bp.route("/exhibition_list")
def exhibition_list():
    return render_template("exhibition_list.html")

# 売上履歴
@bp.route("/earnings_history")
def earnings_history():
    return render_template("earnings_history.html")

# 掲載履歴
@bp.route("/petpublish_hiatory")
def petpublish_history():
    return render_template("petpublish_history.html")

# 出品履歴
@bp.route("/listing_history")
def listing_history():
    return render_template("listing_list.html")


# その他
# ポイント管理
@bp.route("/point")
def point():
    return render_template("point.html")

# メールボックス
@bp.route("/mailbox")
def mailbox():
    return render_template("mailbox.html")

# お知らせ
@bp.route("/notice")
def notice():
    return render_template("notice.html")

# 設定
@bp.route("/setting")
def setting():
    return render_template("setting.html")

# 着せ替え
@bp.route("/dressup")
def dressup():
    return render_template("dressup.html")

# Q&A
@bp.route("/qa")
def qa():
    return render_template("qa.html")

# 問い合わせ
@bp.route("/inquiry")
def inquiry():
    return render_template("inquiry.html")



# 管理者ページ
@bp.route("/admin")
def admin():
    return render_template("adminnistrator.html")

# テーブルメンテナンス
@bp.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")
