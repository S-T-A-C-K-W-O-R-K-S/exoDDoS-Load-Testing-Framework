import logging, os


class exoddos:

    debug_mode = False  # when enabled, more verbose console output will be generated

    host = "http://ebowd83.ecbt1.tadnet.net:8080/api"

    credentials = "environment" + os.path.sep + "user_credentials.csv"

    user_pool = None
