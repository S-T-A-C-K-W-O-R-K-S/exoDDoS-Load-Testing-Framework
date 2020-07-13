from datetime import datetime


class utility:

    def timestamp(self, with_date = False, with_trailing_whitespace = True):
        if with_date:
            timestamp = "[" + datetime.now().strftime("%m-%d-%Y @ %H:%M:%S.%f")[:-3] + "]"

        else:
            timestamp = "[" + datetime.now().strftime("%H:%M:%S.%f")[:-3] + "]"

        if with_trailing_whitespace:
            timestamp += " "

        return timestamp
