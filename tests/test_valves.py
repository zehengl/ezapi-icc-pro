def test_get_valves_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_valves_general_info()

    m.assert_called_once_with(
        "GET",
        f"http://localhost/iccpro/api/valves",
        json=None,
    )
