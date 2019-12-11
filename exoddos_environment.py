class env:

    host = "https://api.meddbase.com/patientportalapi"
    client_key = "api-brl"
    is_oh = "true"
    temp_directory = "sessions"

    def __init__(self, host, client_key, is_oh, temp_directory):
        self.host = host
        self.client_key = client_key
        self.is_oh = is_oh
        self.temp_directory = temp_directory
