import json

from configPy import JSONConfigParser

from providers.registrationProvider.handlers.generators import ACCESS_TOKEN, REGISTRATION_TIME, USERID
from providers.registrationProvider.handlers.profile import PROFILE
from providers.registrationProvider.standards.return_codes import RETURN_CODES


# Import Configurations
configObject = JSONConfigParser(configFilePath=".configs/datafiles.config.json")
configurations = configObject.getConfigurations()


# JSON Writer Function
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


class REGISTER:

    def __init__(self) -> None:
        self.profile_store_file = configurations["user-profile-store"]
        pass

    def register_verified_profile(self, verified_profile):
        with open(self.profile_store_file) as profileStorageObject:
            profile_store = json.load(profileStorageObject)

            if verified_profile["email"] not in profile_store.keys():
                # Acccess Token
                token = ACCESS_TOKEN(length=128, use_method="secrets").generate()

                profile_store[verified_profile["email"]] = PROFILE().new_profile(
                    mailID=verified_profile["email"],
                    userID=USERID(),
                    username=verified_profile["name"],
                    password=verified_profile["passwordHash"],
                    registration_timestamp=REGISTRATION_TIME(),
                    admin_access_token=token
                )
                write_json(profile_store, self.profile_store_file)
                return RETURN_CODES.RPR01
            else:
                return RETURN_CODES.RPR02