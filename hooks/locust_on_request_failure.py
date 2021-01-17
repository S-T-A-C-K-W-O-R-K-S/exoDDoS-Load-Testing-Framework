import json, os

from locust import events
from locust.exception import StopUser

from environment.exoddos import exoddos
from environment.utility import utility


@events.request_failure.add_listener
def on_request_failure(request_type, name, response_time, exception, **kwargs):

    if exoddos.debug_mode:
        print(utility.timestamp(utility) + f"[DEBUG] :: Exception {request_type} Request URL: {exception.request.url}")
        print(utility.timestamp(utility) + f"[DEBUG] :: Exception Response Code: {exception.response.status_code}")
        print(utility.timestamp(utility) + f"[DEBUG] :: Exception Response Message: {exception.response.json()['Message']}")
