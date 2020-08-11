import os


class exoddos:

    debug_mode = False  # when enabled, more verbose console output will be generated

    host = "CSDB"

    ssl_certificate = "environment" + os.path.sep + "ssl" + os.path.sep + "placeholder_ssl_certificate"
    ssl_key = "environment" + os.path.sep + "ssl" + os.path.sep + "placeholder_decrypted_ssl_key"
    ssl = (ssl_certificate, ssl_key)

    query_pages = [(1,100), (101,200), (201,300), (301,400), (401,500)]

    user_pool = [
        ["DDOS-00001", "DDOS-00001@EXO.DDOS", "CSDB-ADMIN"],
        ["DDOS-00002", "DDOS-00002@EXO.DDOS", "CSDB-ADMIN"],
        ["DDOS-00003", "DDOS-00003@EXO.DDOS", "CSDB-ADMIN"]
    ]
