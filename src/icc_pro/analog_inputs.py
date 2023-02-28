from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response, required_kwargs


class AnalogInputsMixin:
    url = "iccpro/api/analoginputs"

    @process_response
    def get_analog_inputs_general_info(self):
        url = urljoin(self.host, AnalogInputsMixin.url)
        return self.make_request("GET", url)

    @process_response
    def get_analog_inputs_current_data(self, **kwargs):
        url = urljoin(self.host, f"{AnalogInputsMixin.url}/current")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)

    @required_kwargs("fromdatetime", "todatetime", "resolution")
    @process_response
    def get_analog_inputs_historical_data(self, **kwargs):
        url = urljoin(self.host, f"{AnalogInputsMixin.url}/history")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)
