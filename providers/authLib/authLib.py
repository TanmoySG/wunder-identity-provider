# from time import sleep
# from handlers.requestHandler import AUTH_REQUEST
# from handlers.maintenanceHandler import MAINTENANCE

# MAINTENANCE().short_term_purge()

# # Eg - In-time verification - should successfully verify account
# email_id = "random1@gmail.com"
# name="Jane Doe"
# pw="123454"

# _otp=AUTH_REQUEST().register(mailID=email_id, name=name, password=pw)

# sleep(5)

# returrn_val = AUTH_REQUEST().verify(verification_mail=email_id, verification_OTP=_otp)

# #placeholder code
# print(returrn_val)

# # Eg - Out-of timeframe/window verification - Should Fail
# email_id = "random2@gmail.com"
# name="Jane Doe"
# pw="123454"

# _otp=AUTH_REQUEST().register(mailID=email_id, name=name, password=pw)
# sleep(5) # Verification window 10s
# returrn_val = AUTH_REQUEST().verify(verification_mail=email_id, verification_OTP=_otp)

# #placeholder code
# print(returrn_val)

import uuid
from handlers.requestHandler import AUTH_REQUEST
from providers.standards.return_codes import RETURN_CODES

class AUTHLIB:

    def __init__(self) -> None:
        # method defines the authentication method. Can have the values- otp or magic_link
        # Currently only supports otp, to be changed when magic link is implemented
        self.method = "otp"


    def register(self, mailID, username, password):
        generated_otp = AUTH_REQUEST().register(
            mailID=mailID,
            name=username,
            password=password
        )
        return generated_otp

    def verification(self, mailID, user_supplied_secret):
        verification_prompt, profile = AUTH_REQUEST().verify(
            verification_mail=mailID,
            verification_OTP=user_supplied_secret
        )

        if verification_prompt == "":
            pass

print(RETURN_CODES().X001)