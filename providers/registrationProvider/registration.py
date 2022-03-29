import json

from configPy import JSONConfigParser

from handlers.generators import ACCESS_TOKEN, REGISTRATION_TIME, USERID
from handlers.profile import PROFILE

# USERID(), REGISTRATION_TIME(),

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
        print("Something")


REGISTER().register_verified_profile({
        "email": "random1@gmail.com",
        "authRequestID": "c9371e4a9b914a0297743c71897084cc",
        "name": "Jane Doe",
        "hashedSecret": "6363cffb341becba0acec637a27e5193",
        "passwordHash": "2637e59347980f0bae0e2817fe650c05be6faf161f957a32feec1d6b2d460a678d0a12c603e459abb43a36ddbe47b38f34841959c426c3d835e18b1b2d2939fb",
        "requestTimestamp": "2022-03-26 17:48:11.921082+00:00",
        "status": "unverified"
    })