import secrets
import os
import datetime
import uuid
import binascii

class USERID:
    def __new__(self) -> str:
        return str(uuid.uuid4())


class REGISTRATION_TIME:
    def __new__(self) -> str:
        return str(
            datetime.datetime.now(
                tz=datetime.timezone.utc
            )
        )


class ACCESS_TOKEN:

    # length [int] - Length of Access Token
    # use_method [secrets | binascii] - Method for generating Token

    def __init__(self, length, use_method="secrets") -> None:
        self.length = length
        self.method = use_method

    def generate(self) -> str:
        if self.method == "binascii" :
            return binascii.hexlify(os.urandom(self.length)).decode()
        elif self.method == "secrets" :
            return secrets.token_urlsafe(self.length)
        else:
            return secrets.token_hex(self.length)
