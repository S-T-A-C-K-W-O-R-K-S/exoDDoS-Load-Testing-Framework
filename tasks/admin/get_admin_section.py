from environment.utility import utility


def get_admin_section(self):

    with self.client.get(f"/Admin/Role",
    headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
    catch_response=True) as response:

        if response.text == '"Administrator"':
            print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Is An Administrator And Has Access To Functions Which Require Elevated Privileges")
            return True

        if response.text == '"CollaborationManager"':
            print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Is A Collaboration Manager And Has Access To Administrator Functions")
            return True

        if response.status_code == 403:
            response.success()
            print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Is Not An Administrator Or A Collaboration Manager And Access To Functions Which Require Elevated Privileges Is Restricted")
            return False

# users can be either:
#     type A - administrator
#     type B - regular user
#         part of the management collaboration, making them a collaboration manager
#         not part of the management collaboration
#     type C - service user
