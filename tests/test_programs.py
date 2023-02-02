def test_get_programs_general_info(mocker, iccpro):
    m = mocker.patch("requests.Session.request")

    iccpro.get_programs_general_info()

    m.assert_called_once_with(
        "GET",
        f"http://localhost/iccpro/api/programs",
        json=None,
    )
