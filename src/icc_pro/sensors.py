from urllib.parse import urljoin

from .core import process_response


class SensorsMixin:
    url = "iccpro/api/sensors"

    @process_response
    def get_sensors_general_info(self):
        url = urljoin(self.host, SensorsMixin.url)
        return self.make_request("GET", url)

    def get_sensors_current_data(self):
        pass

    def get_sensors_historical_data(self):
        pass
