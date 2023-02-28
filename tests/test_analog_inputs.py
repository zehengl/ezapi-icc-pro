from os import getenv
from urllib.parse import urljoin
import pytest


def test_mock_get_analog_inputs_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_analog_inputs_general_info()

    m.assert_called_once_with(
        "GET",
        urljoin(getenv("iccpro_host", "http://localhost/"), "iccpro/api/analoginputs"),
    )


def test_get_analog_inputs_general_info(iccpro):
    assert iccpro.get_analog_inputs_general_info()


def test_get_analog_inputs_current_data(iccpro):
    assert iccpro.get_analog_inputs_current_data()


def test_get_analog_inputs_historical_data_error(iccpro):
    with pytest.raises(RuntimeError):
        iccpro.get_analog_inputs_historical_data()
