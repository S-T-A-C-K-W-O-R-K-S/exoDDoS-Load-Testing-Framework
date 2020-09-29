from environment.utility import utility


def get_document_class(self):

    document_classes = []

    with self.client.get("/DocumentClasses/DocumentClassByContext/NewDocument",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                for item in response.json()["Items"]:
                    if item["isPackage"] == True:
                        document_classes.append(item["IDDocumentClass"])

                retrieved_count = len(document_classes)

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Document Class(es) That They Have Permissions On")

            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Document Classes On Which User '{self.user.username}' Has Permissions Has Failed With Error Code {response.status_code}")

            return document_classes
