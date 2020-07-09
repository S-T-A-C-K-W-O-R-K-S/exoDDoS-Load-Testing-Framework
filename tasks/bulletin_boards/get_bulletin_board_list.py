import random


def get_bulletin_board_list(self, session_id, session_cookie, username, user_collaboration_id):

    with self.client.get(f"/BulletinBoards/List",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            bulletin_boards = []

            if response.status_code == 200:
                retrieved_count = len(response.json()["BulletinBoardList"])

                for bulletin_board in response.json()["BulletinBoardList"]:
                    bulletin_boards.append(bulletin_board["ID"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Bulletin Boards In List Mode")
            
            else:
                print(f"Session ID {session_id}: Retrieving Bulletin Boards In List Mode By User '{username}' Has Failed With Error Code {response.status_code}")

    if (len(bulletin_boards) > 0):
        random_bulletin_board = random.choice(bulletin_boards)
        print(f"Session ID {session_id}: User '{username}' Has Randomly Selected Bulletin Board ID '{random_bulletin_board}' In List Mode")

    else:
        self.interrupt()

    with self.client.get(f"/BulletinBoards/{random_bulletin_board}/Documents",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])

                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Documents For Bulletin Board ID '{random_bulletin_board}'")
            
            else:
                print(f"Session ID {session_id}: Retrieving Documents For Bulletin Board ID '{random_bulletin_board}' By User '{username}' Has Failed With Error Code {response.status_code}")
