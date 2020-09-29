import json, random

from datetime import datetime

from environment.exoddos import exoddos
from environment.utility import utility


def put_send_to_workflow(self, record_id, workflow_steps):

    random_workflow_step = random.choice(workflow_steps)
    step_id = random_workflow_step["step-id"]
    target_id = random_workflow_step["destination-id"]

    payload = {
        "IDProcedureStep": step_id,
        "IDDestinationTarget": target_id,
        "Priority": random.choice([0, 1]),
        "IDDocuments": [record_id],
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
                record_key = response.json()[0]["DocumentKey"]

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Sent To Workflow Step ID '{step_id}' Record ID '{record_id}' With Key '{record_key}'")

            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Sending Record ID '{record_id}' To Workflow Step ID '{step_id}' As User '{self.user.username}' Has Failed With Error Code {response.status_code}")
