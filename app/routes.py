from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index/username')
def index(username=None):
	if username == None:
		return redirect('/login')
	return render_template('index.html', title='Home', username=username)

@app.route('/login')
def login():
	return render_template('login.html', title="Login")