import os

class env:

    debug_mode = False
    
    credentials = "environment" + os.path.sep + "user_credentials.csv"

    host = "CBPM"

    user_pool = []

    if os.environ.get("debug-user") is not None and os.environ.get("debug-pass") is not None:
        debug_user = [os.environ.get("debug-user"), os.environ.get("debug-pass")]
        user_pool.append(debug_user)

    def __init__(self, credentials, host, user_pool):
        self.credentials = credentials
        self.host = host
        self.user_pool = user_pool
