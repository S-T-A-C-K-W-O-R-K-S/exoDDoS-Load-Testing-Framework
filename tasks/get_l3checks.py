from environment.utility import utility


def get_l3checks(self):

    query_string = utility.set_query_string(self, userid = self.user.user_id, sessionid = self.user.session_id, businessdate = self.user.business_date,
        p02 = -1, p03 = 0, p04 = 0, p05 = 0)  # additional L3 Checks query parameters

    with self.client.get(f"/query/EBOR_L3CHECKS?params={query_string}",
        name="Query > Get L3 Checks Items",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.user.username}", "X-ESCB-IAM-EMAIL": f"{self.user.email}", "X-ESCB-IAM-ROLES": f"{self.user.roles}"},
        catch_response=True) as response:

        if response.status_code == 200:

            try:
                results = response.json()["JsonResultData"]["ResultSet"]["Rows"]
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {len(results)} L3 Checks Item(s)")

            except:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved No L3 Checks Items")

        else:
            print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving L3 Checks Items As User '{self.user.username}' Has Failed With Error Code {response.status_code}")
