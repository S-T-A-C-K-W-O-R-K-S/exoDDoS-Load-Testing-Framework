from locust import tag, task, TaskSet

from tasks.baskets.get_workzone import get_workzone
from tasks.baskets.get_inbasket import get_inbasket
from tasks.baskets.get_outbasket import get_outbasket
from tasks.baskets.get_waste_basket import get_waste_basket


class Baskets(TaskSet):

    @task(1)
    @tag("baskets")
    def get_workzone_task(self):
        get_workzone(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)

    @task(1)
    @tag("baskets")
    def get_inbasket_task(self):
        get_inbasket(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)

    @task(1)
    @tag("baskets")
    def get_outbasket_task(self):
        get_outbasket(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)

    @task(1)
    @tag("baskets")
    def get_waste_basket_task(self):
        get_waste_basket(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)

    @task(4)  # 50% chance for the taskset to be interrupted
    @tag("baskets")
    def stop_baskets_taskset(self):
        self.interrupt()
