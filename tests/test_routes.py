from pytest import fail
from werkzeug.exceptions import NotFound


def test_route_user_exists(routes_bind):
    try:
        routes_bind.match('/user')
    except NotFound:
        fail("verify if route user wos declared")

