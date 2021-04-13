from flask import Flask
from config import config_selector
from os import getenv

from app.configurations import database
from app.configurations import migration
from app.configurations import views
from app.configurations import serializer
from app.configurations import authentication


def create_app():

    app = Flask(__name__)
    config_setup = getenv("FLASK_ENV")
    app.config.from_object(config_selector[config_setup])
    database.init_app(app)
    migration.init_app(app)
    serializer.init_app(app)
    authentication.init_app(app)
    views.init_app(app)

    return app