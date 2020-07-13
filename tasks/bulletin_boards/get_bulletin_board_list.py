import random

from environment.utility import utility


def get_bulletin_board_list(self):

    with self.client.get(f"/BulletinBoards/List",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            bulletin_boards = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["BulletinBoardList"])

                for bulletin_board in response.json()["BulletinBoardList"]:
                    bulletin_boards.append(bulletin_board["ID"])

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Bulletin Boards In List Mode")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Bulletin Boards In List Mode By User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    if len(bulletin_boards) > 0:
        random_bulletin_board = random.choice(bulletin_boards)
        print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Randomly Selected Bulletin Board ID '{random_bulletin_board}' In List Mode")

    else:
        self.interrupt()

    with self.client.get(f"/BulletinBoards/{random_bulletin_board}/Documents",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Documents For Bulletin Board ID '{random_bulletin_board}'")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Documents For Bulletin Board ID '{random_bulletin_board}' By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
