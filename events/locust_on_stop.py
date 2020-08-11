from environment.utility import utility

from environment.exoddos import exoddos


def on_stop_teardown(self):

    if exoddos.debug_mode:
        print("[DEBUG] :: Cookie Header: " + self.cookie_header)

    with self.client.post("/logout",
        name="Authentication > IAM Logout",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}",
            "X-ESCB-IAM-ROLES": f"{self.role}", "Cookie": f"{self.cookie_header}", "Content-Type": "text/plain"},
        cert=exoddos.ssl, verify=False,
        json={"user": f"{self.user_id}", "session": f"{self.session_id}", "databaseid": "db1"},
        catch_response=True) as response:

            if response.status_code == 200:
                print(utility.timestamp(self) + f"Session ID {self.session_id}: User '{self.username}' Has Logged Out And Session ID '{self.session_id}' Has Been Terminated")

            else:
                print(utility.timestamp(self) + f"Session ID {self.session_id}: Logging Out As '{self.username}' In Session ID '{self.session_id}' Has Failed With Error Code {response.status_code}")
