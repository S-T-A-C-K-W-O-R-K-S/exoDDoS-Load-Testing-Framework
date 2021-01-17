from environment.utility import utility
from environment.exoddos import exoddos


def on_stop_teardown(self):

    if self.session_id == "NO_SESSION":
        print(utility.timestamp(self) + f"NO_SESSION: User '{self.username}' Without Session Has Been Preemptively Terminated")

    else:
        with self.client.get("/iamlogout",
            name="Authentication > IAM Logout",
            headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}", "X-ESCB-IAM-ROLES": f"{self.roles}"},
            catch_response=True) as response:

                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: {response.text}")

                if response.status_code == 200:
                    print(utility.timestamp(self) + f"Session ID {self.session_id}: User '{self.username}' Has Logged Out And The Session Has Been Terminated")

                else:
                    print(utility.timestamp(self) + f"Session ID {self.session_id}: Logging Out As '{self.username}' In Session ID '{self.session_id}' Has Failed With Error Code {response.status_code}")
