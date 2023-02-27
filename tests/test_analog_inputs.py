from os import getenv
from urllib.parse import urljoin


def test_get_analog_inputs_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_analog_inputs_general_info()

    m.assert_called_once_with(
        "GET",
        urljoin(getenv("host", "http://localhost/"), "iccpro/api/analoginputs"),
    )
