from environment.utility import utility


def get_waste_basket(self):
    with self.client.get("/Baskets/WasteBasket",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                retrieved_count = len(response.json()["Items"])
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {retrieved_count} Waste Basket Items")
            
            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Retrieving Waste Basket Items By User '{self.user.username}' Has Failed With Error Code {response.status_code}")
