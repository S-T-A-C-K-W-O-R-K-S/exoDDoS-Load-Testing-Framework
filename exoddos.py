import csv

from locust import between, HttpUser
from locust.exception import StopUser

from pathlib import Path

from environment.exoddos import exoddos

from events.locust_on_init import on_init
from events.locust_on_request_failure import on_request_failure
from events.locust_on_start import on_start_setup
from events.locust_on_stop import on_stop_teardown
from events.locust_on_test_start import on_test_start
from events.locust_on_test_stop import on_test_stop

from tasksets.baskets_taskset import Baskets
from tasksets.bulletin_boards_taskset import BulletinBoards
from tasksets.qde_taskset import QDE
from tasksets.reports_taskset import Reports
from tasksets.search_taskset import Search
from tasksets.workflows_taskset import Workflows


class CbpmUser(HttpUser):

    tasks = {
        Baskets: 1,
        BulletinBoards: 1,
        QDE: 1,
        Reports: 1,
        Search: 1,
        Workflows: 1
    }  # TODO: Convert Requests With Nested Functions Into SequentialTaskSets

    host = exoddos.host
    wait_time = between(1.0, 2.5)

    def __init__(self, environment):
        super(CbpmUser, self).__init__(environment)

        self.username = "NO_USERNAME"
        self.password = "NO_PASSWORD"
        self.session_id = "NO_SESSION"
        self.session_cookie = "NO_COOKIE"
        self.user_collaboration_id = "NO_COLLABORATION"

        if len(exoddos.user_pool) == 0:
            with open(Path(exoddos.credentials)) as stream:
                reader = csv.reader(stream)
                exoddos.user_pool = list(reader)

    def on_start(self):  # on_start is called when the user spawns, before the execution of any task

        if len(exoddos.user_pool) > 0:
            
            try:
                self.username, self.password = exoddos.user_pool.pop()  # credentials will be used from last to first

                self.session_data = on_start_setup(self, self.username, self.password)

                self.session_id = self.session_data["session_id"]
                self.session_cookie = self.session_data["session_cookie"]
                self.user_collaboration_id = self.session_data["user_collaboration_id"]

            except:
                if exoddos.recycle_failed_logins:
                    exoddos.user_pool.append([self.username, self.password])
                    
                raise StopUser

        elif len(exoddos.user_pool) == 0:
            print("The Swarm Has Exceeded The Number Of Available Credentials")
            raise StopUser

    def on_stop(self):  # on_stop is called when the user is being released, after the tasks have executed
        on_stop_teardown(self, self.username, self.session_id, self.session_cookie)
