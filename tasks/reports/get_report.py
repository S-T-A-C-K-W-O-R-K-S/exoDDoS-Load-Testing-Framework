import random


def get_report(self, session_id, session_cookie, username, user_collaboration_id, filters):

    with self.client.get(f"/Report",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            reports = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                for report in response.json()["Items"]:
                    reports.append(report["IDReport"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Report Types")
            
            else:
                print(f"Session ID {session_id}: Retrieving Report Types By User '{username}' Has Failed With Error Code {response.status_code}")

    if (len(reports) > 0):
        random_report = random.choice(reports)
        print(f"Session ID {session_id}: User '{username}' Has Randomly Selected Report Type ID '{random_report}'")

    else:
        self.interrupt()

    with self.client.get(f"/Report/{random_report}/data?filterOperatorList={filters}",
        name=f"/Report/{random_report}/data",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Documents For Report Type ID '{random_report}'")
            
            else:
                print(f"Session ID {session_id}: Retrieving Documents For Report Type ID '{random_report}' By User '{username}' Has Failed With Error Code {response.status_code}")
