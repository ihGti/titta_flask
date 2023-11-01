from flask import Flask , request , redirect , render_template , Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from project import db , create_app

bp = Blueprint('main',__name__)
app = create_app()

# トップページ
@app.route("/top")
@login_required
def index():
    return render_template("index.html")



# user関連
# 会員登録
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.methods=="POST":
        username = request.form.get('username')
    return render_template("signin.html")

# ログインページ
@app.route("/login")
def login():
    return render_template("login.html")

# 登録完了
@app.route("/cor")
def cor():
    return render_template("cor.html")

# マイページ
@app.route("/myprof")
def myprof():
    return render_template("my_profile.html")

# マイページ編集
@app.route("/prof-egit")
def prof_edit():
    return render_template("profile_edit.html")

# 他者プロフ
@app.route("/userprof")
def user_prof():
    return render_template("user_profile.html")


# 出品関連
# 本出品
@app.route("/exhibit")
def exhibit():
    return render_template("exhibit.html")

# 出品完了
@app.route("/exhibit_con")
def exhibit_con():
    return render_template("exhibit_con.html")

# お試し出品
@app.route("/exhibit_trial")
def exhibit_trial():
    return render_template("exhibit_trial.html")

# 商品関連
# 商品一覧
@app.route("/product")
def product():
    return render_template("product.html")

# 商品詳細
@app.route("/product_detail")
def product_detail():
    return render_template("product_detail.html")


# 目玉機能
# 里親掲示板
@app.route("/foster_board")
def foster_board():
    return render_template("foster_board.html")

# 迷子掲示板
@app.route("/lost_petboard")
def lost_petboard():
    return render_template("lost_petboard.html")

# 里親投稿
@app.route("/foster_post")
def foster_post():
    return render_template("foster_post.html")

# 迷子投稿
@app.route("/lost_post")
def lost_post():
    return render_template("lost_post.html")

# 里親詳細
@app.route("/foster_detail")
def foster_detail():
    return render_template("foster_detail.html")

# 迷子詳細
@app.route("/lost_detail")
def lost_detail():
    return render_template("lost_detail.html")

# ペット一覧
@app.route("/reg_pet")
def pet_list():
    return render_template("reg_pet.html")

# コンテスト
@app.route("/contest")
def contest():
    return render_template("contest.html")

# 譲渡会
@app.route("/assignment")
def assignment():
    return render_template("assignment.html")

# コミュニティルーム
@app.route("/community")
def community():
    return render_template("community.html")


# 履歴関連
# お気に入り
@app.route("/favorite")
def favorite():
    return render_template("favorite.html")

# 閲覧履歴
@app.route("/browsing")
def browsing():
    return render_template("browsing.html")

# 購入履歴
@app.route("/listing_list")
def listing_list():
    return render_template("listing_list.html")

# 出品リスト
@app.route("/exhibition_list")
def exhibition_list():
    return render_template("exhibition_list.html")

# 売上履歴
@app.route("/earnings_history")
def earnings_history():
    return render_template("earnings_history.html")

# 掲載履歴
@app.route("/petpublish_hiatory")
def petpublish_history():
    return render_template("petpublish_history.html")

# 出品履歴
@app.route("/listing_history")
def listing_history():
    return render_template("listing_list.html")


# その他
# ポイント管理
@app.route("/point")
def point():
    return render_template("point.html")

# メールボックス
@app.route("/mailbox")
def mailbox():
    return render_template("mailbox.html")

# お知らせ
@app.route("/notice")
def notice():
    return render_template("notice.html")

# 設定
@app.route("/setting")
def setting():
    return render_template("setting.html")

# 着せ替え
@app.route("/dressup")
def dressup():
    return render_template("dressup.html")

# Q&A
@app.route("/qa")
def qa():
    return render_template("qa.html")

# 問い合わせ
@app.route("/inquiry")
def inquiry():
    return render_template("inquiry.html")



# 管理者ページ
@app.route("/admin")
def admin():
    return render_template("adminnistrator.html")

# テーブルメンテナンス
@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")
