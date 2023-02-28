def test_acquire_token(iccpro):
    assert iccpro.acquire_token()


def test_refresh_token(iccpro):
    assert iccpro.refresh_token()
