import math

from datetime import date, datetime, timedelta

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


    def print_dashes(self):
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")


    def set_query_params(self, userid, sessionid, **kwargs):

        query_params = [{"name": "userid", "value": f"{userid}"}, {"name": "sessionid","value": f"{sessionid}"}]

        for key, value in kwargs.items():
            iteration = list(kwargs.keys()).index(key) + 1

            query_params.append({"name": f"{iteration}", "value": value})

        return query_params


    def output_response_outcome(self, username, session_id, request_url, request_name, query_params, response):

        if response.status_code == 200:

            try:
                retrieved_count = len(response.json()["JsonResultData"]["Records"]["Record"])

                utility.print_dashes(self)
                print(utility.timestamp(self) + f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Records")
                print(utility.timestamp(self) + f"Request Name: {request_name}")
                print(utility.timestamp(self) + f"Request URL: {exoddos.host}{request_url}")
                print(utility.timestamp(self) + f"Query Parameters: {str(query_params)}")

            except:
                utility.print_dashes(self)
                print(utility.timestamp(self) + f"Session ID {session_id}: Query Executed By User '{username}' Did Not Return Any Records")
                print(utility.timestamp(self) + f"Request Name: {request_name}")
                print(utility.timestamp(self) + f"Request URL: {exoddos.host}{request_url}")
                print(utility.timestamp(self) + f"Query Parameters: {str(query_params)}")

        else:
            utility.print_dashes(self)
            print(utility.timestamp(self) + f"Session ID {session_id}: Retrieving Records As '{username}' Has Failed With Error Code {response.status_code}")
            print(utility.timestamp(self) + f"Request Name: {request_name}")
            print(utility.timestamp(self) + f"Request URL: {exoddos.host}{request_url}")
            print(utility.timestamp(self) + f"Query Parameters: {str(query_params)}")


    def last_days_of_the_previous_twelve_months(self):

        one_year_ago = date(datetime.now().year - 1, datetime.now().month, datetime.now().day)
        today = date(datetime.now().year, datetime.now().month, datetime.now().day)

        start_month = one_year_ago.month + 1
        end_month = (today.year - one_year_ago.year) * 12 + today.month

        for month in range(start_month, end_month + 1):
            year = math.floor((month - 1) / 12) + one_year_ago.year
            month = (month - 1) % 12 + 1

            last_day_of_the_month = (datetime(year, month, 1) - timedelta(days = 1))
            yield last_day_of_the_month.strftime("%d/%m/%Y")
