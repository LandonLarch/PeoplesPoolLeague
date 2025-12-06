from flask import Flask
from decouple import config
from .extensions import db, migrate
from .routes import main

def create_app():
    app = Flask(__name__)
    # load config from .env
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SECRET_KEY']            = config('SECRET_KEY')
    app.config['ENV']                   = config('FLASK_ENV', default='production')

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register routes
    app.register_blueprint(main)

    return app
