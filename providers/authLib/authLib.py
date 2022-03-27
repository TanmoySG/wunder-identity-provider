import uuid

from logsmith import log

from handlers.requestHandler import AUTH_REQUEST
from standards.return_codes import RETURN_CODES

#Initiate Logging
log = log()
log.configure(console_only=True, ENV="Dev")


class AUTHLIB:

    def __init__(self) -> None:
        # method defines the authentication method. Can have the values- otp or magic_link
        # Currently only supports otp, to be changed when magic link is implemented
        self.method = "otp"


    def register(self, mailID, username, password):
        response_code, generated_otp = AUTH_REQUEST().register(
            mailID=mailID,
            name=username,
            password=password
        )

        if response_code == RETURN_CODES.ALR01:
            return RETURN_CODES.ALR01["details"]
        elif response_code == RETURN_CODES.ALR02 or response_code == RETURN_CODES.ALR03:
            return generated_otp


    def verify(self, mailID, user_supplied_secret):
        response_code, response_object = AUTH_REQUEST().verify(
            verification_mail=mailID,
            verification_OTP=user_supplied_secret
        )

        if response_code == RETURN_CODES.ALR11:
            return response_code["details"]
        elif response_code == RETURN_CODES.ALR12:
            regenerated_otp = response_object
            return regenerated_otp
        elif response_code == RETURN_CODES.ALR13:
            return response_code["details"]
        elif response_code == RETURN_CODES.ALR14:
            verified_profile = response_object
            return verified_profile
        elif response_code == RETURN_CODES.ALR15:
            regenerated_otp = response_object
            return regenerated_otp
