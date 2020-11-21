import graypy, logging
from datetime import datetime

from environment.exoddos import exoddos


class utility:

    def timestamp(self, with_date = False, with_trailing_whitespace = True):
        if with_date:
            timestamp = "[" + datetime.now().strftime("%m-%d-%Y @ %H:%M:%S.%f")[:-3] + "]"

        else:
            timestamp = "[" + datetime.now().strftime("%H:%M:%S.%f")[:-3] + "]"

        if with_trailing_whitespace:
            timestamp += " "

        return timestamp


class graylog:

    logger = logging.getLogger("exoDDoS")
    logger.setLevel(exoddos.graylog_log_level)

    handler = graypy.GELFUDPHandler(exoddos.graylog_ip, exoddos.graylog_port)
    
    # GELFUDPHandler    -   UDP log forwarding
    # GELFTCPHandler    -   TCP log forwarding
    # GELFTLSHandler    -   TCP log forwarding with TLS support
    # GELFHTTPHandler   -   HTTP log forwarding
    # GELFRabbitHandler -   RabbitMQ log forwarding

    logger.addHandler(handler)
