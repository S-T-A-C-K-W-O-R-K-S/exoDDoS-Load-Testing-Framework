from environment.utility import utility


def on_stop_teardown(self):

    with self.client.get("/Auth/Logout",
        headers={"session-id": f"{self.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.session_cookie}"},
        catch_response=True) as response:

            if response.status_code == 200:
                print(utility.timestamp(self) + f"Session ID {self.session_id}: User '{self.username}' Has Logged Out And Session ID '{self.session_id}' Has Been Terminated")

            else:
                print(utility.timestamp(self) + f"Session ID {self.session_id}: Logging Out As '{self.username}' In Session ID '{self.session_id}' Has Failed With Error Code {response.status_code}")
