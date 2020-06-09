import os

class env:

    debug_mode = False

    if os.environ.get("swarm") is None:
        credentials = "environment" + os.path.sep + "user_credentials.csv"
    elif os.environ.get("swarm") is not None:
        credentials = os.environ.get("swarm")  # can use the "swarm" environment variable to override the built-in credentials file

    host = "CBPM"

    user_pool = None

    def __init__(self, credentials, host, user_pool):
        self.credentials = credentials
        self.host = host
        self.user_pool = user_pool
