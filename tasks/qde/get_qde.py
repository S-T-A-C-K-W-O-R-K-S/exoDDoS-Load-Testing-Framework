import random

from environment.utility import utility


def get_qde(self):

    with self.client.get("/QDE",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            qde_types = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for qde_type_id in response.json()["Items"]:
                    qde_types.append(qde_type_id["IDParameter"])

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} QDE Types")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving QDE Types By User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    if len(qde_types) > 0:
        random_qde_type = random.choice(qde_types)
        print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Randomly Selected QDE Type ID '{random_qde_type}'")

    else:
        self.interrupt()

    # TODO: Implement Support For Getting QDE Filters

    with self.client.get(f"/QDE/{random_qde_type}",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Results For QDE Type ID '{random_qde_type}'")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving QDE Type Results By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
