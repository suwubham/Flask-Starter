from flask import Flask
import os

from app.routes.test import test_bp
from app.extensions import db, migrate
from app.models import *
from app.config import config


def create_app(config_name=None):
    app = Flask(__name__)

    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'testing')

    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(test_bp)

    @app.route("/")
    def root():
        return "Hello World"
    return app
