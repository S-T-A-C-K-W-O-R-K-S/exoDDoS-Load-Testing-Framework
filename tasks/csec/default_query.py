from environment.exoddos import exoddos
from environment.utility import utility


def default_query(self):

    query_params = utility.set_query_params(self, userid = self.user.user_id, sessionid = self.user.session_id,
        p01 = "F3", p02 = "*", p03 = "", p04 = "", p05 = "", p06 = "", p07 = 2, p08 = 1, p09 = 0, p10 = 20, p11 = "")

    request_url = "/query/idqm.CSECTool20.lx.dw"
    request_name = "CSEC > Default Query"

    with self.client.post(request_url, name=request_name,
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.user.username}", "X-ESCB-IAM-EMAIL": f"{self.user.email}",
            "X-ESCB-IAM-ROLES": f"{self.user.role}", "Cookie": f"{self.user.cookie_header}", "Content-Type": "text/plain"},
        cert=exoddos.ssl, verify=False,
        json={"userid": f"{self.user.user_id}", "sessionid": f"{self.user.session_id}", "databaseid": "dw1", "queryparams": query_params},
        catch_response=True) as response:

            utility.output_response_outcome(self, self.user.username, self.user.session_id, request_url, request_name, query_params, response)
