from handlers.generators import HASH_SECRET, OTP, UUID, TIMESTAMP
from handlers.authProfileHandler import AUTH_PROFILE
from logsmith import log
import hashlib
import json
import datetime

log = log()
log.configure(console_only=True, ENV="Dev")

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def hash_password(password) -> str:
    return hashlib.sha512(
        password.encode("utf-8")
    ).hexdigest()


class AUTH_REQUEST:

    def __init__(self) -> None:
        pass

    def register(self, mailID, name, password):
        self.request_id = UUID().generate()
        self._OTP = OTP().generate(length=6)
        self._REQUEST_TIME = datetime.datetime.now(tz=datetime.timezone.utc)

        with open("/workspaces/wunder-identity-provider/dataFiles/authlib.json") as authlibObject:
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
                write_json(authlib, "/workspaces/wunder-identity-provider/dataFiles/authlib.json")
                log.SUCCESS("Registered")
                return self._OTP
            else:
                log.FAILURE("Mail Exists")
                return self._OTP

    def verify(self, verification_mail, verification_OTP):
        with open("/workspaces/wunder-identity-provider/dataFiles/authlib.json") as authlibObject:
            authlib=json.load(authlibObject)
            verification_profile = authlib[verification_mail]

            # Generate Secret for Current Timestamp
            current_timestamp = TIMESTAMP().generate(timeframe=1)
            hashed_verification_secret = HASH_SECRET().generate(OTP=verification_OTP, TIMESTAMPS=current_timestamp[0])

            # Dynamic Secret list creation for Request Timestamp till verifiable time frame (90s here)
            verifiable_timeframe = TIMESTAMP().generate(timeframe=90, initTime=verification_profile["requestTimestamp"])
            verifiable_secrets = HASH_SECRET().generate(OTP=verification_OTP, TIMESTAMPS=verifiable_timeframe)

            if hashed_verification_secret in verifiable_secrets:
                print("Verified")
            else:
                print("Failed")