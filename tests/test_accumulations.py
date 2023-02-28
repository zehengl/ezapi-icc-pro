import pytest


def test_get_valves_historical_accumulations_error(iccpro):
    with pytest.raises(RuntimeError):
        iccpro.get_valves_historical_accumulations()


def test_get_meters_historical_accumulations_error(iccpro):
    with pytest.raises(RuntimeError):
        iccpro.get_meters_historical_accumulations()
