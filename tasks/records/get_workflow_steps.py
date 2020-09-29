from environment.utility import utility


def get_workflow_steps(self, record_id):

    workflow_steps = []

    with self.client.get(f"/Documents/{record_id}/WorkflowSteps",
        name="/api/v1/Documents/RecordID/WorkflowSteps",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                for step in response.json()["Items"]:
                    workflow_steps.append({"step-id": step["ID"], "destination-id": step["IDDestination_Target"], "description": step["Description"]})

                retrieved_count = len(workflow_steps)

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Workflow Step(s) For Record ID '{record_id}'")

            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Workflow Steps For Record ID '{record_id}' As User '{self.user.username}' Has Failed With Error Code {response.status_code}")

            return workflow_steps
