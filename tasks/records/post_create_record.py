import json, random

from datetime import datetime

from environment.exoddos import exoddos
from environment.utility import utility


def post_create_record(self, document_classes):

    random_document_class = random.choice(document_classes)
    print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Randomly Selected Document Class '{random_document_class}' For Document Creation")

    with self.client.get(f"/Documents/NewDocument/{random_document_class}",
        name=f"/api/v1/Documents/NewDocument/{random_document_class}",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        catch_response=True) as response:

            if response.status_code == 200:
                editable_attributes = []
                payload = {}

                for attribute in response.json()["Metadata"]["AttributesLayoutWithValues"]:
                    if attribute["Layout"]["isEditable"] == True:
                        editable_attributes.append(attribute)

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Retrieved {len(editable_attributes)} Editable Attributes For Document Class ID '{random_document_class}'")

                if len(editable_attributes) > 0:
                    payload = generate_payload_for_record_creation(self, random_document_class, editable_attributes)

                else:
                    self.interrupt()

            else:
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Selecting Document Class ID '{random_document_class}' For Record Creation As User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    record_id = None

    with self.client.post("/Documents",
        headers={"session-id": f"{self.user.session_id}", "Cookie": f".AspNet.ApplicationCookie={self.user.session_cookie}", "CBPm-IDCollaboration": f"{self.user.collaboration_id}"},
        json=payload,
        catch_response=True) as response:

            if response.status_code == 201:  # 201 Created
                record_id = response.json()["IDDocument"]
                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: User '{self.user.username}' Has Created Record ID '{record_id}' Of Document Class ID '{random_document_class}'")

            else:
                if exoddos.debug_mode:
                    print(utility.timestamp(self) + f"[DEBUG] :: Response Text: {response.text}")

                print(utility.timestamp(self) + f"Session ID {self.user.session_id}: Creating Record Of Document Class ID '{random_document_class}' As User '{self.user.username}' Has Failed With Error Code {response.status_code}")

    return record_id


# # # # # # # # # # THIS IS WHERE THE MAGIC HAPPENS # # # # # # # # # #


def generate_payload_for_record_creation(self, document_class, editable_attributes):

    payload = {
        "Attributes": [],
        "CopyPackageMembers": False,
        "DocumentCopyQuantity": 1,
        "IDDocument": 0,
        "IDDocumentClass": document_class
    }

    for attribute in editable_attributes:
        if attribute["Layout"]["AttributeName"] == "Document Key":
            reusable_timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            payload.update({"DocumentKey": reusable_timestamp})
            payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": reusable_timestamp})

        else:
            if attribute["Layout"]["IDAttributeDisplayType"] == "Text Field":
                if attribute["Layout"]["Len"] <= 8 or attribute["Layout"]["IDAttributeType"] == "N":
                    payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": datetime.now().strftime("%H%M%S")})

                elif attribute["Layout"]["IDAttributeType"] == "C":
                    payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": datetime.now().strftime("%H:%M:%S.%f")[:-3]})

            if attribute["Layout"]["IDAttributeDisplayType"] == "DateOnly Control":
                payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": datetime.now().strftime("%d-%b-%Y 00:00:00")})

            if attribute["Layout"]["IDAttributeDisplayType"] == "DateTime Control":
                payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": datetime.now().strftime("%d-%b-%Y %H:%M:%S")})

            if attribute["Layout"]["IDAttributeDisplayType"] == "Dropdown":
                options = []

                for option in attribute["Layout"]["Domain"]:
                    options.append(option["Value"])

                payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": random.choice(options)})

            if attribute["Layout"]["IDAttributeDisplayType"] == "Checkbox":
                payload["Attributes"].append({"IDAttribute": attribute["Layout"]["IDAttribute"], "Value": random.choice([True, False])})

    if exoddos.debug_mode:
        print(utility.timestamp(self) + f"[DEBUG] :: Request Payload: {json.dumps(payload)}")

    return payload
