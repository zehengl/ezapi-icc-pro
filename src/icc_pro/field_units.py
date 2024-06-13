from urllib.parse import urljoin

from .core import process_response


class FieldUnitsMixin:
    url = "iccpro/api/fieldunits"

    @process_response
    def get_field_units_general_info(self):
        url = urljoin(self.host, FieldUnitsMixin.url)
        return self.make_request("GET", url)
