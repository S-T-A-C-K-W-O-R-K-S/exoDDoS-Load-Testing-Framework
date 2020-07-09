def get_bulletin_board_tree(self, session_id, session_cookie, username, user_collaboration_id):

    with self.client.get(f"/BulletinBoards/Tree",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}", "CBPm-IDCollaboration": f"{user_collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                print(f"Session ID {session_id}: User '{username}' Has Retrieved The Tree Of Bulletin Boards")
            
            else:
                print(f"Session ID {session_id}: Retrieving The Tree Of Bulletin Boards By User '{username}' Has Failed With Error Code {response.status_code}")
