from os import getenv


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("FLASK_DB_URI")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("FLASK_DB_URI")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("FLASK_DB_URI")


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}