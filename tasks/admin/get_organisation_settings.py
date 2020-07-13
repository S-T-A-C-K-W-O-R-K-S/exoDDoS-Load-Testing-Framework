from environment.utility import utility


def get_organisation_settings(self, top):

    with self.client.get(f"/Admin/Organisations?$top={top}",
        name=f"/Admin/Organisations",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                total_count = response.json()["Count"]
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved The Settings For {retrieved_count} Organisations Out Of A Total Of {total_count}")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving The Settings For Organisations By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
