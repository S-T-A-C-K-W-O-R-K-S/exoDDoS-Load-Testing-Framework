import os


class exoddos:

    # # # manually-managed flags
    debug_mode = False              # when enabled, more verbose console output will be generated
    recycle_failed_logins = False   # when enabled, credentials for users that fail to log in will go back in the user pool
    results = 100                   # the maximum number of results to return when performing an expensive request

    # # # self-managed flags
    high_failure_rate = False       # when true, new users will be prevented from spawning

    # # # environment properties
    host = "CBPm"
    credentials = "environment" + os.path.sep + "user_credentials.csv"
    user_pool = None

    # # # environment conditions
    if os.environ.get("debug-user") is not None and os.environ.get("debug-pass") is not None:
        debug_user = [os.environ.get("debug-user"), os.environ.get("debug-pass")]
        user_pool.append(debug_user)
