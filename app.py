from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Создание приложения Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.secret_key = 'mysecretkey'
db = SQLAlchemy(app)

# Определим модель для базы данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))

# Настройка админки
admin = Admin(app, name='My Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session, endpoint='user'))

if __name__ == '__main__':
    app.run(debug=True)
