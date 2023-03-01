from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class ProgramsMixin:
    url = "iccpro/api/programs"

    @process_response
    def get_programs_general_info(self):
        url = urljoin(self.host, ProgramsMixin.url)
        return self.make_request("GET", url)

    @process_response
    def get_programs_detailed_info(self, **kwargs):
        url = urljoin(self.host, f"{ProgramsMixin.url}/getprograms")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        return self.make_request("GET", req.url)

    def set_programs_status(self):
        raise NotImplementedError

    def set_programs_preset_data(self):
        raise NotImplementedError

    def irrigate_now_program_group(self):
        raise NotImplementedError

    def reset_program_alarm(self):
        raise NotImplementedError

    def change_program_depth(self):
        raise NotImplementedError
