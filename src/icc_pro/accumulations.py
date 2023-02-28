from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response, required_kwargs


class AccumulationsMixin:
    url = "iccpro/api/accumulation"

    @required_kwargs("fromdatetime", "todatetime", "resolution")
    @process_response
    def get_valves_historical_accumulations(self, **kwargs):
        url = urljoin(self.host, f"{AccumulationsMixin.url}/valves")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)

    @required_kwargs("fromdatetime", "todatetime", "resolution")
    @process_response
    def get_meters_historical_accumulations(self, **kwargs):
        url = urljoin(self.host, f"{AccumulationsMixin.url}/meters")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)
