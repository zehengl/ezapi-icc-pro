from os import getenv

from icc_pro import ICC_PRO


def test_icc_pro_init(iccpro):
    assert len(ICC_PRO.list_generic_endpoints()) == 8

    host = getenv("host", "http://localhost")
    username = getenv("username", "username")
    password = getenv("password", "password")
    client_id = getenv("client_id", "client_id")
    client_secret = getenv("client_secret", "client_secret")

    assert iccpro.host == host
    assert iccpro.username == username
    assert iccpro.password == password
    assert iccpro.client_id == client_id
    assert iccpro.client_secret == client_secret

    assert len(iccpro.list_generic_endpoints()) == 8
    assert len(iccpro.list_detailed_endpoints()) == 8
