import random


def get_quick_search(self, session_id, session_cookie, username, user_collaboration_id, page_size, page):

    with self.client.get(f"/DocumentClasses",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            document_classes = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for document_class_id in response.json()["Items"]:
                    document_classes.append(document_class_id["ID"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Document Classes For A Quick Search")
            
            else:
                print(f"Session ID {session_id}: Retrieving Document Classes By User '{username}' Has Failed With Error Code {response.status_code}")

    if (len(document_classes) > 0):
        random_document_class = random.choice(document_classes)
        print(f"Session ID {session_id}: User '{username}' Has Randomly Selected Document Class ID '{random_document_class}' For A Quick Search")

    else:
        self.interrupt()

    with self.client.get(f"/Documents/QuickSearch?IDDocumentClass={random_document_class}&pageSize={page_size}&page={page}",
        name=f"/Documents/QuickSearch?IDDocumentClass={random_document_class}",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                total_count = response.json()["Count"]
                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Quick Search Results Out Of A Total Of {total_count} For Document Class ID '{random_document_class}'")
            
            else:
                print(f"Session ID {session_id}: Retrieving Quick Search Results By User '{username}' Has Failed With Error Code {response.status_code}")
