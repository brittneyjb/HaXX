from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange
from app.models import Users

class LoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, id):
        user = Users.query.filter_by(id=id.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class AddForm(FlaskForm):
    taskName = StringField('Task Title', validators=[DataRequired()])
    taskImportance = RadioField('Importance', choices=[('1','1'),('2','2'),('3','3'), ('4','4'), ('5','5')])
    taskTime = StringField('Length of Task (hours)', validators=[DataRequired(), NumberRange(0, 100)])
    taskDueDate = DateField('Due Date (YYYY-MM-DD)', validators=[DataRequired()])
