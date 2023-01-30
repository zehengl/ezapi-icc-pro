from icc_pro import ICC_PRO


def test_icc_pro_init():
    host = "host"
    username = "username"
    password = "password"
    client_id = "client_id"
    client_secret = "client_secret"

    icc_pro = ICC_PRO(host, username, password, client_id, client_secret)

    assert icc_pro.host == host
    assert icc_pro.username == username
    assert icc_pro.password == password
    assert icc_pro.client_id == client_id
    assert icc_pro.client_secret == client_secret
