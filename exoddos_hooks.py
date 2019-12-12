from exoddos_environment import env


def login(self, username, password):  # on_start

    with self.client.post(f"/auth/login?client-key={env.client_key}&is-oh={env.is_oh}",
        json={"username": f"{username}", "password": f"{password}"},
        catch_response=True) as response:

            if response.status_code == 200:
                session_token = response.json()['result']['Token']
                asp_net_session_id = response.cookies['ASP.NET_SessionId']

                print(f"logged in with username '{username}' and password '{password}'")
                print(f"Session Token: {session_token}")
                print(f"ASP.NET Session ID: {asp_net_session_id}")

                return session_token

            else:
                print(f"logging in has failed with error code: {response.status_code}")


def logout(self, username, session_token):  # on_stop

    with self.client.post(f"/auth/logout?client-key={env.client_key}&is-oh={env.is_oh}&token={session_token}",
        catch_response=True) as response:

            if response.status_code == 200:
                print(f"{username} has logged out")
                print(f"session '{session_token}' has been terminated")

            else:
                print(f"logging out has failed with error code: {response.status_code}")


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
