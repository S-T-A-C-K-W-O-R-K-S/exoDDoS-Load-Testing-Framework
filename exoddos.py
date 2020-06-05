from imports.all_imports import *


class UserBehavior(TaskSet):

    def on_start(self):  # on_start is called when a locust spawns, before any task is scheduled for execution

        if len(user_pool) > 0:
            self.username, self.password = user_pool.pop()

        elif len(user_pool) == 0:
            self.username = "NO_USERNAME"
            self.password = "NO_PASSWORD"
            print("The Swarm Has Exceeded The Number Of Available Credentials")

        self.session_data = on_start_setup(self, self.username, self.password)

        self.session_id = self.session_data["session_id"]
        self.session_cookie = self.session_data["session_cookie"]
        self.user_collaboration_id = self.session_data["user_collaboration_id"]

    def on_stop(self):  # on_stop is called when the task set is stopping, after the tasks have executed
        on_stop_teardown(self, self.username, self.session_id, self.session_cookie)

    @task(50)  # 50% chance for this task to be randomly selected for execution
    def get_inbasket_task(self):
        get_inbasket(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id,
            orderby=f"ChangeDate%20desc", top=50, skip=2, inlinecount="allpages")

    @task(50)  # 50% chance for this task to be randomly selected for execution
    def get_workzone_task(self):
        get_workzone(self, self.session_id, self.session_cookie, self.username, self.user_collaboration_id,
            orderby=f"ChangeDate%20desc", top=50, skip=2, inlinecount="allpages")


user_pool = None


class WebsiteUser(HttpLocust):

    task_set = UserBehavior
    wait_time = between(1.0, 2.5)

    host = env.host

    def __init__(self):
        super(WebsiteUser, self).__init__()
        global user_pool
        if user_pool is None:
            with open(Path("environment" + os.path.sep + "user_credentials.csv")) as stream:
                reader = csv.reader(stream)
                user_pool = list(reader)
