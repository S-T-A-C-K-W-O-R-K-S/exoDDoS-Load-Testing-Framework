from environment.utility import utility


def get_inbasket(self):
    with self.client.get(f"/Baskets/InBasket",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} In-Basket Items")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving In-Basket Items By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
