import os

class env:

    debug_mode = False

    credentials = "environment" + os.path.sep + "user_credentials.csv"
    host = "CBPM"
    user_pool = None

    def __init__(self, credentials, host, user_pool):
        self.credentials = credentials
        self.host = host
        self.user_pool = user_pool
