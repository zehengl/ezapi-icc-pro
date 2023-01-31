from urllib.parse import urljoin

from .core import process_response


class ValvesMixin:

    url = "iccpro/api/valves"

    @process_response
    def get_valves_general_info(self):
        url = urljoin(self.host, ValvesMixin.url)
        return self.make_request("GET", url)

    def get_valves_gis_info(self):
        pass

    def get_valves_status(self):
        pass

    def create_valves_snapshot(self):
        pass

    def update_valves_snapshot(self):
        pass
