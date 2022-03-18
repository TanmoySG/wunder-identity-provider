import string
import random
import datetime
import uuid


# OTP Generator Class
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
        self.unique_id =""

    def generate(self):
        self.unique_id = uuid.uuid4()
        return self.unique_id
