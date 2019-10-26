from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index(username=null):
	if user == null:
		return redirect(url_for(login))
	return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():

