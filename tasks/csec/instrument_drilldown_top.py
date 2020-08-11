from environment.exoddos import exoddos
from environment.utility import utility


def instrument_drilldown_top(self):

    for p03 in ["AT", "DE"]:

        for p11 in ["GI", "REDEMPTION", "STOCK"]:

            for (p09, p10) in exoddos.query_pages:

                for p01 in utility.last_days_of_the_previous_twelve_months(self):

                    query_params = utility.set_query_params(self, userid = self.user.user_id, sessionid = self.user.session_id,
                        p01 = p01, p02 = "F3", p03 = p03, p04 = "", p05 = "", p06 = "", p07 = "", p08 = "", p09 = p09, p10 = p10, p11 = p11)

                    request_url = "/aquery/idqm.CSECTool20.ISIN.dw"
                    request_name = f"CSEC > IDD BOT > {p03}, {p11}, {p09}-{p10:03}, {p01}"

                    with self.client.post(request_url, name=request_name,
                        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.user.username}", "X-ESCB-IAM-EMAIL": f"{self.user.email}",
                            "X-ESCB-IAM-ROLES": f"{self.user.role}", "Cookie": f"{self.user.cookie_header}", "Content-Type": "text/plain"},
                        cert=exoddos.ssl, verify=False,
                        json={"userid": f"{self.user.user_id}", "sessionid": f"{self.user.session_id}", "databaseid": "dw1", "queryparams": query_params},
                        catch_response=True) as response:

                            utility.output_response_outcome(self, self.user.username, self.user.session_id, request_url, request_name, query_params, response)
