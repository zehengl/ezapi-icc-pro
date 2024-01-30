from os import getenv

import pytest


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_acquire_token(iccpro):
    assert iccpro.acquire_token()


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_refresh_token(iccpro):
    assert iccpro.refresh_token()
