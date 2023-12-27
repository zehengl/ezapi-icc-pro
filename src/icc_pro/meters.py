from urllib.parse import urljoin

from .core import process_response


class MetersMixin:
    url = "iccpro/api/meters"

    @process_response
    def get_meters_general_info(self):
        url = urljoin(self.host, MetersMixin.url)
        return self.make_request("GET", url)
