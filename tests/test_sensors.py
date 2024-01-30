from os import getenv
from urllib.parse import urljoin

import pytest


def test_mock_get_sensors_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_sensors_general_info()

    m.assert_called_once_with(
        "GET",
        urljoin(getenv("iccpro_host"), "iccpro/api/sensors"),
    )


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_sensors_general_info(iccpro):
    assert iccpro.get_sensors_general_info()


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_sensors_current_data(iccpro):
    assert iccpro.get_sensors_current_data()


def test_get_sensors_historical_data_error(iccpro):
    with pytest.raises(RuntimeError):
        iccpro.get_sensors_historical_data()
