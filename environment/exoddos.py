import os

class exoddos:

    debug_mode = False
    shutdown_on_stop = True

    env = None
    host = "CBPm"
    credentials = "environment" + os.path.sep + "user_credentials.csv"
    user_pool = []

    if os.environ.get("debug-user") is not None and os.environ.get("debug-pass") is not None:
        debug_user = [os.environ.get("debug-user"), os.environ.get("debug-pass")]
        user_pool.append(debug_user)

    def __init__(self, env, host, credentials, user_pool):
        self.env = env
        self.credentials = credentials
        self.host = host
        self.user_pool = user_pool
