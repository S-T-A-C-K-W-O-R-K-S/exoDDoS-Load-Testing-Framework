from locust import task, TaskSet

from tasks.get_collection import get_collection
from tasks.get_dqm import get_dqm
from tasks.get_l3checks import get_l3checks
from tasks.get_market_indicators import get_market_indicators
from tasks.get_transactions import get_transactions


class ESTR(TaskSet):

    @task(3)
    def get_collection_task(self):
        get_collection(self)

    @task(3)
    def get_dqm_task(self):
        get_dqm(self)

    @task(3)
    def get_l3checks_task(self):
        get_l3checks(self)

    @task(3)
    def get_market_indicators_task(self):
        get_market_indicators(self)

    @task(3)
    def get_transactions_task(self):
        get_transactions(self)
    
    @task(5)  # 25% chance for the taskset to be interrupted
    def stop_taskset(self):
        self.interrupt()
