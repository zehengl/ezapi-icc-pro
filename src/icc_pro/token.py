from urllib.parse import urljoin

from .core import process_response


class TokenMixin:
    url = "iccpro/token"

    @process_response
    def acquire_token(self):
        url = urljoin(self.host, TokenMixin.url)
        headers = {
            "content-type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        return self.make_request("POST", url, headers=headers, data=data)

    def refresh_token(self, host, client_id, client_secret, refresh_token):
        pass
