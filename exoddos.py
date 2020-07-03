import csv

from locust import between, HttpUser

from pathlib import Path

from environment.exoddos import exoddos

from hooks.locust_on_init import on_init
from hooks.locust_on_request_failure import on_request_failure
from hooks.locust_on_test_start import on_test_start
from hooks.locust_on_test_stop import on_test_stop

from tasksets.user_behaviour import UserBehaviour


class User(HttpUser):

    tasks = [UserBehaviour]
    wait_time = between(1.0, 2.5)
    host = exoddos.host

    def __init__(self, environment):
        super(User, self).__init__(environment)
        
        exoddos.env = self.environment
        # TODO: Find A More Elegant Way To Hook Into The Environment

        if len(exoddos.user_pool) == 0:
            with open(Path(exoddos.credentials)) as stream:
                reader = csv.reader(stream)
                exoddos.user_pool = list(reader)
