import random

from environment.utility import utility


def put_move_to_workzone(self, inbasket_items):
    random_document = random.choice(inbasket_items)
    document_id = random_document["document-id"]
    document_key = random_document["document-key"]

    payload = {"Ids": [document_id], "UserSpecifiedChangeDate": None}

    with self.client.put("/Documents/MultipleReceiveToWorkZone/NewVersion",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        json=payload,
        catch_response=True) as response:

            if response.status_code == 200:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Received Document ID '{document_id}' With Key '{document_key}' To Their Workzone")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Receiving Document ID '{document_id}' With Key '{document_key}' To The Workzone As User '{self.user.username}' Has Failed With Error Code {response.status_code}")
