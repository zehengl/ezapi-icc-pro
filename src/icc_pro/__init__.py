from urllib.parse import urljoin

import requests

from .accumulations import AccumulationsMixin
from .analog_inputs import AnalogInputsMixin
from .meters import MetersMixin
from .programs import ProgramsMixin
from .sensors import SensorsMixin
from .token import TokenMixin
from .valves import ValvesMixin
from .virtual_meters import VirtualMetersMixin

mixins = [
    AccumulationsMixin,
    AnalogInputsMixin,
    MetersMixin,
    ProgramsMixin,
    SensorsMixin,
    TokenMixin,
    ValvesMixin,
    VirtualMetersMixin,
]


class ICC_PRO(*mixins):
    url = None

    def __init__(self, host, username, password, client_id, client_secret, login=True):
        self.host = host
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret

        self.session = requests.Session()

        if login:
            self.set_tokens(self.acquire_token())

    def set_tokens(self, resp):
        self._access_token = resp.get("access_token")
        self._refresh_token = resp.get("refresh_token")
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self._access_token}",
            }
        )

    def renew(self):
        self.set_tokens(self.refresh_token())

    @classmethod
    def list_generic_endpoints(cls):
        return [(m.__name__[:-5], m.url) for m in mixins]

    def list_detailed_endpoints(self):
        return [(m.__name__[:-5], urljoin(self.host, m.url)) for m in mixins]

    def make_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)
