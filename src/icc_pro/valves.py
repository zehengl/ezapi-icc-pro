from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class ValvesMixin:
    url = "iccpro/api/valves"

    @process_response
    def get_valves_general_info(self):
        url = urljoin(self.host, ValvesMixin.url)
        return self.make_request("GET", url)

    @process_response
    def get_valves_gis_info(self, **kwargs):
        url = urljoin(self.host, f"{ValvesMixin.url}/getgisdata")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)

    @process_response
    def get_valves_status(self, **kwargs):
        url = urljoin(self.host, f"{ValvesMixin.url}/getgisstatus")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)

    def create_valves_snapshot(self):
        raise NotImplementedError

    def update_valves_snapshot(self):
        raise NotImplementedError
