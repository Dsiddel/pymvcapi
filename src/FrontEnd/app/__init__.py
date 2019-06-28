from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

with open('app\config.json') as f:
    config = json.load(f)

app = Flask(__name__)
app.config.update(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models