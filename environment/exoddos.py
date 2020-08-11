import os


class exoddos:

    debug_mode = False  # when enabled, more verbose console output will be generated

    host = "https://csdwd260.ecbt1.tadnet.net/csdb-idqm/api"

    ssl_certificate = "environment" + os.path.sep + "ssl" + os.path.sep + "csdb-fin.crt"
    ssl_key = "environment" + os.path.sep + "ssl" + os.path.sep + "csdb-fin-decrypted.key"
    ssl = (ssl_certificate, ssl_key)

    query_pages = [(1,100), (101,200), (201,300), (301,400), (401,500)]

    user_pool = [
        ["EUFINCORE", "vlad.tanasescu@fincore.com", "APPR_CSDB_BA-ADMIN"],
        ["EUGERGANA", "gergana.tabakova@fincore.com", "APPR_CSDB_BA-ADMIN"],
        ["EURADICMI", "mina.radic@fincore.com", "APPR_CSDB_BA-ADMIN"]
    ]
