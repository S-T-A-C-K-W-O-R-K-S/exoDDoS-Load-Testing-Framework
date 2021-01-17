from locust.exception import StopUser

from environment.exoddos import exoddos
from environment.utility import utility


def on_start_setup(self):

    if len(exoddos.user_pool) > 0:
        
        try:
            self.username = exoddos.user_pool.pop()[0]  # credentials will be used from last to first

            session_data = authenticate(self)

            self.user_id = session_data["user_id"]
            self.session_id = session_data["session_id"]
            self.business_date = utility.get_parsed_date(self, session_data["business_date"])

        except Exception as e:
            print(e)
            raise StopUser

    elif len(exoddos.user_pool) == 0:
        print(utility.timestamp(self) + "The Swarm Has Exceeded The Number Of Available Credentials")
        raise StopUser


def authenticate(self):

    with self.client.get("/iamlogin",
        name="Authentication > IAM Login",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}", "X-ESCB-IAM-ROLES": f"{self.roles}"},
        allow_redirects=False,  # disable redirects in order for this API call to work (the cookies get lost in the redirect chain)
        catch_response=True) as response:

            if response.status_code == 303:
                response.success()

            else:
                print(utility.timestamp(self) + f"NO_SESSION: User '{self.username}' Has Failed IAM Authentication With Error Code {response.status_code}")


    with self.client.get("/iamuser",
        name="Authentication > IAM User",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}", "X-ESCB-IAM-ROLES": f"{self.roles}"},
        catch_response=True) as response:

            if exoddos.debug_mode:
                print(utility.timestamp(self) + f"[DEBUG] :: {response.text}")

                cookies = response.cookies.get_dict()

                for cookie in cookies:
                    print(utility.timestamp(self) + f"[DEBUG] :: {cookie}: {cookies[cookie]}")

            if response.status_code == 200:

                user_id = response.json()["userID"]
                session_id = response.json()["sessionID"]

                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: User '{self.username}' With ID '{user_id}' Has Logged In As '{self.roles}' With Email '{self.email}' And", end = " ")
                else:
                    print(utility.timestamp(self) + f"NO_SESSION: User '{self.username}' With ID '{user_id}' Has Logged In And", end = " ")

                print(f"Session ID '{session_id}' Has Been Created")

            else:
                session_id = "NO_SESSION"
                print(utility.timestamp(self) + f"Retrieving The Details Of User '{self.username}' Has Failed With Error Code {response.status_code}")


    query_string = utility.set_query_string(self, userid = user_id, sessionid = session_id)


    with self.client.get(f"/query/ESTER_OPEN_BUSDAY?params={query_string}",
        name="Query > Get Business Date",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}", "X-ESCB-IAM-ROLES": f"{self.roles}"},
        catch_response=True) as response:

        if exoddos.debug_mode:
            print(utility.timestamp(self) + f"[DEBUG] :: {query_string}")
            print(utility.timestamp(self) + f"[DEBUG] :: {response.text}")

        if response.status_code == 200:

            business_date = response.json()["JsonResultData"]["ResultSet"]["Rows"][0]["CURRENTBUSINESSDATE"]
            print(utility.timestamp(self) + f"Session ID {self.session_id}: User '{self.username}' Has Retrieved The Current Business Date Of '{business_date}'")

        else:
            business_date = "NO_BUSINESS_DATE"
            print(utility.timestamp(self) + f"Session ID {self.session_id}: Retrieving The Current Business Date For User '{self.username}' Has Failed With Error Code {response.status_code}")

    return {"user_id": f"{user_id}", "session_id": f"{session_id}", "business_date": f"{business_date}"}
