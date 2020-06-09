from imports.environment import env


def on_start_setup(self, username, password):

    with self.client.post(f"/auth/login",
        json={"Username": f"{username}", "Password": f"{password}"},
        catch_response=True) as response:

            if response.status_code == 200:
                session_id = response.json()["SessionID"]
                session_cookie = response.cookies[".AspNet.ApplicationCookie"]

                if env.debug_mode:
                    print(f"[DEBUG] :: User '{username}' Has Logged In With Password '{password}'")
                else:
                    print(f"User '{username}' Has Logged In")

                print(f"Session ID '{session_id}' Has Been Created")

            else:
                session_id = "NO_SESSION"
                print(f"Logging In Has Failed With Error Code {response.status_code}")

    with self.client.post(f"/auth/disclaimer",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}"},
        catch_response=True) as response:

            if response.text == '"DISCLAIMER_ACCEPTED"':
                session_cookie = response.cookies[".AspNet.ApplicationCookie"]
                print(f"Session ID {session_id}: User '{username}' Has Accepted The Disclaimer")
                
                if env.debug_mode:
                    print(f"[DEBUG] :: Session Cookie: {session_cookie}")

    with self.client.get(f"/home/configuration",
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
                print(f"Retrieving The Application Configuration Has Failed With Error Code {response.status_code}")

    return {"session_id": f"{session_id}", "session_cookie": f"{session_cookie}", "user_collaboration_id": f"{user_collaboration_id}"}
