import random

from environment.utility import utility


def get_report(self, filters):

    with self.client.get("/Report",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            reports = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for report in response.json()["Items"]:
                    reports.append(report["IDReport"])

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Report Types")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Report Types By User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    if len(reports) > 0:
        random_report = random.choice(reports)
        print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Randomly Selected Report Type ID '{random_report}'")

    else:
        self.interrupt()

    with self.client.get(f"/Report/{random_report}/data?filterOperatorList={filters}",
        name=f"/api/v1/Report/{random_report}/data",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Documents For Report Type ID '{random_report}'")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Documents For Report Type ID '{random_report}' By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
