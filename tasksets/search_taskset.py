from locust import tag, task, TaskSet

from environment.exoddos import exoddos

from tasks.search.get_quick_search import get_quick_search
from tasks.search.get_advanced_search import get_advanced_search


class Search(TaskSet):

    @task(1)
    @tag("search")
    def get_quick_search_task(self):
        get_quick_search(self, page_size=exoddos.results, page=1)

    @task(1)
    @tag("search")
    def get_advanced_search_task(self):
        get_advanced_search(self, page_size=exoddos.results, page=1)

    @task(2)  # 50% chance for the taskset to be interrupted
    @tag("search")
    def stop_search_taskset(self):
        self.interrupt()
