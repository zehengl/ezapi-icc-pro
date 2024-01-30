from os import getenv

import pytest
from dotenv import load_dotenv

from icc_pro import ICC_PRO

load_dotenv()


@pytest.fixture()
def iccpro():
    host = getenv("iccpro_host")
    username = getenv("iccpro_username")
    password = getenv("iccpro_password")
    client_id = getenv("iccpro_client_id")
    client_secret = getenv("iccpro_client_secret")

    if all([host, username, password, client_id, client_secret]):
        login = True
    else:
        login = False

    return ICC_PRO(host, username, password, client_id, client_secret, login=login)
