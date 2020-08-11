from datetime import datetime
from locust import events

from environment.utility import utility


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    utility.print_dashes(utility)
    print("Test Run Terminated: " + datetime.now().strftime("%d-%m-%Y @ %H:%M:%S"))
    print()
