# flask部品の取り込み
from flask import Flask , request , flash, redirect , render_template , Blueprint , current_app , url_for , session
# flask-loginライブラリの取り込み
from flask_login import login_user, login_required, logout_user, current_user , login_manager
# パスワードのセキュリティ関連のライブラリ
from werkzeug.security import generate_password_hash, check_password_hash
# 画像のファイル名を保護
from werkzeug.utils import secure_filename
# db接続に使う(更新・追加・削除)
from project import db , create_app
# models.pyで定義したテーブル
from project.models import T_User , T_Exhibit , T_Paramerter , T_Category , T_Favorite , T_Point , T_Cartlist , T_Pet , T_FosterPet , T_LostPet , T_Chat , T_UserReview , T_Contest , T_ContestMaster

import os
# 時間の制約
from datetime import datetime, date

# 画面表示する
bp = Blueprint('main',__name__)


# app = Flas
# k(__name__)
# トップページ
@bp.route("/top", methods=['GET','POST'])
# loginしていないと表示できないページが
# login情報の保持
@login_required
def index():
    # methodがpostの場合
    if request.method== 'POST':
        word = request.form.get('word')
        exword = request.form.get('exword')
        genre = request.form.get('genre')
        l_price= request.form.get('lowerprice')
        h_price = request.form.get('highprice')
        
        # 本出品だけを抽出
        query = T_Exhibit.query.filter_by(F_EXhibitType=1)
        
        # タグ検索
        if word:
            query = query.filter(T_Exhibit.F_ExTag.contains(word))
            
        # 除外ワード
        if exword:
            query = query.filter(T_Exhibit.F_ExInfo.like(f"%{exword}%"))
            
        # 下限金額
        if l_price:
            query = query.filter(T_Exhibit.F_ExPrice >= l_price)
        # 上限金額
        if h_price:
            query = query.filter(T_Exhibit.F_ExPrice <= h_price)
        
        # カテゴリー検索
        if genre:
            category = T_Category.query.filter_by(F_CategoryID=genre).first()
            if category:
                query = query.filter(T_Exhibit.F_CategoryID==category.F_CategoryID)
        
        # 商品検索結果
        product = query.all()
        
        # 検索した商品の数を取得
        num_product = len(product)
        return render_template('product.html', product=product , user=current_user , word=word , exword=exword , genre=genre , num_product=num_product)
    # カテゴリーを全件取得
    category=T_Category.query.filter_by(F_CategoryCode='c')
    return render_template("index.html" , username=current_user.F_UserName , user=current_user, category=category)


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
        
        # 画像を保存する場合の処理
        prof_image_filename = secure_filename(prof_image.filename)
        prof_image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], prof_image_filename))

        # メールアドレスとパスワードが一致した場合、パスワードをハッシュ化する
        if mail == mail_conform and password == password_conform:
            hashed_password = generate_password_hash(password, method='sha256')
        else:
            pass


        
        # T_Userの対応するカラムに変数を格納
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
        
        # 登録したら初期ポイントで100ポイント付加
        init_point =T_Point(F_PointQuantity=100)
        user.points.append(init_point)
        
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
        
        # T_UserのF_Emailと入力したメールアドレスを比較し、対象ユーザーを取り出す
        user = T_User.query.filter_by(F_Email=mail).first()
        
        if user :
            if check_password_hash(user.F_Password,password):
                login_user(user)
                return redirect('/top')
            else:
                flash('パスワードが違います')
                return render_template('login.html')
        else:
            flash('メールアドレスが存在しません')
            return redirect('/login')
        
    return render_template('login.html')

# 登録完了
@bp.route("/cor")
def cor():
    return render_template("cor.html")

# マイページ
@bp.route("/myprof")
@login_required
def myprof():
    # ログインしているユーザーの情報を取得
    user = T_User.query.get(current_user.F_UserID)
    
    return render_template("my_profile.html" , user=user)

# マイページ編集
@bp.route("/prof_edit", methods=['GET','POST'])
def prof_edit():
    user = T_User.query.get(current_user.F_UserID)
    if request.method=='POST':
        # ユーザーネームを入力
        username = request.form.get("username")
        # プロフィールコメント
        user_description = request.form.get("user-description")
        # プロフ画像
        profile_image = request.files['profile_image']
        # ユーザーネームの更新
        user.F_UserName = username
        # プロフコメントの更新
        user.F_Profile_Comment = user_description
        
        # プロフ画像の更新
        if profile_image:
            fileimage = secure_filename(profile_image.filename)
            profile_image.save(os.path.join(current_app.config['UPLOAD_FOLDER'],fileimage))
            
            user.F_ProfileImage = fileimage
        # 内容の更新処理
        db.session.commit()
        return redirect('myprof')
    
    return render_template("profile_edit.html",user=user)

# 他者プロフ
@bp.route("/userprof/<int:user_id>")
@login_required
def user_prof(user_id):
    # 他者プロフを取得
    users = T_User.query.get(user_id)
    
    exhibits = T_Exhibit.query.get(user_id)
    
    if users:
        # フォローしているユーザーを取得
        friends = T_User.query.join(T_Paramerter, T_Paramerter.F_friendid == T_User.F_UserID).filter(T_Paramerter.F_userid == T_User.F_UserID).all()
        # フォロワーをカウント
        followers_count = T_Paramerter.query.filter_by(F_friendid=users.F_UserID).count()
        # フォロー中のユーザーをカウント
        following_count = T_Paramerter.query.filter_by(F_userid=users.F_UserID).count()
    return render_template("user_profile.html",users=users, friends=friends , followers_count=followers_count , following_count=following_count , user=current_user , exhibits=exhibits)

# フォロー関連
@bp.route("/add_friend/<int:user_id>",methods=['POST'])
@login_required
def add_friend(user_id):
    # ログインユーザー
    current_user_id = current_user.F_UserID
    # ユーザーをフォローしているか
    user_friendship = T_Paramerter.query.filter_by(F_userid = current_user_id, F_friendid = user_id).first()
    # フォローしていたら
    if user_friendship:
        return "すでにフォローされています"
    # フォローしていない場合はフォロー処理をする
    friendship = T_Paramerter(F_userid=current_user_id, F_friendid=user_id)
    db.session.add(friendship)
    db.session.commit()
    
    return redirect(url_for('user_prof', user_id=user_id))

# 出品関連
# 本出品
@bp.route("/upload" , methods=['POST'])
def exhibit():    
    if request.method == "POST":
        image_files=[]
            # 1~5枚の画像を保存する処理
        for i in range(1,6):
            file = request.files.get(f'imageinput{i}')
        # 画像の保存
            if file:
                filename = secure_filename(file.filename)
                image_files.append(filename)
                filepath=os.path.join(current_app.config['UPLOAD_FOLDER_TOREDO'], filename)
                file.save(filepath)
        
        # タイトル
        title = request.form.get('title')
        # 説明
        info = request.form.get('setumei')
        # 状態
        situation = request.form.get('situation')
        # 配達方法
        deli = request.form.get('deli')
        # ジャンル
        genre = request.form.get('genre')
        # カテゴリーテーブルから取得
        category = T_Category.query.get(genre)
        # 金額
        many = request.form.get('kane')
        # ハッシュタグ
        tag = request.form.get('tag')
        # ハッシュタグから単語を抽出
        hashtags = [word for word in tag.split() if word.startswith('#')]
        hashtags = ' '.join(hashtags)
        
        user_id = current_user.F_UserID
        
        session["exhibit_info"] = {
            "title":title,
            "info":info,
            "situation":situation,
            "deli":deli,
            "category":category.F_CategoryID,
            "many":many,
            "tag":tag,
            "user":user_id,
            "image_files":image_files,
        }
    return redirect('/exhibit_con')

# 出品
@bp.route('/exhibit', methods=['GET'])
@login_required
def upload_page():
    # カテゴリー全件取得
    categories = T_Category.query.filter_by(F_CategoryCode='c')
    return render_template('exhibit.html' , user=current_user , categories=categories)

# 出品確認
@bp.route("/exhibit_con", methods=["GET","POST"])
def exhibit_con():
    
    exhibit_info = session.get('exhibit_info')
    print(exhibit_info)
    return render_template("exhibit_con.html" , user=current_user , exhibit_info=exhibit_info )

# 出品完了
@bp.route("/exhibit_comp", methods=["GET","POST"])
def exhibit_comp():
    if request.method=="POST":
        exhibit_data= session.get('exhibit_info')
        
        if exhibit_data:
            exhibit = T_Exhibit(
                F_ExTitle = exhibit_data["title"],
                F_ExPrice = exhibit_data["many"],
                F_ExSit = exhibit_data["situation"],
                F_ExInfo = exhibit_data["info"],
                F_ExDeli = exhibit_data["deli"],
                F_ExTag = exhibit_data["tag"],
                F_CategoryID = exhibit_data["category"],
                F_UserID = exhibit_data["user"],
                F_ExPhoto = exhibit_data["image_files"][0],
                F_ExPhotoS = exhibit_data["image_files"][1] if len(exhibit_data["image_files"])>1 else None,
                F_ExPhotoT = exhibit_data["image_files"][2] if len(exhibit_data["image_files"])>2 else None,
                F_ExPhotoF = exhibit_data["image_files"][3] if len(exhibit_data["image_files"])>3 else None,
                F_ExPhotoH = exhibit_data["image_files"][4] if len(exhibit_data["image_files"])>4 else None,
                F_EXhibitType = 1,
                F_ExTime = datetime.utcnow()
            )
            db.session.add(exhibit)
            db.session.commit()
        total_point = 50
    
        user_point = T_Point.query.filter_by(F_UserID=current_user.F_UserID).first()
    
        if user_point:
            new_point = user_point.F_PointQuantity + total_point
        
            user_point.F_PointQuantity = new_point
        
            db.session.commit()
        return render_template("exhibit_comp.html", user=current_user)
    return render_template("exhibit_comp.html" , user=current_user)

# お試し出品投稿
@bp.route('/trial_page',methods=['POST'])
def trial_upload():
    
    for i in range(1,6):
        file = request.files.get(f'imageinput{i}')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER_DEMOEXHIBIT'],filename))
            
            if i == 1:
                demoexhibit = T_Exhibit(F_ExPhoto=filename)
        
            elif i == 2:
                demoexhibit.F_ExPhotoS = filename
            
            elif i == 3:
                demoexhibit.F_ExPhotoT = filename
            
            elif i == 4:
                demoexhibit.F_ExPhotoF = filename
            
            elif i == 5:
                demoexhibit.F_ExPhotoH = filename
            
    title = request.form.get('title')
        
    info = request.form.get('setumei')
        
    situation = request.form.get('situation')
        
    deli = request.form.get('deli')
        
    genre = request.form.get('genre')
        
    category = T_Category.query.get(genre)
        
    many = request.form.get('kane')
        
    tag = request.form.get('tag')
        
    demoexhibit.F_ExTitle = title
        
    demoexhibit.F_ExInfo = info
        
    demoexhibit.F_ExSit = situation
        
    demoexhibit.F_ExDeli = deli
        
    demoexhibit.F_ExPrice = many
        
    demoexhibit.F_CategoryID = category.F_CategoryID
        
    demoexhibit.F_ExTag = tag
        
    demoexhibit.F_EXhibitType = 2
    demoexhibit.F_UserID = current_user.F_UserID
    
    demoexhibit.F_ExTime = datetime.utcnow()
    db.session.add(demoexhibit)
    db.session.commit()
    user = T_User.query.get(current_user.F_UserID)
    
    total_point = 200
    
    user_point = T_Point.query.filter_by(F_UserID=current_user.F_UserID).first()
    
    if user_point:
        new_point = user_point.F_PointQuantity + total_point
        
        user_point.F_PointQuantity = new_point
        
        db.session.commit()

    return redirect("/top")

# お試し出品画面表示
@bp.route("/exhibit_trial", methods=['GET'])
def exhibit_trial():
    categories = T_Category.query.filter_by(F_CategoryCode='c')
    return render_template("exhibit_trial.html" , user=current_user , categories=categories)

# 商品関連
# 商品一覧
@bp.route("/product")
def product():
    product = T_Exhibit.query.all()
    category = T_Category.query.all()
    return render_template("product.html" , product=product , user=current_user , category=category)

# カテゴリー検索:index.html
@bp.route('/category_product/<int:category_id>/products', methods=['GET'])
@login_required
def category_product(category_id):
    category = T_Category.query.get(category_id)
    product = T_Exhibit.query.filter_by(F_CategoryID=category_id,F_EXhibitType=1).all()
    
    return render_template('product.html', product=product, category=category , user=current_user)


# 商品詳細
@bp.route("/product_detail/<int:exhibit_id>")
@login_required
def product_detail(exhibit_id):
    # idに基づいた商品を取得
    exhibit = T_Exhibit.query.get(exhibit_id)
    # 商品を出品したユーザーを取得
    users = T_User.query.get(exhibit.F_UserID)
    return render_template("product_detail.html", exhibit=exhibit , user=current_user , users=users)


# 購入確認
@bp.route("/settelement_comp/<int:exhibit_id>", methods=['POST'])
@login_required
def settelement_check(exhibit_id):
    # 商品を取得
    exhibit = T_Exhibit.query.get(exhibit_id)
    
    return render_template('settelement_comp.html', exhibit=exhibit, user=current_user)

# 購入確定
@bp.route("/settelement_check/<int:exhibit_id>", methods=['GET','POST'])
@login_required
def settelement_comp(exhibit_id):
    # 商品取得
    exhibit = T_Exhibit.query.get(exhibit_id)
    # ユーザーポイント取得
    user_point = T_Point.query.filter_by(F_UserID = current_user.F_UserID).first()
    # 出品したユーザーとログインユーザーが一致した場合
    if exhibit.F_UserID == current_user.F_UserID:
        return redirect(url_for('main.product_detail', exhibit_id=exhibit_id))
    
    if request.method=='POST':
        # 購入方法などのフォーム
        if 'check' in request.form:
            exhibit = T_Exhibit.query.get(exhibit_id)
            # ポイント取得
            points = int(request.form.get('pointnum')) if request.form.get('pointnum').isdigit() else 0
            user_point = T_Point.query.filter_by(F_UserID = current_user.F_UserID).first()
            if user_point.F_PointQuantity < points:
                return render_template("settelement_check.html", user=current_user,points=points , user_point=user_point , exhibit=exhibit)
            if points and user_point.F_PointQuantity > 0:
                # ユーザーがポイントを持っており、ポイントを使う場合の処理
                cart_price =exhibit.F_ExPrice - points

                user_point.F_PointQuantity -= points
                session["cart_price"] = cart_price

            elif points==0 :
                cart_price = exhibit.F_ExPrice
            return render_template("settelement_check.html",exhibit=exhibit, user=current_user, points=points, user_point=user_point, cart_price=cart_price)
        # 購入完了画面に進む
        elif 'comp' in request.form:
            exhibit = T_Exhibit.query.get(exhibit_id)
            # ポイント取得
            cart_price = session.get("cart_price")
            user_point = T_Point.query.filter_by(F_UserID = current_user.F_UserID).first()
            
            if cart_price:
                cart = T_Cartlist(F_UserID = current_user.F_UserID,
                                F_ExID = exhibit_id,
                                F_CartPrice = cart_price)
            
            db.session.add(cart)
            
            user_cart_price = T_Cartlist.query.filter_by(F_UserID=current_user.F_UserID).all()
            post_user_price = sum(purchase.F_CartPrice for purchase in user_cart_price)
                
            total_cart_price = post_user_price + cart_price
                
            user_point.F_CartPrice = total_cart_price
            
            exhibit.F_Sold = True
            
            db.session.commit()
            
            return render_template("settlement_comp.html",exhibit=exhibit, user=current_user , cart_price=cart_price)

    return render_template("settelement_check.html", exhibit=exhibit, user=current_user , user_point=user_point )


# 目玉機能
# 里親掲示板
@bp.route("/foster_board")
@login_required
def foster_board():
    return render_template("foster_board.html" , user=current_user)

# 迷子掲示板
@bp.route("/lost_petboard" , methods=['GET','POST'])
@login_required
def lost_petboard():
    if request.method == 'POST':
        location = request.form.get('hakkenti')
        lostarea = request.form.get('lostarea')
        lost_date = request.form.get('foundday')
        found = datetime.strptime(lost_date,'%Y-%m-%d').date()
        gender = request.form.get('gender')
        kinds = request.form.get('kinds')
        freeword = request.form.get('freeword')
        
        query = T_Pet.query.all()
        query2 = T_LostPet.query.filter_by(T_LostPet.F_PetID == T_Pet.F_PetID)
        
        if location:
            query = query2.filter(T_Pet.F_Location == location)
            
    return render_template("lost_petboard.html" , user=current_user)

# 里親投稿
@bp.route("/foster_post_page",methods=['POST'])
def foster_post():
    if request.method=='POST':
        # pet
        date_query = request.form.get('keisaiW')
        k_date= datetime.strptime(date_query,'%Y-%m-%d').date()
        kinds= request.form.get('kindsW')
        category = T_Category.query.get(kinds)
        gender = request.form.get('radio-002')
        age = request.form.get('ageW')
        size = request.form.get('sizeW')
        vaccine = request.form.get('radio-003')
        vaccine2 = request.form.get('vaccineW')
        cast = request.form.get('radio-004')
        background = request.form.get('backgroundW')
        personal = request.form.get('personalityW')
        health = request.form.get('healthW')
        other = request.form.get('otherW')
        image = request.files['example']
        # foster
        title = request.form.get('postW')
        location = request.form.get('radio-001')
        single = request.form.get('radio-005')
        elder = request.form.get('radio-006')
        place = request.form.get('placeW')
        
        
        if image:
            pet_image = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_FOSTERPET'],pet_image))
            
        pet =T_Pet(
            F_Date=k_date,
            F_CategoryID = category.F_CategoryID,
            F_Seibetu = gender,
            F_Age = age,
            F_Size = size,
            F_VeccineR = vaccine,
            F_VeccineT = vaccine2,
            F_Castration = cast,
            F_Background = background,
            F_Features = personal,
            F_Health = health,
            F_Remarks = other,
            F_Image = pet_image,
            F_UserID = current_user.F_UserID
        )
        db.session.add(pet)
        db.session.commit()
        
        foster = T_FosterPet(
            F_FosterTitle= title,
            F_Location = location,
            F_FosterPlase = place,
            F_Senoir = elder,
            F_Single = single,
            F_FosterDate = datetime.utcnow(),
            F_PetID = pet.F_PetID
        )
        db.session.add(foster)
        db.session.commit()
            
    return redirect('/top')

@bp.route('/foster_post', methods=['GET'])
@login_required
def foster():
    category = T_Category.query.filter_by(F_CategoryCode='p')
    return render_template("foster_post.html",category=category, user=current_user)

# 迷子投稿
@bp.route("/lost_post_page", methods=['POST'])
def lost_post():
    if request.method == 'POST':
        # pet
        k_date = datetime.strptime(request.form.get('keisaiW'),'%Y-%m-%d').date()
        kinds = request.form.get('kindsW')
        category = T_Category.query.get(kinds)
        gender = request.form.get('radio-002')
        age = request.form.get('ageW')
        size = request.form.get('sizeW')
        color = request.form.get('colorW')
        background = request.form.get('backgroundW')
        personal = request.form.get('personalityW')
        health = request.form.get('healthW')
        other = request.form.get('otherW')
        image = request.files['example']
        
        # foster
        title = request.form.get('postW')
        location = request.form.get('radio-001')
        hogodate = datetime.strptime(request.form.get('hogoW'),'%Y-%m-%d').date()
        place = request.form.get('hogoplaceW')
        injury = request.form.get('radio-003')
        institution = request.form.get('institutionW')
        feature = request.form.get('featuresW')
        places = request.form.get('placeW')
        
        if image:
            lost_image = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_LOSTPET'],lost_image))
        
        pet = T_Pet(
            F_Date = k_date,
            F_CategoryID = category.F_CategoryID,
            F_Seibetu = gender,
            F_Age = age,
            F_Size = size,
            F_Colors = color,
            F_Background = background,
            F_Features = personal,
            F_Health = health,
            F_Remarks = other,
            F_Image = lost_image,
            F_UserID = current_user.F_UserID
        )
        
        db.session.add(pet)
        db.session.commit()
        
        lost_pet = T_LostPet(
            F_LostTitle = title,
            F_LostDate = hogodate,
            F_LostPlase = location,
            F_LostInjury = injury,
            F_LostInstitution = institution,
            F_LostPlace = place,
            F_LostLocation = places,
            F_LostFeatures = feature,
            F_PetID = pet.F_PetID
        )
        
        db.session.add(lost_pet)
        db.session.commit()
        
    return redirect('/top')

@bp.route('/lost_post',methods=['GET'])
@login_required
def lost():
    category = T_Category.query.filter_by(F_CategoryCode='p')
    return render_template('lost_post.html', user=current_user, category=category)

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
    
    return render_template("reg_pet.html" , user=current_user)

# コンテストマスター
@bp.route("/master_upload", methods=['GET','POST'])
def master_upload():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        c_date = datetime.strptime(request.form.get('time'),'%Y-%m-%d').date()
        image = request.files['image']
        
        if image:
            file = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_CONTEST_MASTER'],file))
        
        master = T_ContestMaster(
            F_ContestMasterTitle = title,
            F_ContestMasterContent = content,
            F_ContestMasterImage = file,
            F_ContestMasterTime = c_date
        )
        
        db.session.add(master)
        db.session.commit()
        
    return 'Contest Successfully!'

# コンテストマスター表示
@bp.route('/master')
def master():
    return render_template('contest_master.html')

# コンテスト
@bp.route("/contest")
def contest():
    slider = T_ContestMaster.query.all()
    contest = T_ContestMaster.query.all()
    contestpost = len(contest)
    return render_template("contest.html",user=current_user , contest=contest , contestpost=contestpost, slider=slider)

# コンテスト詳細
@bp.route("/contest_detail/<int:contest_id>")
def contest_detail(contest_id):
    contest_detail = T_ContestMaster.query.get(contest_id)
    return render_template("contest_detail.html",user=current_user, contest_detail=contest_detail)

# コンテスト応募
@bp.route("/apply/<int:contest_id>")
def apply(contest_id):
    apply = T_ContestMaster.query.get(contest_id)
    return render_template("apply.html",user=current_user , apply=apply)

# コンテスト応募投稿
@bp.route('/apply_upload/<int:contest_id>',methods=['GET','POST'])
def apply_upload(contest_id):
    if request.method == 'POST':
        title = request.form.get('title')
        comment = request.form.get('comment')
        apply_image = request.files['prof-image']
        contest_master = T_ContestMaster.query.get(contest_id)
        if apply_image:
            apply_file = secure_filename(apply_image.filename)
            apply_image.save(os.path.join(current_app.config['UPLOAD_FOLDER_CONTEST'],apply_file))
            
        contest = T_Contest(
            F_ContestTitle = title,
            F_ContestComment = comment,
            F_ContestImage = apply_file,
            F_UserID = current_user.F_UserID,
            F_ContestMasterID = contest_master.F_ContestMasterID
        )
        
        db.session.add(contest)
        db.session.commit()
    return redirect('/contest')

# 譲渡会
@bp.route("/assignment")
def assignment():
    return render_template("assignment.html", user=current_user)

# コミュニティルーム
@bp.route("/community")
@login_required
def community():
    
    user_chat = T_Chat.query.filter((T_Chat.F_SenderID == current_user.F_UserID) | (T_Chat.F_ReceiverID == current_user.F_UserID))
    
    last_message = {}
    for chat in user_chat:
        other_user_id = chat.F_SenderID if chat.F_SenderID != current_user.F_UserID else chat.F_ReceiverID
        if other_user_id not in last_message or chat.F_ChatTime > last_message[other_user_id]['timestamp']:
            last_message[other_user_id]={
                'timestamp':chat.F_ChatTime,
                'message':chat.F_ChatContest
            }
    
    users = {}
    for user_id in last_message.keys():
        user = T_User.query.get(user_id)
        users[user_id] = user
        

    return render_template("community.html",user=current_user , last_message=last_message,users=users)


# チャットメイン
@bp.route('/community_mein/<int:receiver_id>', methods=['GET','POST'])
def community_mein(receiver_id):
    if request.method == 'POST':
        message = request.form.get('chat_input')
        sendimg = request.files.get('sendimg')
        sender_id = current_user.F_UserID
        
        send_image=None
        if sendimg and sendimg.filename!= '':
            send_image = secure_filename(sendimg.filename)
            sendimg.save(os.path.join(current_app.config['UPLOAD_FOLDER_CHAT'],send_image))
        
        new_message = T_Chat(
            F_SenderID = sender_id,
            F_ReceiverID = receiver_id,
            F_ChatContest = message,
            F_ChatImage = send_image,
            F_ChatTime = datetime.utcnow()
        )
        
        db.session.add(new_message)
        db.session.commit()
    receiver = T_User.query.get(receiver_id)
    messages = T_Chat.query.filter(((T_Chat.F_SenderID == current_user.F_UserID) & (T_Chat.F_ReceiverID == receiver_id)) | ((T_Chat.F_SenderID == receiver_id) & (T_Chat.F_ReceiverID == current_user.F_UserID))).order_by(T_Chat.F_ChatTime)
    
    user_chat = T_Chat.query.filter((T_Chat.F_SenderID == current_user.F_UserID) | (T_Chat.F_ReceiverID == current_user.F_UserID))
    
    last_message = {}
    for chat in user_chat:
        other_user_id = chat.F_SenderID if chat.F_SenderID != current_user.F_UserID else chat.F_ReceiverID
        if other_user_id not in last_message or chat.F_ChatTime > last_message[other_user_id]['timestamp']:
            last_message[other_user_id]={
                'timestamp':chat.F_ChatTime,
                'message':chat.F_ChatContest
            }
    users = {}
    for user_id in last_message.keys():
        user = T_User.query.get(user_id)
        users[user_id] = user
    return render_template('community.html',user=current_user, receiver=receiver, messages=messages , users=users)

# 履歴関連
# お気に入り
@bp.route("/favorite/<int:exhibit_id>", methods=['POST'])
@login_required
def favorite(exhibit_id):
    favorite = T_Favorite.query.filter_by(user_id=current_user.F_UserID,exhibit_id=exhibit_id).first()
    
    if favorite:
        db.session.delete(favorite)
        
    else:
        new_favorite = T_Favorite(user_id=current_user.F_UserID, exhibit_id=exhibit_id)
        db.session.add(new_favorite)
        db.session.commit()
    return redirect("/top")

# お気に入り表示
@bp.route('/favorites')
@login_required
def favorites():
    favorites_exhibit = T_Exhibit.query.join(T_Favorite,T_Favorite.exhibit_id == T_Exhibit.F_ExID).filter(T_Favorite.user_id == current_user.F_UserID).all()
    return render_template('favorite.html',favorites_exhibit=favorites_exhibit , user=current_user)

# 閲覧履歴
@bp.route("/browsing")
def browsing():
    return render_template("browsing.html")

# 購入履歴
@bp.route("/listing_list")
def listing_list():
    cart = T_Cartlist.query.filter_by(F_UserID=current_user.F_UserID).all()
    
    
    exhibit_info = []
    for carts in cart:
        exhibit = T_Exhibit.query.get(carts.F_ExID)
        user = T_User.query.get(exhibit.F_UserID)
        exhibit_info.append((exhibit,user))
        
    num_list = len(exhibit_info)
    return render_template("listing_list.html",user=current_user, exhibit_info=exhibit_info , num_list=num_list)

# 出品リスト
@bp.route("/exhibition_list",methods=['GET','POST'])
def exhibition_list():
    if request.method == 'POST':
        
        exhibition = request.form.get('checkbox-001')
        sold = request.form.get('checkbox-002')
        trial = request.form.get('checkbox-003')
        
        query = T_Exhibit.query.filter(F_EXhibitType=1)
        
        if not exhibition:
            query = query.filter(T_Exhibit.F_EXhibitType==1)
        
        if not sold :
            query = query.filter(T_Exhibit)
            
        if not trial:
            query = query.filter(T_Exhibit.F_EXhibitType==2)
        
        products = query.all()
        
        return render_template("exhibition_list.html",products=products,user=current_user)
    exhibit = T_Exhibit.query.filter_by(F_EXhibitType=1)
    demoexhibit = T_Exhibit.query.filter_by(F_EXhibitType=2)
    
    num_exhibit =len(exhibit)
    return render_template("exhibition_list.html",user=current_user,exhibit=exhibit, demoexhibit=demoexhibit , num_exhibit=num_exhibit)

# 売上履歴
@bp.route("/earnings_history")
def earnings_history():
    
    sales = T_Cartlist.query.all()
    
    sales_info = []
    
    for purchase in sales:
        exhibit = T_Exhibit.query.get(purchase.F_ExID)
        user = T_User.query.get(exhibit.F_UserID)
        
        sales_info.append((exhibit, user))
        
    return render_template("earnings_history.html", user=current_user , sales_info=sales_info)

# 掲載履歴
@bp.route("/petpublish_hiatory")
def petpublish_history():
    return render_template("petpublish_history.html" , user=current_user)

# 出品履歴
@bp.route("/listing_history")
def listing_history():
    user_id = current_user.F_UserID
    post_exhibit = T_Exhibit.query.filter_by(F_UserID =user_id, F_ExhibitType=2).all()
    return render_template("listing_list.html",post_exhibit=post_exhibit , user=current_user)


# その他
# ポイント管理
@bp.route("/point")
def point():
    
    user = current_user.F_UserID
    points = sum(T_Point.query.filter_by(F_UserID = user).all())
    return render_template("point.html" , points=points , user=user)

# メールボックス
@bp.route("/mailbox")
def mailbox():
    return render_template("mailbox.html")

# お知らせ
@bp.route("/notice")
def notice():
    return render_template("notice.html" , user=current_user)

# 設定
@bp.route("/setting")
def setting():
    return render_template("setting.html" , user=current_user)

# 着せ替え
@bp.route("/dressup")
def dressup():
    return render_template("dressup.html")

# Q&A
@bp.route("/qa")
def qa():
    return render_template("qa.html", user=current_user)

# 問い合わせ
@bp.route("/inquiry")
def inquiry():
    return render_template("inquiry.html" , user=current_user)




# テーブルメンテナンス
@bp.route("/maintenance")
def maintenance():
    return render_template("maintenance.html", user=current_user)

