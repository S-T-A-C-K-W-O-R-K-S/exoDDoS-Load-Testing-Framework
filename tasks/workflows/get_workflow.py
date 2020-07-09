import random


def get_workflow(self, session_id, session_cookie, username, user_collaboration_id):

    with self.client.get(f"/Workflows",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            workflows = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for workflow in response.json()["Items"]:
                    workflows.append(workflow["ID"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Workflows")
            
            else:
                print(f"Session ID {session_id}: Retrieving Workflows By User '{username}' Has Failed With Error Code {response.status_code}")

    if (len(workflows) > 0):
        random_workflow = random.choice(workflows)
        print(f"Session ID {session_id}: User '{username}' Has Randomly Selected Workflow ID '{random_workflow}'")

    else:
        self.interrupt()

    with self.client.get(f"/Workflows/{random_workflow}/DocumentClasses",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            document_classes = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for document_class_id in response.json()["Items"]:
                    document_classes.append(document_class_id["IDDocumentClass"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Document Classes For Workflow ID '{random_workflow}'")
            
            else:
                print(f"Session ID {session_id}: Retrieving Document Classes For Workflow ID '{random_workflow}' By User '{username}' Has Failed With Error Code {response.status_code}")

    if (len(document_classes) > 0):
        random_document_class = random.choice(document_classes)
        print(f"Session ID {session_id}: User '{username}' Has Randomly Selected Document Class ID '{random_document_class}' For Workflow ID '{random_workflow}'")

    else:
        self.interrupt()

    with self.client.get(f"/Workflows/{random_workflow}/DocumentCount/{random_document_class}",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json())

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Steps For Workflow ID '{random_workflow}'")
            
            else:
                print(f"Session ID {session_id}: Retrieving Steps For Workflow ID '{random_workflow}' By User '{username}' Has Failed With Error Code {response.status_code}")
