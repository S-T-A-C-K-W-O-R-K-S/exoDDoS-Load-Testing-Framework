from environment.utility import utility


def get_bulletin_board_tree(self):

    with self.client.get(f"/BulletinBoards/Tree",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved The Tree Of Bulletin Boards")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving The Tree Of Bulletin Boards By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
