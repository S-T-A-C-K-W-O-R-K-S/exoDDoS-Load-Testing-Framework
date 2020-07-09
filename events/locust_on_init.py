import gevent, time

from locust import events, runners
from locust.runners import STATE_CLEANUP, STATE_STOPPING, STATE_STOPPED, WorkerRunner


def checker(environment):
    while not environment.runner.state in [STATE_CLEANUP, STATE_STOPPING, STATE_STOPPED]:
        time.sleep(1)
        if environment.runner.stats.total.fail_ratio >= 0.05:  # 5%
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"Test Run Will Terminate Prematurely Due To A Failure Rate Of {environment.runner.stats.total.fail_ratio}")
            print()

            environment.runner.quit()
            return

            # TODO: Initiate Shutdown, Terminate Active Sessions & Remove SYS Import, RUNNER.QUIT()
            # LOCUST.MAIN.SHUTDOWN()

#    if environment.runner.state == STATE_STOPPED:
#        if exoddos.shutdown_on_stop:
#           TODO: Initiate Shutdown


@events.init.add_listener
def on_init(environment, **_kwargs):
    if not isinstance(environment.runner, WorkerRunner):  # evaluates to TRUE if the runner is either LocalRunner or MasterRunner
        gevent.spawn(checker, environment)
