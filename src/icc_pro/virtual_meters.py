from urllib.parse import urljoin

from .core import process_response


class VirtualMetersMixin:
    url = "iccpro/api/virtualmeters"

    @process_response
    def get_virtual_meters_general_info(self):
        url = urljoin(self.host, VirtualMetersMixin.url)
        return self.make_request("GET", url)
