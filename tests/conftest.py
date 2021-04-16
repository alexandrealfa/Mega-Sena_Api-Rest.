from pytest import fixture
from app import create_app


@fixture
def app():
    return create_app()



@fixture
def routes_bind(app):
    return  app.url_map.bind('')