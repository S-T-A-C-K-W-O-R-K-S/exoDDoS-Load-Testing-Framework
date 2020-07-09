from environment.exoddos import exoddos


def on_start_setup(self, username, password):

    with self.client.post(f"/Auth/Login",
        json={"Username": f"{username}", "Password": f"{password}"},
        catch_response=True) as response:

            if response.status_code == 200:
                session_id = response.json()["SessionID"]
                session_cookie = response.cookies[".AspNet.ApplicationCookie"]

                if exoddos.debug_mode:
                    print(f"[DEBUG] :: NO_SESSION: User '{username}' Has Logged In With Password '{password}' And", end = " ")
                else:
                    print(f"________NO_SESSION: User '{username}' Has Logged In And", end = " ")

                print(f"Session ID '{session_id}' Has Been Created")

            else:
                session_id = "NO_SESSION"
                print(f"________NO_SESSION: Logging In As '{username}' Has Failed With Error Code {response.status_code}")

    with self.client.post(f"/Auth/Disclaimer",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}"},
        catch_response=True) as response:

            if response.text == '"DISCLAIMER_ACCEPTED"':
                session_cookie = response.cookies[".AspNet.ApplicationCookie"]
                print(f"Session ID {session_id}: User '{username}' Has Accepted The Disclaimer")
                
                if exoddos.debug_mode:
                    print(f"[DEBUG] :: Session ID {session_id} Cookie: {session_cookie}")

            else:
                print(f"Session ID {session_id}: Accepting The Disclaimer By User '{username}' Has Failed With Error Code {response.status_code}")

    with self.client.get(f"/Home/Configuration",
        headers={"Cookie": f".AspNet.ApplicationCookie={session_cookie}"},
        catch_response=True) as response:

            if response.status_code == 200:
                user_collaboration_id = "NO_COLLABORATION"
                user_id = response.json()["User"]["ID"]

                for preference in response.json()["User"]["MyPreferences"]:
                    if preference["ID"] == "User_IDCollaborationSelected":
                        user_collaboration_id = preference["Value"]

                print(f"Session ID {session_id}: User '{username}' With ID '{user_id}' Is In Collaboration ID '{user_collaboration_id}'")

            else:
                print(f"Session ID {session_id}: Retrieving The Application Configuration By User '{username}' Has Failed With Error Code {response.status_code}")

    return {"session_id": f"{session_id}", "session_cookie": f"{session_cookie}", "user_collaboration_id": f"{user_collaboration_id}"}
