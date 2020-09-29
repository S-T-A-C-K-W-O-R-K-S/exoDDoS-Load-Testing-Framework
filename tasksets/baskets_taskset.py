from locust import tag, task, SequentialTaskSet, TaskSet

from tasks.baskets.get_workzone import get_workzone
from tasks.baskets.put_move_through_workflow import put_move_through_workflow
from tasks.baskets.get_inbasket import get_inbasket
from tasks.baskets.put_move_to_workzone import put_move_to_workzone
from tasks.baskets.get_outbasket import get_outbasket
from tasks.baskets.get_waste_basket import get_waste_basket


class Baskets(TaskSet):

    @task(2)
    @tag("baskets")
    class Workzone(SequentialTaskSet):

        @task
        @tag("workzone")
        def get_workzone_task(self):
            self.workzone_items = get_workzone(self)

        @task
        @tag("workzone")
        def put_move_through_workflow_task(self):
            if len(self.workzone_items) > 0:
                put_move_through_workflow(self, self.workzone_items)
            else:
                self.interrupt()

        @task
        @tag("workzone")
        def stop_workzone_taskset(self):
            self.interrupt()

    @task(2)
    @tag("baskets")
    class InBasket(SequentialTaskSet):
        
        @task
        @tag("inbasket")
        def get_inbasket_task(self):
            self.inbasket_items = get_inbasket(self)

        @task
        @tag("inbasket")
        def put_move_to_workzone_task(self):
            if len(self.inbasket_items) > 0:
                put_move_to_workzone(self, self.inbasket_items)
            else:
                self.interrupt()

        @task
        @tag("inbasket")
        def stop_inbasket_taskset(self):
            self.interrupt()

    @task(1)
    @tag("baskets")
    def get_outbasket_task(self):
        get_outbasket(self)

    @task(1)
    @tag("baskets")
    def get_waste_basket_task(self):
        get_waste_basket(self)

    @task(4)  # 40% chance for the taskset to be interrupted
    @tag("baskets")
    def stop_baskets_taskset(self):
        self.interrupt()
