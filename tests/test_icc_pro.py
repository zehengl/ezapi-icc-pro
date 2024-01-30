from os import getenv

from icc_pro import ICC_PRO


def test_icc_pro_init(iccpro):
    assert len(ICC_PRO.list_generic_endpoints()) == 8

    host = getenv("iccpro_host")
    username = getenv("iccpro_username")
    password = getenv("iccpro_password")
    client_id = getenv("iccpro_client_id")
    client_secret = getenv("iccpro_client_secret")

    assert iccpro.host == host
    assert iccpro.username == username
    assert iccpro.password == password
    assert iccpro.client_id == client_id
    assert iccpro.client_secret == client_secret

    assert len(iccpro.list_generic_endpoints()) == 8
    assert len(iccpro.list_detailed_endpoints()) == 8
