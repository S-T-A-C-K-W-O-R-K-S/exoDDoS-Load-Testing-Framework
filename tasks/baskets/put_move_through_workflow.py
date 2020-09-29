import json, random

from datetime import datetime

from environment.exoddos import exoddos
from environment.utility import utility

from ..records.get_workflow_steps import get_workflow_steps


def put_move_through_workflow(self, workzone_items):

    random_document = random.choice(workzone_items)
    document_id = random_document["document-id"]
    document_key = random_document["document-key"]

    workflow_steps = get_workflow_steps(self, document_id)

    if len(workflow_steps) > 0:
        next_workflow_step = workflow_steps[0]
        step_id = next_workflow_step["step-id"]
        target_id = next_workflow_step["destination-id"]

        payload = {
            "IDProcedureStep": step_id,
            "IDDestinationTarget": target_id,
            "Priority": random.choice([0, 1]),
            "IDDocuments": [document_id],
            "FlowComment": f"AUTOMATICALLY SENT TO TARGET ID '{target_id}' IN WORKFLOW STEP ID '{step_id}' @ {datetime.now().strftime('%H:%M:%S.%f')[:-3]}",
            "UserSpecifiedChangeDate": f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')}",
            "IDCBPApplication": None
        }

        if exoddos.debug_mode:
            print(utility.timestamp(self) + f"[DEBUG] :: Request Payload: {json.dumps(payload)}")

        with self.client.put("/Documents/MultipleSendInWorkflow",
            headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
            json=payload,
            catch_response=True) as response:

                if response.status_code == 200:
                    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Sent To Workflow Step ID '{step_id}' Record ID '{document_id}' With Key '{document_key}'")

                else:
                    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Sending Record ID '{document_id}' With Key '{document_key}' To Workflow Step ID '{step_id}' As User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    elif len(workflow_steps) == 0:
        bulletin_boards = []

        with self.client.get(f"/BulletinBoards/Available?ids={document_id}",
            name="/api/v1/BulletinBoards/Available",
            headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
            catch_response=True) as response:

                if response.status_code == 200:
                    for bulletin_board in response.json():
                        bulletin_boards.append({"bulletin-board-id": bulletin_board["IDDestination"], "bulletin-board-key": bulletin_board["BulletinBoard"]})

                    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {len(bulletin_boards)} Bulletin Board(s)")

                    if len(bulletin_boards) == 0:
                        self.interrupt()
            
                else:
                    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Bulletin Boards By User '{self.user.username}' Has Failed With Error Code {response.status_code}")

        random_bulletin_board = random.choice(bulletin_boards)
        bulletin_board_id = random_bulletin_board["bulletin-board-id"]
        bulletin_board_key = random_bulletin_board["bulletin-board-key"]

        payload = {
            "idBuletinBoard": bulletin_board_id,
            "idDocuments": [document_id],
            "BulletinBoardName": f"{bulletin_board_key}",
            "FlowComment": f"AUTOMATICALLY SENT TO BULLETIN BOARD '{bulletin_board_key}' WITH ID '{bulletin_board_id}' @ {datetime.now().strftime('%H:%M:%S.%f')[:-3]}",
            "DoSendEmail": False
        }

        with self.client.put("/BulletinBoards/MultiplePutOnBulletinBoard",
            headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
            json=payload,
            catch_response=True) as response:

                if response.status_code == 200:
                    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Sent Document ID '{document_id}' To Bulletin Board '{bulletin_board_key}' With ID '{bulletin_board_id}")

                else:
                    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Sending Document ID '{document_id}' To Bulletin Board '{bulletin_board_key}' With ID '{bulletin_board_id} As User '{self.user.username}' Has Failed With Error Code {response.status_code}")
