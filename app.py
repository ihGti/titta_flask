from project import create_app
from project.config import SQLALCHEMY_DATABASE_URI


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

if __name__ == '__main__':
    app.run(debug=True)