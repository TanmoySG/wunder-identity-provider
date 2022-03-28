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

    def __init__(self, length) -> None:
        self.length = length

    def generate(self) -> str:
        # return binascii.hexlify(os.urandom(self.length)).decode()
        return secrets.token_hex(self.length)
