class TokenMixin:

    url = "iccpro/token"

    def get_token(self, host, username, password, client_id, client_secret):
        pass

    def refresh_token(self, host, client_id, client_secret, refresh_token):
        pass
