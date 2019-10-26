import os
import urllib.parse 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=haxx.database.windows.net;DATABASE=UserDatabase;UID=haxx;PWD=HackGT2019")


# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

from app import routes