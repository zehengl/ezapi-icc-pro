from os import getenv
from urllib.parse import urljoin

import pytest


def test_mock_get_valves_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_valves_general_info()

    m.assert_called_once_with(
        "GET",
        urljoin(getenv("iccpro_host"), "iccpro/api/valves"),
    )


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_valves_general_info(iccpro):
    assert iccpro.get_valves_general_info()


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_valves_gis_info(iccpro):
    assert iccpro.get_valves_gis_info()


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_valves_status(iccpro):
    assert iccpro.get_valves_status()


def test_create_valves_snapshot_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.create_valves_snapshot()


def test_update_valves_snapshot_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.update_valves_snapshot()
