# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
#!flask\Scripts\python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models