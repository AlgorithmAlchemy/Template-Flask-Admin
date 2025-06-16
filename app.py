from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Настройка приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

# Выбери тему Bootswatch здесь:
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # например, cerulean, flatly, darkly и др.

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))

with app.app_context():
    db.create_all()

# Инициализируем админку (без передачи template_mode или theme)
admin = Admin(app, name='My Admin Panel')
admin.add_view(ModelView(User, db.session, endpoint='user'))

if __name__ == '__main__':
    app.run(debug=True)
