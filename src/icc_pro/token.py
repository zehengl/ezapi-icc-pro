from urllib.parse import urljoin

from .core import process_response


class TokenMixin:
    url = "iccpro/token"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
    }

    @process_response
    def acquire_token(self):
        url = urljoin(self.host, TokenMixin.url)
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        return self.make_request("POST", url, headers=TokenMixin.headers, data=data)

    @process_response
    def refresh_token(self):
        url = urljoin(self.host, TokenMixin.url)
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self._refresh_token,
        }
        return self.make_request("POST", url, headers=TokenMixin.headers, data=data)
