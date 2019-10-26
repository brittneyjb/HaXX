from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

<<<<<<< HEAD
class Users(UserMixin, db.Model):
    id = db.Column(db.String(64), primary_key=True)
=======
class User(UserMixin, db.Model):
    id = db.Column(db.String(64), primary_key=True, unique=True)
>>>>>>> dc384799a323a552b83169a71e1255ec2cd373f6
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
<<<<<<< HEAD
        return '<Users {}>'.format(self.id)    
=======
    	return '<User {}>'.format(self.id)    
>>>>>>> dc384799a323a552b83169a71e1255ec2cd373f6

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
<<<<<<< HEAD
        return Users.query.get(id)
=======
    	return User.query.get(int(id))
>>>>>>> dc384799a323a552b83169a71e1255ec2cd373f6
