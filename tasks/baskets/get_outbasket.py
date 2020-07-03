def get_outbasket(self, session_id, session_cookie, username, user_collaboration_id):
    with self.client.get(f"/Baskets/outBasket",
        headers={"session-id": f"{session_id}", "Cookie": f".AspNet.ApplicationCookie={session_cookie}",
            "CBPm-IDCollaboration": f"{user_collaboration_id}", "Accept": f"application/json"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                print(f"Session ID {session_id}: User '{username}' Has Retrieved {retrieved_count} Out-Basket Items")
            
            else:
                print(f"Session ID {session_id}: Retrieving Out-Basket Items Has Failed With Error Code {response.status_code}")
