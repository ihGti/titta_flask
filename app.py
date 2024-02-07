from project import create_app

app = create_app()

# 作成者名前
# app.py = 山本
# models.py = 山本
# __init__.py = 山本
# views.py = 山本
# config.py = 山本

if __name__ == '__main__':
    app.run(debug=True,port=5000)