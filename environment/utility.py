import json, logging
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


    def set_query_string(self, userid, sessionid, **kwargs):

        query_params = [{"name": "userid", "value": f"{userid}"}, {"name": "sessionid", "value": f"{sessionid}"}]

        for key, value in kwargs.items():
            iteration = list(kwargs.keys()).index(key) + 1

            query_params.append({"name": f"{iteration}", "value": value})

        query_string = {"userid": f"{userid}", "sessionid": f"{sessionid}", "databaseid": "db1", "queryparams": query_params}

        return json.dumps(query_string)


    def get_parsed_date(self, date, input_format = "%d/%m/%Y", output_format = "%Y%m%d"):

        parsed_date = "NO_PARSED_DATE"

        try:
            parsed_date = datetime.strptime(date, input_format).strftime(output_format)

        except Exception as exception:
            print(utility.timestamp(self) + f"Could Not Parse Date '{date}' Using Format '{format}' Due To Error: {exception}")

        return parsed_date
