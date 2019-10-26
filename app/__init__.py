import os
import urllib.parse 
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_migrate import Migrate
import pyodbc

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=haxx.database.windows.net;DATABASE=UserDatabase;UID=haxx;PWD=HackGT2019")


# initialization
app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
#migrate = Migrate(app, db)

from app import routes, models