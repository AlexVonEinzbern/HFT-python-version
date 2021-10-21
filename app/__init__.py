from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
CORS()

def init_app():
    """Construct the core app"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from . import routes #Import routes
        db.create_all()

        return app