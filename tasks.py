from environment import env

def referrals(self, username, session_token, status, page_size, page_number):

    response = self.client.get(f"/referrals/referrals?status={status}&page-size={page_size}&page-number={page_number}&" +
        f"client-key={env.client_key}&token={session_token}")

    print(f"user '{username}' has retrieved {response.json()['result']['TotalCount']} referrals")


def employees(self, username, session_token, page_size, page_number):
    
    response = self.client.post(f"/patients/patients?page-size={page_size}&page-number={page_number}&" +
        f"client-key={env.client_key}&token={session_token}",
        json={"customData":["RecallDueDate","LastActivity","FitnessOutcome"]})

    print(f"user '{username}' has retrieved {response.json()['result']['TotalCount']} employees")


def absences(self, username, session_token, page_sort_descending, page_size, page_number):
    
    response = self.client.get(f"/absences/absences?page-sort-descending={page_sort_descending}&page-size={page_size}&page-number={page_number}&" +
        f"client-key={env.client_key}&token={session_token}")

    print(f"user '{username}' has retrieved {response.json()['result']['TotalCount']} absences")
