import requests
import wrapt


@wrapt.decorator
def process_response(wrapped, instance, args, kwargs):
    try:
        resp = wrapped(*args, **kwargs)
    except (requests.ConnectionError, requests.Timeout) as e:
        raise Exception("Service Unavailable") from e
    else:
        resp.raise_for_status()
        return resp.json()
