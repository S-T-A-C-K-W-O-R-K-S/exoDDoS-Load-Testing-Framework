import requests

from locust import between, HttpUser

from environment.exoddos import exoddos

from hooks.locust_on_init import on_init
from hooks.locust_on_request_failure import on_request_failure
from hooks.locust_on_test_start import on_test_start
from hooks.locust_on_test_stop import on_test_stop

from events.locust_on_start import on_start_setup
from events.locust_on_stop import on_stop_teardown

from tasksets.csec_taskset import CSEC


class CsdbUser(HttpUser):

    requests.urllib3.disable_warnings()  # Disable SSL Warnings

    tasks = [CSEC]

    host = exoddos.host
    wait_time = between(1.0, 2.5)

    def __init__(self, environment):
        super(CsdbUser, self).__init__(environment)

        self.username = "NO_USERNAME"
        self.user_id = "NO_USER_ID"
        self.email = "NO_EMAIL"
        self.role = "NO_ROLE"
        self.session_id = "NO_SESSION"

        self.cookie_jar = []
        self.cookie_header = "NO_COOKIE"

    def on_start(self):  # on_start is called when the user spawns, before the execution of any task
        on_start_setup(self)

    def on_stop(self):  # on_stop is called when the user is being released, after the tasks have executed
        on_stop_teardown(self)
