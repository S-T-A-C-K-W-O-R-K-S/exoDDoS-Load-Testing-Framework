import random

from environment.utility import utility


def get_advanced_search(self, page_size, page):

    with self.client.get("/DocumentClasses",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            document_classes = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for document_class_id in response.json()["Items"]:
                    document_classes.append(document_class_id["ID"])

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Document Classes For An Advanced Search")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Document Classes By User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    if len(document_classes) > 0:
        random_document_class = random.choice(document_classes)
        print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Randomly Selected Document Class ID '{random_document_class}' For An Advanced Search")

    else:
        self.interrupt()

    with self.client.get(f"/Documents/Search?IDDocumentClass={random_document_class}&pageSize={page_size}&page={page}",
        name=f"/api/v1/Documents/Search?IDDocumentClass={random_document_class}",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                total_count = response.json()["Count"]
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Advanced Search Results Out Of A Total Of {total_count} For Document Class ID '{random_document_class}'")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Advanced Search Results By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
