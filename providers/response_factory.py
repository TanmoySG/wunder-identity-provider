# Generates Valid API Responses from provided parameters
# Move this section to separate file

class RESPONSE_FACTORY:

    def get(self, status, response, scopes, payload):
        self.response = {
            "status" : status,
            "response" : response,
            "scopes": scopes,
            "payload" : payload
        }

        return self.response