import hashlib


def hash_password(password) -> str:
    return hashlib.sha512(
        password.encode("utf-8")
    ).hexdigest()


class AUTH_PROFILE:
    def __init__(self) -> None:
        pass

    def create_profile(self, mail, request_id, name, secrets, password):
        requested_profile = {
            "email": mail,
            "authRequestID": request_id,
            "name": name,
            "passwordHash": hash_password(password),
            "hashedSecrets": secrets,
            "status": "unverified"
        }
        return requested_profile


# def verify(hash_list, otp):
#     current_timestamp = TIMESTAMP().generate(timeframe=1)

#     gen_2 = HASH_SECRET().generate(OTP=otp, TIMESTAMPS=current_timestamp[0])

#     if gen_2 in hash_list:
#         print("Verified")
#     else:
#         print("Failed")


# _OTP = OTP().generate(length=6)
# print(_OTP)

# _CURRENT_TIMESTAMP = TIMESTAMP().generate(timeframe=20)
# # print(_CURRENT_TIMESTAMP)

# _UUID = UUID().generate()
# # print(_UUID)

# _HASH = HASH_SECRET().generate(OTP=_OTP, TIMESTAMPS=_CURRENT_TIMESTAMP)
# # print(_HASH)

# verify(hash_list=_HASH, otp=input("Enter OTP: "))
