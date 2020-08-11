from locust.exception import StopUser

from environment.exoddos import exoddos
from environment.utility import utility


def on_start_setup(self):

    if len(exoddos.user_pool) > 0:
        
        try:
            self.username, self.email, self.role = exoddos.user_pool.pop()  # credentials will be used from last to first
            
            session_data = authenticate(self)

            self.user_id = session_data["user_id"]
            self.session_id = session_data["session_id"]
            self.cookie_jar = session_data["cookie_jar"]
            self.cookie_header = session_data["cookie_header"]

        except Exception as e:
            print(e)
            raise StopUser

    elif len(exoddos.user_pool) == 0:
        print("The Swarm Has Exceeded The Number Of Available Credentials")
        raise StopUser


def authenticate(self):

    with self.client.get("/iamlogin",
        name="Authentication > IAM Login",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}", "X-ESCB-IAM-ROLES": f"{self.role}"},
        cert=exoddos.ssl, verify=False, allow_redirects=False,  # disable redirects in order for this API call to work (the cookies get lost in the redirect chain)
        catch_response=True) as response:

            if response.status_code == 303:
                response.success()

                if exoddos.debug_mode:
                    cookies = response.cookies.get_dict()

                    for cookie in cookies:
                        print(f"[DEBUG] :: {cookie}: {cookies[cookie]}")

                cookie_play_session = "PLAY_SESSION=" + response.cookies["PLAY_SESSION"]
                cookie_credentials = "CREDENTIALS=" + response.cookies["CREDENTIALS"]
                cookie_session_id = "SESSION-ID=" + response.cookies["SESSION-ID"]

                cookie_jar = [cookie_play_session, cookie_credentials, cookie_session_id]
                cookie_header = f"{cookie_play_session}; {cookie_credentials}; {cookie_session_id}"

            else:
                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: Logging In As '{self.username}' With Role '{self.role}' With Email '{self.password}' Has Failed With Error Code {response.status_code}")
                else:
                    print(utility.timestamp(self) + f"NO_SESSION: Logging In As '{self.username}' Has Failed With Error Code {response.status_code}")

    with self.client.get("/iamuser",
        name="Authentication > IAM User",
        headers={"X-ESCB-IAM-CC": "EU", "X-ESCB-IAM-UID": f"{self.username}", "X-ESCB-IAM-EMAIL": f"{self.email}", "X-ESCB-IAM-ROLES": f"{self.role}"},
        cert=exoddos.ssl, verify=False,
        catch_response=True) as response:

            if response.status_code == 200:

                user_id = response.json()["userID"]
                session_id = response.json()["sessionID"]

                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: User '{self.username}' With ID '{user_id}' Has Logged In As '{self.role}' With Email '{self.email}' And", end = " ")
                else:
                    print(utility.timestamp(self) + f"NO_SESSION: User '{self.username}' With ID '{user_id}' Has Logged In And", end = " ")

                print(f"Session ID '{session_id}' Has Been Created")

            else:
                session_id = "NO_SESSION"
                
                print(utility.timestamp(self) + f"[DEBUG] :: Retrieving The Details Of User '{self.username}' Has Failed With Error Code {response.status_code}")

    return {"user_id": f"{user_id}", "session_id": f"{session_id}", "cookie_jar": cookie_jar, "cookie_header": cookie_header}
