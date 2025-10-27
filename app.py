from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

# Choose a Bootswatch theme here:
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # Example: cerulean, flatly,
# darkly

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))


with app.app_context():
    db.create_all()

admin = Admin(app, name='My Admin Panel')
admin.add_view(ModelView(User, db.session, endpoint='user'))

if __name__ == '__main__':
    app.run(debug=True)
