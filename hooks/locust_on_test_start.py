from datetime import datetime
from locust import events

from environment.utility import utility


@events.test_start.add_listener
def on_test_start(**kwargs):
    print()
    print("Test Run Initiated: " + datetime.now().strftime("%d-%m-%Y @ %H:%M:%S"))
    utility.print_dashes(utility)
