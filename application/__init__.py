from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import secret_key

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = "SECRET_KEY"

app.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY= secret_key.SECRET_KEY
)

db = SQLAlchemy(app)

from application import routes