import json, os

from locust import events
from locust.exception import StopUser

from environment.exoddos import exoddos
from environment.utility import graylog, utility


@events.request_failure.add_listener
def on_request_failure(request_type, name, response_time, exception, **kwargs):

    if exoddos.use_graylog:

        graylog_message = {
            "RequestType": f"{request_type}",
            "RequestName": f"{name}",
            "RequestURL": f"{exception.request.url}",
            "ResponseTime": response_time,
            "ResponseCode": exception.response.status_code,
            "Response": f"{exception.response.text}",
            "Exception": f"{exception}"
        }

        graylog.logger.error(json.dumps(graylog_message, indent = 4))

    if exoddos.debug_mode:
        print(utility.timestamp(utility) + f"[DEBUG] :: Exception {request_type} Request URL: {exception.request.url}")
        print(utility.timestamp(utility) + f"[DEBUG] :: Exception Response Code: {exception.response.status_code}")
        print(utility.timestamp(utility) + f"[DEBUG] :: Exception Response Message: {exception.response.json()['Message']}")
