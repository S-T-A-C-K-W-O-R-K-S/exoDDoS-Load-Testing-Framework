import csv, random

from locust import between, HttpUser
from locust.exception import StopUser

from pathlib import Path

from environment.exoddos import exoddos
from environment.utility import utility

from hooks.locust_on_init import on_init
from hooks.locust_on_request_failure import on_request_failure
from hooks.locust_on_test_start import on_test_start
from hooks.locust_on_test_stop import on_test_stop

from events.locust_on_start import on_start_setup
from events.locust_on_stop import on_stop_teardown

from tasksets.estr_taskset import ESTR


class EstrUser(HttpUser):

    tasks = [ESTR]

    host = exoddos.host
    wait_time = between(1.0, 2.5)

    def __init__(self, environment):
        super(EstrUser, self).__init__(environment)

        self.email = "test@user.estr"
        self.roles = "APPR_ESTER_ECB_Administrator"

        self.username = "NO_USERNAME"
        self.user_id = "NO_USER_ID"
        self.session_id = "NO_SESSION"
        self.business_date = "NO_BUSINESS_DATE"

        if exoddos.user_pool is None:
            with open(Path(exoddos.credentials)) as stream:
                reader = csv.reader(stream)
                exoddos.user_pool = list(reader)
                random.shuffle(exoddos.user_pool)

    def on_start(self):  # on_start is called when the user spawns, before the execution of any task
        on_start_setup(self)

    def on_stop(self):  # on_stop is called when the user is being released, after the tasks have executed
        on_stop_teardown(self)
