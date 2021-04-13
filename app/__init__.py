from flask import Flask
from config import config_selector
from os import getenv


def create_app():
    app = Flask(__name__)
    config_setup = getenv("FLASK_ENV")
    app.config.from_object(config_selector[config_setup])
    return app