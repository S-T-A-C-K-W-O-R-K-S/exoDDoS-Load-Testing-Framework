from locust.exception import StopUser

from environment.exoddos import exoddos
from environment.utility import utility


def on_start_setup(self):

    if len(exoddos.user_pool) > 0:
        
        try:
            self.username, self.password = exoddos.user_pool.pop()  # credentials will be used from last to first

            session_data = authenticate(self)

            self.session_id = session_data["session_id"]
            self.session_cookie = session_data["session_cookie"]
            self.collaboration_id = session_data["collaboration_id"]

        except:
            if exoddos.recycle_failed_logins:
                exoddos.user_pool.append([self.username, self.password])
                
            raise StopUser

    elif len(exoddos.user_pool) == 0:
        print("The Swarm Has Exceeded The Number Of Available Credentials")
        raise StopUser


def authenticate(self):

    with self.client.post(f"/Auth/Login",
        json={"Username": f"{self.username}", "Password": f"{self.password}"},
        catch_response=True) as response:

            if response.status_code == 200:
                session_id = response.json()["SessionID"]
                session_cookie = response.cookies[".AspNet.ApplicationCookie"]

                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: User '{self.username}' Has Logged In With Password '{self.password}' And", end = " ")
                else:
                    print(utility.timestamp(self) + f"________NO_SESSION: User '{self.username}' Has Logged In And", end = " ")

                print(f"Session ID '{session_id}' Has Been Created")

            else:
                session_id = "NO_SESSION"

                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: Logging In As '{self.username}' With Password '{self.password}' Has Failed With Error Code {response.status_code}")
                else:
                    print(utility.timestamp(self) + f"________NO_SESSION: Logging In As '{self.username}' Has Failed With Error Code {response.status_code}")

    with self.client.post(f"/Auth/Disclaimer",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}"},
        catch_response=True) as response:

            if response.text == '"DISCLAIMER_ACCEPTED"':
                session_cookie = response.cookies[".AspNet.ApplicationCookie"]
                print(utility.timestamp(self) + f"Session ID {session_id}: User '{self.username}' Has Accepted The Disclaimer")
                
                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: Session ID {session_id} Cookie: {session_cookie}")

            else:
                print(utility.timestamp(self) + f"Session ID {session_id}: Accepting The Disclaimer By User '{self.username}' Has Failed With Error Code {response.status_code}")

    with self.client.get(f"/Home/Configuration",
        headers={"Cookie": f".AspNet.ApplicationCookie={session_cookie}"},
        catch_response=True) as response:

            if response.status_code == 200:
                collaboration_id = "NO_COLLABORATION"
                user_id = response.json()["User"]["ID"]

                for preference in response.json()["User"]["MyPreferences"]:
                    if preference["ID"] == "User_IDCollaborationSelected":
                        collaboration_id = preference["Value"]

                print(utility.timestamp(self) + f"Session ID {session_id}: User '{self.username}' With ID '{user_id}' Is In Collaboration ID '{collaboration_id}'")

            else:
                print(utility.timestamp(self) + f"Session ID {session_id}: Retrieving The Application Configuration By User '{self.username}' Has Failed With Error Code {response.status_code}")

    return {"session_id": f"{session_id}", "session_cookie": f"{session_cookie}", "collaboration_id": f"{collaboration_id}"}
