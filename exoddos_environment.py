class env:

    host = "https://api.meddbase.com/patientportalapi"
    client_key = "api-brl"
    is_oh = "true"

    def __init__(self, host, client_key, is_oh):
        self.host = host
        self.client_key = client_key
        self.is_oh = is_oh
