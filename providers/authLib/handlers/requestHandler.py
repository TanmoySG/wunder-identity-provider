from handlers.generators import HASH_SECRET, OTP, UUID, TIMESTAMP
from handlers.authProfileHandler import AUTH_PROFILE
from logsmith import log
import hashlib
import json

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
        self._CURRENT_TIMESTAMP = TIMESTAMP().generate(timeframe=90)
        self.secrets_list = HASH_SECRET().generate(
            OTP=self._OTP,
            TIMESTAMPS=self._CURRENT_TIMESTAMP
        )
        with open("/workspaces/wunder-identity-provider/dataFiles/authlib.json") as authlibObject:
            authlib = json.load(authlibObject)
            if mailID not in authlib.keys():
                authlib[mailID] = AUTH_PROFILE().create_profile(
                    mail=mailID,
                    request_id=self.request_id,
                    name=name,
                    secrets=self.secrets_list,
                    password=password
                )
                write_json(authlib, "/workspaces/wunder-identity-provider/dataFiles/authlib.json")
                log.SUCCESS("Registered")
            else:
                log.FAILURE("Mail Exists")

    def verify(self):
        pass
