import hashlib


def hash_password(password) -> str:
    return hashlib.sha512(
        password.encode("utf-8")
    ).hexdigest()


class AUTH_PROFILE:
    def __init__(self) -> None:
        pass

    def create_profile(self, mail, request_id, name, secret, requestTimestamp, password):
        requested_profile = {
            "email": mail,
            "authRequestID": request_id,
            "name": name,
            "hashedSecret" : secret,
            "passwordHash": hash_password(password),
            "requestTimestamp": requestTimestamp,
            "status": "unverified"
        }
        return requested_profile
