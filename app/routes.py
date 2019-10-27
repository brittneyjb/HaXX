from app import app
from app import db
from flask import render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import flask
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Users, Tasks
from app.forms import LoginForm, RegistrationForm, AddForm
from queue import PriorityQueue
from sqlalchemy import *
priorities = PriorityQueue()

@app.route('/')
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    temp = PriorityQueue()
    for i in priorities.queue: temp.put(i)
    return render_template('dashboard.html', title='Home', Otasks=[],tasks=temp)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(id=form.id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(id=form.id.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/newTask', methods=['GET', 'POST'])
def newTask():
    form = AddForm()
    if form.validate_on_submit():
        task = Tasks(task = form.taskName.data, rating = form.taskImportance.data, dueDate = form.taskDueDate.data, taskTime = form.taskTime.data, id=current_user.id)
        task.set_priority()
        priorities.put((0 - task.get_priority(), (form.taskName.data, form.taskDueDate.data)))
        db.session.add(task)
        db.session.commit()
        flash('Task Added')
        return redirect(url_for('index'))
    return render_template('newTask.html', form=form)
