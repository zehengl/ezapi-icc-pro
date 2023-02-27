import pytest
from os import getenv
from dotenv import load_dotenv

load_dotenv()

from icc_pro import ICC_PRO


@pytest.fixture()
def iccpro():
    host = getenv("host", "http://localhost")
    username = getenv("username", "username")
    password = getenv("password", "password")
    client_id = getenv("client_id", "client_id")
    client_secret = getenv("client_secret", "client_secret")

    return ICC_PRO(host, username, password, client_id, client_secret)
