import datetime
import hashlib
import json
import re

from configPy import JSONConfigParser

from providers.authLib.handlers.authProfileHandler import AUTH_PROFILE
from providers.authLib.handlers.generators import HASH_SECRET, OTP, TIMESTAMP, UUID
from providers.authLib.standards.return_codes import RETURN_CODES as RC

# Import Configurations
configObject = JSONConfigParser(configFilePath=".configs/datafiles.config.json")
configurations = configObject.getConfigurations()


# JSON Writer Function
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# Hash Password with SHA-512 
def hash_password(password) -> str:
    return hashlib.sha512(
        password.encode("utf-8")
    ).hexdigest()


# Check Email Validity
def check_mailID_validity(mailID) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, mailID):
        return True
    else:
        return False


# Auth Request Class
class AUTH_REQUEST:

    def __init__(self) -> None:
        pass

    def register(self, mailID, name, password):

        if not check_mailID_validity(mailID=mailID) :
            return RC.ALR01, {}

        self.request_id = UUID().generate()
        self._OTP = OTP().generate(length=6)
        self._REQUEST_TIME = datetime.datetime.now(tz=datetime.timezone.utc)

        with open(configurations["authlib-store"]) as authlibObject:
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
                write_json(authlib, configurations["authlib-store"])
                return RC.ALR02, self._OTP
            else:
                return RC.ALR03, ""

    def regenerate_profile(self, mailID):
        self._OTP = OTP().generate(length=6)
        self._REQUEST_TIME = datetime.datetime.now(tz=datetime.timezone.utc)

        with open(configurations["authlib-store"]) as authlibObject:
            authlib=json.load(authlibObject)

            authlib[mailID]["requestTimestamp"] = str(self._REQUEST_TIME)
            authlib[mailID]["hashedSecret"] = hashlib.md5(self._OTP.encode("UTF-8")).hexdigest()

            write_json(authlib, configurations["authlib-store"])

            return self._OTP


    def verify(self, verification_mail, verification_OTP):
        with open(configurations["authlib-store"]) as authlibObject:
            authlib=json.load(authlibObject)

            if verification_mail not in authlib.keys():
                return RC.ALR11, {}

            verification_profile = authlib[verification_mail]

            if verification_profile["hashedSecret"] == "" and verification_profile["requestTimestamp"] == "" :
                return RC.ALR12, self.regenerate_profile(mailID=verification_mail)

            if hashlib.md5(verification_OTP.encode("UTF-8")).hexdigest() != verification_profile["hashedSecret"]:
                return RC.ALR13, {}
            
            # Generate Secret for Current Timestamp
            current_timestamp = TIMESTAMP().generate(timeframe=1)
            hashed_verification_secret = HASH_SECRET().generate(OTP=verification_OTP, TIMESTAMPS=current_timestamp[0])

            # Dynamic Secret list creation for Request Timestamp till verifiable time frame (90s here)
            verifiable_timeframe = TIMESTAMP().generate(timeframe=configurations["otp-verification-window"], initTime=verification_profile["requestTimestamp"])
            verifiable_secrets = HASH_SECRET().generate(OTP=verification_OTP, TIMESTAMPS=verifiable_timeframe)

            
            if hashed_verification_secret in verifiable_secrets:
                profile = authlib[verification_mail]
                del authlib[verification_mail]
                write_json(authlib, configurations["authlib-store"])
                return RC.ALR14, profile
            else:
                regenerated_otp = self.regenerate_profile(mailID=verification_mail)
                return RC.ALR15, regenerated_otp
