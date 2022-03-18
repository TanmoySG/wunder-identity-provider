from time import sleep
from generators import OTP, TIMESTAMP, UUID, HASH_SECRET
import datetime


def verify(hash_list, otp):
    current_timestamp = str(
        datetime.datetime.timestamp(
            datetime.datetime.now(
                tz=datetime.timezone.utc
            )
        )
    ).split(".")[0]

    gen_2 = HASH_SECRET().generate(OTP=otp, TIMESTAMPS=current_timestamp)
    if gen_2 in hash_list:
        print("Verified")
    else:
        print("Failed")


_OTP = OTP().generate(length=6)
print(_OTP)

_CURRENT_TIMESTAMP = TIMESTAMP().generate(timeframe=20)
# print(_CURRENT_TIMESTAMP)

_UUID = UUID().generate()
# print(_UUID)

_HASH = HASH_SECRET().generate(OTP=_OTP, TIMESTAMPS=_CURRENT_TIMESTAMP)
# print(_HASH)

sleep(2)

verify(hash_list=_HASH, otp=input("Set OTP "))
