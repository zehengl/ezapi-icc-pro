from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response, required_kwargs


class SensorsMixin:
    url = "iccpro/api/sensors"

    @process_response
    def get_sensors_general_info(self):
        url = urljoin(self.host, SensorsMixin.url)
        return self.make_request("GET", url)

    @process_response
    def get_sensors_current_data(self, **kwargs):
        url = urljoin(self.host, f"{SensorsMixin.url}/current")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)

    @required_kwargs("fromdatetime", "todatetime", "resolution")
    @process_response
    def get_sensors_historical_data(self, **kwargs):
        url = urljoin(self.host, f"{SensorsMixin.url}/history")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)
