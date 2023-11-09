from project import create_app
from project.config import SQLALCHEMY_DATABASE_URI

SQLALCHEMY_DATABASE_URI = 'mysql://titta_project:2023$Iht!tta@localhost/titta_db'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)