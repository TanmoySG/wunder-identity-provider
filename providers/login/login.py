import hashlib
import json
import re

from configPy import JSONConfigParser

from providers.login.handlers.jwt import JWT
from providers.login.handlers.payload import PAYLOAD
from providers.login.standards.return_codes import RETURN_CODES

# Import Configurations
configObject = JSONConfigParser(configFilePath="configs/datafiles.config.json")
configurations = configObject.getConfigurations()

# JWT Configs
jwtconfigObject = JSONConfigParser(configFilePath="configs/jwt.config.json")
jwtConfigurations = jwtconfigObject.getConfigurations()


def check_mailID_validity(mailID) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, mailID):
        return True
    else:
        return False


# Hash Password with SHA-512 
def hash_password(password) -> str:
    return hashlib.sha512(
        password.encode("utf-8")
    ).hexdigest()


class LOGIN:

    def __init__(self) -> None:
        self.profile_store_file = configurations["user-profile-store"]
        pass

    def verify(self, mailID, password):
        if not check_mailID_validity(mailID=mailID):
            return RETURN_CODES.LPR01, {}

        with open(self.profile_store_file) as profileStorageObject:
            profiles_store = json.load(profileStorageObject)

            if mailID in profiles_store.keys():
                profile = profiles_store[mailID]

                if profile["password"] == hash_password(password=password):
                    payload = PAYLOAD().get(profile=profile)
                    token = JWT(
                        algorithm=jwtConfigurations["jwt-algorithm"]
                    ).get(
                        payload=payload,
                        secret=jwtConfigurations["jwt-secret"]
                    )

                    verified_response = {}
                    # verified_response["response"] = RETURN_CODES.LPR04["response"]
                    # verified_response["message"] = RETURN_CODES.LPR04["details"]
                    verified_response["username"] = profile["name"]
                    verified_response["token"] = token
                    
                    return RETURN_CODES.LPR04 , verified_response
                else:
                    return RETURN_CODES.LPR03, {}
            else:
                return RETURN_CODES.LPR02, {}