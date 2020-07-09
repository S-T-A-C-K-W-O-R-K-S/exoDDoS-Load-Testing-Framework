import os

class exoddos:

    debug_mode = False              # when enabled, more verbose console output will be generated
    recycle_failed_logins = False   # when enabled, credentials for users that fail to log in will go back in the user pool
    shutdown_on_stop = True         # when enabled, the framework will shut down automatically at the end of the test run

    host = "CBPm"
    credentials = "environment" + os.path.sep + "user_credentials.csv"
    user_pool = []

    if os.environ.get("debug-user") is not None and os.environ.get("debug-pass") is not None:
        debug_user = [os.environ.get("debug-user"), os.environ.get("debug-pass")]
        user_pool.append(debug_user)

    def __init__(self, host, credentials, user_pool):
        self.credentials = credentials
        self.host = host
        self.user_pool = user_pool
