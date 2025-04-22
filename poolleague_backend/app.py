from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# existing config…
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app.config['SECRET_KEY']            = config('SECRET_KEY')
app.config['ENV']                   = config('FLASK_ENV', default='production')

# Set up DB and migrations
db      = SQLAlchemy(app)
migrate = Migrate(app, db)
