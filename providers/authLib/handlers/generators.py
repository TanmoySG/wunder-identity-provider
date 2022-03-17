import string, random
import time, datetime

def get_correct_date(date_object):
    pass

class OTP:

    def __init__(self):
        self.OTP = ""

    def generate(self, length) -> str:
        self.OTP = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits , k = length))
        return self.OTP

class TIMESTAMP:

    def __init__(self) -> None:
        current_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        self.current_datatime_object = {
            "day" : current_datetime.day,
            "month" : current_datetime.month,
            "year" : current_datetime.year,
            "hour" : current_datetime.hour,
            "minute" : current_datetime.minute,
            "second" : current_datetime.second
        }

    def timestamp_range(self):


        self.timestamp_frame = [
            datetime.datetime.timestamp(
                datetime.datetime(
                    year=self.current_datatime_object["year"],
                    month=self.current_datatime_object["month"],
                    day=self.current_datatime_object["day"],
                    hour=self.current_datatime_object["hour"],
                    minute=self.current_datatime_object["minute"],
                    second= i+self.current_datatime_object["second"]
                ) 
            ) for i in range(0, 5)
        ]


    def generate(self):
        self.timestamp_range()
        return self.timestamp_frame