def on_stop_teardown(self, username, session_id, session_cookie):

    with self.client.get(f"/Auth/Logout",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}"},
        catch_response=True) as response:

            if response.status_code == 200:
                print(f"Session ID {session_id}: User '{username}' Has Logged Out And Session ID '{session_id}' Has Been Terminated")

            else:
                print(f"Session ID {session_id}: Logging Out As '{username}' In Session ID '{session_id}' Has Failed With Error Code {response.status_code}")
