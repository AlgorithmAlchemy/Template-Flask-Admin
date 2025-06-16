from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, theme
from flask_admin.contrib.sqla import ModelView

# Инициализация Flask-приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'

# Выбери тему Bootswatch здесь:
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # например, cerulean, flatly, darkly и др.

# Инициализация базы данных
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))

# Создание всех таблиц в БД
with app.app_context():
    db.create_all()

# Инициализируем админку (без передачи template_mode или theme)
admin = Admin(app, name='My Admin Panel')
admin.add_view(ModelView(User, db.session, endpoint='user'))


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
