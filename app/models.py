from app import db
from app import app
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(128), index = True, unique = True)
    password = db.Column(db.String(1024), index = True, unique = False)

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)
        db.session.commit()

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)
