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


def required_kwargs(*required_kwargs):
    """
    Decorator to check if criteria of required kwargs are met
    Raises:
        RuntimeError: a bad client request
    Returns:
        func: decorated function
    """

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        if all([kwarg in kwargs for kwarg in required_kwargs]):
            return wrapped(*args, **kwargs)

        msg = f"required kwargs: {' and '.join(required_kwargs)}"

        raise RuntimeError(f"{msg}")

    return wrapper
