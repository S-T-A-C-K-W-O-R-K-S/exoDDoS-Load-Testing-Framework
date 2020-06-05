from datetime import datetime
from locust import events
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner
import gevent, time


def checker(environment):
    while not environment.runner.state in [STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP]:
        time.sleep(1)
        if environment.runner.stats.total.fail_ratio > 0.2:  # 20%
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"Test Run Will Terminate Prematurely Due To A Failure Rate Of {environment.runner.stats.total.fail_ratio}")
            print()
            environment.runner.quit()
            return

@events.init.add_listener
def on_init(environment, **_kwargs):
    if not isinstance(environment.runner, WorkerRunner):
        gevent.spawn(checker, environment)
