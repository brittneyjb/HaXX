from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
import datetime

class Users(UserMixin, db.Model):
    id = db.Column(db.String(64), primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Users {}>'.format(self.id)     

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return Users.query.get(id)
class Tasks(db.Model):
    id = db.Column(db.String())
    rating = db.Column(db.Integer())
    task = db.Column(db.String(120), primary_key=True)
    taskTime = db.Column(db.Float())
    dueDate = db.Column(db.Date())
    priority = db.Column(db.Float())
    def set_priority(self):
        self.priority = round(.4 * float(self.rating) + .5 * 1/float(self.dueDate.day - datetime.datetime.today().day) + .1 * float(self.taskTime), 4)
    def get_priority(self):
        return self.priority
    def rank_priority(self, other):
        return this.priority > other.priority
