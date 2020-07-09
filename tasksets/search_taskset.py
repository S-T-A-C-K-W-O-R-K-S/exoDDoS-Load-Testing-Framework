from locust import tag, task, TaskSet

from tasks.search.get_quick_search import get_quick_search
from tasks.search.get_advanced_search import get_advanced_search


class Search(TaskSet):

    @task(1)
    @tag("search")
    def get_quick_search_task(self):
        get_quick_search(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id, page_size=100, page=1)

    @task(1)
    @tag("search")
    def get_advanced_search_task(self):
        get_advanced_search(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id, page_size=100, page=1)

    @task(2)  # 50% chance for the taskset to be interrupted
    @tag("search")
    def stop_search_taskset(self):
        self.interrupt()
