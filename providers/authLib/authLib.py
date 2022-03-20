from time import sleep
from handlers.requestHandler import AUTH_REQUEST

# Eg - In-time verification - should successfully verify account
email_id = "random1@gmail.com"
name="Jane Doe"
pw="123454"

_otp=AUTH_REQUEST().register(mailID=email_id, name=name, password=pw)
AUTH_REQUEST().verify(verification_mail=email_id, verification_OTP=_otp)

# Eg - Out-of timeframe/window verification - Should Fail
email_id = "random2@gmail.com"
name="Jane Doe"
pw="123454"

_otp=AUTH_REQUEST().register(mailID=email_id, name=name, password=pw)
sleep(11) # Verification window 10s
AUTH_REQUEST().verify(verification_mail=email_id, verification_OTP=_otp)