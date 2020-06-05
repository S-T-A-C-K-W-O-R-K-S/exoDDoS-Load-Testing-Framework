from imports.environment import env
from locust import events


@events.request_failure.add_listener
def on_request_failure(request_type, name, response_time, exception, **kwargs):
    if env.debug_mode:
        print(f"[DEBUG] :: Exception {request_type} Request URL: {exception.request.url}")
        print(f"[DEBUG] :: Exception Response Code: {exception.response.status_code}")
        print(f"[DEBUG] :: Exception Response Message: {exception.response.json()['Message']}")
