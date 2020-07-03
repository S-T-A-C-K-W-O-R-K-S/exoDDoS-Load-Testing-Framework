from locust import tag, task, TaskSet

from events.taskset_on_start import on_start_setup
from events.taskset_on_stop import on_stop_teardown
from environment.exoddos import exoddos

from tasks.baskets.get_workzone import get_workzone
from tasks.baskets.get_inbasket import get_inbasket
from tasks.baskets.get_outbasket import get_outbasket
from tasks.baskets.get_waste_basket import get_waste_basket

from tasks.search.get_quick_search import get_quick_search
from tasks.search.get_advanced_search import get_advanced_search


class UserBehaviour(TaskSet):

    def on_start(self):  # on_start is called when a locust spawns, before any task is scheduled for execution 
 
        if len(exoddos.user_pool) > 0: 
            self.username, self.password = exoddos.user_pool.pop() 
 
        elif len(exoddos.user_pool) == 0: 
            self.username = "NO_USERNAME" 
            self.password = "NO_PASSWORD" 
            print("The Swarm Has Exceeded The Number Of Available Credentials") 
         
        try: 
            self.session_data = on_start_setup(self, self.username, self.password) 
 
            self.session_id = self.session_data["session_id"] 
            self.session_cookie = self.session_data["session_cookie"] 
            self.user_collaboration_id = self.session_data["user_collaboration_id"] 
 
        except: 
            exoddos.user_pool.append([self.username, self.password]) 
 
    def on_stop(self):  # on_stop is called when the task set is stopping, after the tasks have executed 
        on_stop_teardown(self, self.username, self.session_id, self.session_cookie) 

    @task(1)
    @tag("baskets")
    def get_workzone_task(self):
        get_workzone(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id)

    @task(1)
    @tag("baskets")
    def get_inbasket_task(self):
        get_inbasket(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id)

    @task(1)
    @tag("baskets")
    def get_outbasket_task(self):
        get_outbasket(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id)

    @task(1)
    @tag("baskets")
    def get_waste_basket_task(self):
        get_waste_basket(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id)

    @task(1)
    @tag("search")
    def get_quick_search_task(self):
        get_quick_search(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id)

    @task(1)
    @tag("search")
    def get_advanced_search_task(self):
        get_advanced_search(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id)
