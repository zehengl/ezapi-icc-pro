import pytest

from icc_pro import ICC_PRO


@pytest.fixture()
def iccpro():
    host = "http://localhost"
    username = "username"
    password = "password"
    client_id = "client_id"
    client_secret = "client_secret"

    return ICC_PRO(host, username, password, client_id, client_secret)
