from os import getenv

import pytest
from dotenv import load_dotenv

from icc_pro import ICC_PRO

load_dotenv()


@pytest.fixture()
def iccpro():
    host = getenv("iccpro_host", "http://localhost")
    username = getenv("iccpro_username", "username")
    password = getenv("iccpro_password", "password")
    client_id = getenv("iccpro_client_id", "client_id")
    client_secret = getenv("iccpro_client_secret", "client_secret")

    return ICC_PRO(host, username, password, client_id, client_secret)
