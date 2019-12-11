import csv

from locust import HttpLocust, TaskSet
from locust import between

from task_sequences import FirstTaskSequence, SecondTaskSequence
from test_hooks import login, logout


red_pill = None


class UserBehavior(TaskSet):

    tasks = {FirstTaskSequence: 50, SecondTaskSequence: 50}  # both task sets have a 50% chance to be selected for execution
    
    def __init__(self, session_token):
        self.session_token = None

    def on_start(self):  # on_start is called when a locust hatches, before any task is scheduled for execution

        if len(red_pill) > 0:
            self.username, self.password = red_pill.pop()

        elif len(red_pill) == 0:
            self.password = "NO_PASSWORD"
            self.username = "NO_USERNAME"
            print("the swarm has exceeded the number of available credentials")
            
        self.session_token = login(self, self.username, self.password)

    def on_stop(self):  # on_stop is called when the task set is stopping, after the tasks have executed
        logout(self, self.username, self.session_token)


class WebsiteUser(HttpLocust):

    task_set = UserBehavior
    wait_time = between(1.0, 2.5)

    host = "https://api.meddbase.com/patientportalapi"
    sock = None

    def __init__(self):
        super(WebsiteUser, self).__init__()
        global red_pill
        if red_pill is None:
            with open('user_credentials.csv') as stream:
                reader = csv.reader(stream)
                red_pill = list(reader)
