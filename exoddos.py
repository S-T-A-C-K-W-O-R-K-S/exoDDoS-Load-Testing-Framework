from imports import *


class UserBehavior(TaskSet):

    def on_start(self):  # on_start is called when a locust hatches, before any task is scheduled for execution

        if len(red_pill) > 0:
            self.username, self.password = red_pill.pop()

        elif len(red_pill) == 0:
            self.username = "NO_USERNAME"
            self.password = "NO_PASSWORD"
            print("the swarm has exceeded the number of available credentials")

        self.session_token = login(self, self.username, self.password)

    def on_stop(self):  # on_stop is called when the task set is stopping, after the tasks have executed
        logout(self, self.username, self.session_token)

    @task(33)  # 33% chance for this task to be selected for execution
    def referrals_task(self):
        referrals(self, self.username, self.session_token, status = 0, page_size = 20, page_number = 1)

    @task(33)  # 33% chance for this task to be selected for execution
    def employees_task(self):
        employees(self, self.username, self.session_token, page_size = 10, page_number = 1)

    @task(33)  # 33% chance for this task to be selected for execution
    def absences_task(self):
        absences(self, self.username, self.session_token, page_sort_descending = "true", page_size = 10, page_number = 1)


red_pill = None


class WebsiteUser(HttpLocust):

    task_set = UserBehavior
    wait_time = between(1.0, 2.5)

    host = env.host

    def __init__(self):
        super(WebsiteUser, self).__init__()
        global red_pill
        if red_pill is None:
            with open(Path("user_credentials.csv")) as stream:
                reader = csv.reader(stream)
                red_pill = list(reader)
