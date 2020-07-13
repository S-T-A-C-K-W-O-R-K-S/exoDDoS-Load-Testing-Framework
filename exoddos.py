import csv, random

from locust import between, HttpUser

from pathlib import Path

from environment.exoddos import exoddos

from hooks.locust_on_init import on_init
from hooks.locust_on_request_failure import on_request_failure
from hooks.locust_on_test_start import on_test_start
from hooks.locust_on_test_stop import on_test_stop

from events.locust_on_start import on_start_setup
from events.locust_on_stop import on_stop_teardown

from tasksets.admin_taskset import Admin
from tasksets.baskets_taskset import Baskets
from tasksets.bulletin_boards_taskset import BulletinBoards
from tasksets.qde_taskset import QDE
from tasksets.reports_taskset import Reports
from tasksets.search_taskset import Search
from tasksets.workflows_taskset import Workflows


class CbpmUser(HttpUser):

    tasks = {Admin: 1, Baskets: 1, BulletinBoards: 1, QDE: 1, Reports: 1, Search: 1, Workflows: 1}
    # TODO: Convert Requests With Nested Functions Into SequentialTaskSets

    host = exoddos.host
    wait_time = between(1.0, 2.5)

    def __init__(self, environment):
        super(CbpmUser, self).__init__(environment)

        self.username = "NO_USERNAME"
        self.password = "NO_PASSWORD"
        self.session_id = "NO_SESSION"
        self.session_cookie = "NO_COOKIE"
        self.collaboration_id = "NO_COLLABORATION"

        self.has_elevated_privileges = None

        if len(exoddos.user_pool) == 0:
            with open(Path(exoddos.credentials)) as stream:
                reader = csv.reader(stream)
                exoddos.user_pool = list(reader)
                random.shuffle(exoddos.user_pool)

    def on_start(self):  # on_start is called when the user spawns, before the execution of any task
        on_start_setup(self)

    def on_stop(self):  # on_stop is called when the user is being released, after the tasks have executed
        on_stop_teardown(self)
