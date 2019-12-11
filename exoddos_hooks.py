import os, shutil

from exoddos_environment import env

from pathlib import Path


def login(self, username, password):  # on_start

    with self.client.post(f"/auth/login?client-key={env.client_key}&is-oh={env.is_oh}",
        json={"username": f"{username}", "password": f"{password}"},
        catch_response=True) as response:

            if response.status_code == 200:
                session_token = response.json()['result']['Token']
                asp_net_session_id = response.cookies['ASP.NET_SessionId']

                print(f"logged in with username '{username}' and password '{password}'")
                print(f"session token: {session_token}")
                print(f"ASP.NET session ID: {asp_net_session_id}")

                session_file = open(Path(f"sessions/{asp_net_session_id}"),"w+")
                session_file.write(session_token)
				session_file.close()

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


def create_temp_directory(self, temp_directory):  # locust setup

    if not os.path.exists(Path(temp_directory)):
        os.mkdir(Path(temp_directory))
        print(f"directory '{temp_directory}' created")
    
    else:
        print(f"directory '{temp_directory}' already exists")


def delete_temp_directory(self, temp_directory):  # locust teardown

    shutil.rmtree(temp_directory)
    print(f"directory '{temp_directory}' has been deleted")


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
