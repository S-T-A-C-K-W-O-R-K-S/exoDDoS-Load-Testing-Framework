from imports.environment import env
from locust.events import request_failure


def on_failure(request_type, name, response_time, exception, **kwargs):
    if env.debug_mode:
        print(f"[DEBUG] :: Exception {request_type} Request URL: {exception.request.url}")
        print(f"[DEBUG] :: Exception Response Code: {exception.response.status_code}")
        print(f"[DEBUG] :: Exception Response Message: {exception.response.json()['Message']}")

request_failure += on_failure


                                # # # # # # # # # # # # # # # # #
                                #                               #
                                #   ORDER OF EVENTS             #
                                #                               #
                                #       1. Locust SETUP         #
                                #       2. TaskSet SETUP        #
                                #       3. TaskSet ON_START     #
                                #       4. TaskSet TASKS...     #
                                #       5. TaskSet ON_STOP      #
                                #       6. TaskSet TEARDOWN     #
                                #       7. Locust TEARDOWN      #
                                #                               #
                                # # # # # # # # # # # # # # # # #
