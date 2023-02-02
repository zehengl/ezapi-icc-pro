from urllib.parse import urljoin

from .core import process_response


class AnalogInputsMixin:
    url = "iccpro/api/analoginputs"

    @process_response
    def get_analog_inputs_general_info(self):
        url = urljoin(self.host, AnalogInputsMixin.url)
        return self.make_request("GET", url)

    def get_analog_inputs_current_data(self):
        pass

    def get_analog_inputs_historical_data(self):
        pass
