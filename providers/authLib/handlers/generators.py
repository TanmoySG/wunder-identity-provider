import string
import random
import datetime


# OTP Generator Class
class OTP:

    def __init__(self):
        self.OTP = ""

    def generate(self, length) -> str:
        self.OTP = ''.join(
            random.choices(
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits,
                k=length
            )
        )
        return self.OTP


# TIMESTAMP(s) Gnerator Class
class TIMESTAMP:

    def __init__(self) -> None:
        self.current_datetime = datetime.datetime.now(tz=datetime.timezone.utc)

    def timestamp_range(self):
        return [
            str(
                datetime.datetime.timestamp(
                    self.current_datetime + datetime.timedelta(seconds=i)
                )
            ).split(".")[0] for i in range(0, 90)
        ]

    def generate(self):
        self.timestamp_frame = self.timestamp_range()
        return self.timestamp_frame
