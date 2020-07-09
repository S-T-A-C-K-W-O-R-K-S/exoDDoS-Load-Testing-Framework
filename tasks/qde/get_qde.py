import random


def get_qde(self, session_id, session_cookie, username, user_collaboration_id):

    with self.client.get(f"/QDE",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            qde_types = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for qde_type_id in response.json()["Items"]:
                    qde_types.append(qde_type_id["IDParameter"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} QDE Types")
            
            else:
                print(f"Session ID {session_id}: Retrieving QDE Types By User '{username}' Has Failed With Error Code {response.status_code}")

    if (len(qde_types) > 0):
        random_qde_type = random.choice(qde_types)
        print(f"Session ID {session_id}: User '{username}' Has Randomly Selected QDE Type ID '{random_qde_type}'")

    else:
        self.interrupt()

    # TODO: Implement Support For Getting QDE Filters

    with self.client.get(f"/QDE/{random_qde_type}",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Results For QDE Type ID '{random_qde_type}'")
            
            else:
                print(f"Session ID {session_id}: Retrieving QDE Type Results By User '{username}' Has Failed With Error Code {response.status_code}")
