import hashlib
import string
import random
import datetime
import uuid


# OTP Generator
class OTP:

    def __init__(self):
        self.OTP = ""

    def generate(self, length) -> str:
        # length - Length of OTP
        self.OTP = ''.join(
            random.choices(
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits,
                k=length
            )
        )
        return self.OTP


# TIMESTAMP Generator
class TIMESTAMP:

    def __init__(self) -> None:
        self.current_datetime = datetime.datetime.now(tz=datetime.timezone.utc)

    def generate(self, timeframe):
        # timeframe - OTP Validity Timeframe in Second
        self.timestamp_frame = [
            str(
                datetime.datetime.timestamp(
                    self.current_datetime + datetime.timedelta(seconds=i)
                )
            ).split(".")[0] for i in range(0, timeframe)
        ]

        return self.timestamp_frame


# Request ID Generator
class UUID:

    def __init__(self) -> None:
        self.unique_id = ""

    def generate(self):
        self.unique_id = uuid.uuid4()
        return self.unique_id


# SECRET Generator
class HASH_SECRET:

    def __init__(self) -> None:
        self.secrets = []
        pass

    def generate(self, OTP, TIMESTAMPS):
        if type(TIMESTAMPS) == list:
            for timestamp in TIMESTAMPS:
                secret = f"{timestamp}/{OTP}"
                self.secrets.append(
                    hashlib.sha256(
                        secret.encode("utf-8")
                    ).hexdigest()
                )
        elif type(TIMESTAMPS) == str:
            secret = f"{TIMESTAMPS}/{OTP}"
            self.secrets = hashlib.sha256(
                secret.encode("utf-8")
            ).hexdigest()
        else:
            raise TypeError("TIMESTAMP Type doesn't match.")

        return self.secrets
