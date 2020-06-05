from datetime import datetime
from locust import events


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Test Run Terminated: " + datetime.now().strftime("%d-%m-%Y @ %H:%M:%S"))
    print()
