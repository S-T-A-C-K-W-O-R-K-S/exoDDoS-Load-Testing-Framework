import json


session_token = None

client_key = "api-brl"
is_oh = "true"


def login(self, username, password): # on_start
    response = self.client.post(f"/auth/login?client-key={client_key}&is-oh={is_oh}", json = {"username":f"{username}","password":f"{password}"})

    if response.json()['status'] == "ok":
        session_token = response.json()['result']['Token']
        print(f"logged in with username '{username}' and password '{password}'")
        print(f"session token: {session_token}")

    else:
        print(f"login status: {response.json()['status']}")


def logout(self, username): # on_stop
    response = self.client.post(f"/auth/logout?client-key={client_key}&is-oh={is_oh}&token={session_token}")
    
    if response.json()['status'] == "ok":
        print(f"{username} has logged out")
        print(f"session '{session_token}' has been terminated")
        
    else:
        print(f"logout status: {response.json()['status']}")


# # # # # # # # # # # # # # # # #
#                               #
#   ORDER OF EVENTS             #
#                               #
#       1. Locust SETUP         #
#       2. TaskSet SETUP        #
#       3. TaskSet ON_START     #
#       4. TaskSet TASKS...     #
#       5. TaskSet ON_STOP      #
#       6. TaskSet TEARDOWN     #
#       7. Locust TEARDOWN      #
#                               #
# # # # # # # # # # # # # # # # #
