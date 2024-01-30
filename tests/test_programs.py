from os import getenv
from urllib.parse import urljoin

import pytest


def test_mock_get_programs_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_programs_general_info()

    m.assert_called_once_with(
        "GET",
        urljoin(getenv("iccpro_host"), "iccpro/api/programs"),
    )


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_programs_general_info(iccpro):
    assert iccpro.get_programs_general_info()


@pytest.mark.skipif(not getenv("iccpro_host"), reason="Missing config")
def test_get_programs_detailed_info(iccpro):
    assert iccpro.get_programs_detailed_info()


def test_set_programs_status_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.set_programs_status()


def test_set_programs_preset_data_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.set_programs_preset_data()


def test_irrigate_now_program_group_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.irrigate_now_program_group()


def test_reset_program_alarm_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.reset_program_alarm()


def test_change_program_depth_error(iccpro):
    with pytest.raises(NotImplementedError):
        iccpro.change_program_depth()
