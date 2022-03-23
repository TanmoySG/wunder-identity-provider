import datetime
import hashlib
import json

from configPy import JSONConfigParser
from logsmith import log

from handlers.authProfileHandler import AUTH_PROFILE
from handlers.generators import HASH_SECRET, OTP, TIMESTAMP, UUID

# Import Configurations
configObject = JSONConfigParser(configFilePath=".configs/datafiles.config.json")
configurations = configObject.getConfigurations()

# Initiate Logging
log = log()
log.configure(console_only=True, ENV="Dev")


# JSON Writer Function
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# Hash Password with SHA-512 
def hash_password(password) -> str:
    return hashlib.sha512(
        password.encode("utf-8")
    ).hexdigest()


# Auth Request Class
class AUTH_REQUEST:

    def __init__(self) -> None:
        pass

    def register(self, mailID, name, password):
        self.request_id = UUID().generate()
        self._OTP = OTP().generate(length=6)
        self._REQUEST_TIME = datetime.datetime.now(tz=datetime.timezone.utc)

        with open(configurations["authlib_store"]) as authlibObject:
            authlib = json.load(authlibObject)
            if mailID not in authlib.keys():
                authlib[mailID] = AUTH_PROFILE().create_profile(
                    mail=mailID,
                    request_id=self.request_id,
                    name=name,
                    requestTimestamp=str(self._REQUEST_TIME),
                    secret=hashlib.md5(self._OTP.encode("UTF-8")).hexdigest(),
                    password=password
                )
                write_json(authlib, configurations["authlib_store"])
                log.INFO("Registered")
                return self._OTP
            else:
                log.WARN("Mail Exists")
                return self._OTP

    def verify(self, verification_mail, verification_OTP):
        with open(configurations["authlib_store"]) as authlibObject:
            authlib=json.load(authlibObject)
            verification_profile = authlib[verification_mail]

            # Generate Secret for Current Timestamp
            current_timestamp = TIMESTAMP().generate(timeframe=1)
            hashed_verification_secret = HASH_SECRET().generate(OTP=verification_OTP, TIMESTAMPS=current_timestamp[0])

            # Dynamic Secret list creation for Request Timestamp till verifiable time frame (90s here)
            verifiable_timeframe = TIMESTAMP().generate(timeframe=configurations["otp_verification_window"], initTime=verification_profile["requestTimestamp"])
            verifiable_secrets = HASH_SECRET().generate(OTP=verification_OTP, TIMESTAMPS=verifiable_timeframe)

            if hashed_verification_secret in verifiable_secrets:
                log.SUCCESS("Verified")
            else:
                log.FAILURE("Failed")
